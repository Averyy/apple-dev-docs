# Creating a collaborative photo gallery with SharePlay

**Framework**: Group Activities

Build a shared photo gallery by using SharePlay to synchronize images among participants.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- Xcode 26.0+

#### Overview

SharePlay allows multiple people to collaborate and share content such as photos or files with each other.

This sample code project uses SharePlay to create a shared photo gallery containing images. Participants in a FaceTime call, or using nearby sharing on visionOS, can upload images to share with each other. All participants in the session see the changes in real time.

While running the app, Control-clicking or long-pressing on an image gives you the option to remove an image or open it with [`Quick Look`](https://developer.apple.com/documentation/quicklook) as a preview. When you open a QuickLook preview, the window opens only for you.

SharePlay allows you to share different types of data among participants. Because this sample sends larger amounts of data, like images and files, it uses [`GroupSessionJournal`](groupsessionjournal.md) to share data. For smaller amounts of data or more time-sensitive messages, like adding a comment to someone’s shared image, use [`GroupSessionMessenger`](groupsessionmessenger.md). For more information, see [`Synchronizing data during a SharePlay activity`](synchronizing-data-during-a-shareplay-activity.md).

> **Note**: SharePlay requires the `Group Activities` capability. For instructions on adding a capability to Xcode, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/xcode/adding-capabilities-to-your-app).

For a SharePlay sample code project that uses `GroupSessionMessenger`, see [`Implementing SharePlay for immersive spaces in visionOS`](https://developer.apple.com/documentation/visionos/implementing-shareplay-for-immersive-spaces-in-visionos).

#### Define a Custom Group Activity

The app creates a [`GroupActivity`](groupactivity.md) called `PhotoShareActivity` that defines the photo-sharing experience and allows you to start an activity-related SharePlay session. The activity provides metadata, like the title and type of the activity, which appears in the system UI when people share an experience.

```swift
struct PhotoShareActivity: GroupActivity, Transferable {
    /// Configures the displayed SharePlay activity metadata.
    var metadata: GroupActivityMetadata = {
        var metadata = GroupActivityMetadata()
        metadata.type = .generic
        metadata.title = "Share Photos"
        metadata.subtitle = "Collaborate on a shared photo album."
        return metadata
    }()
}
```

For more information, see [`Defining your app’s SharePlay activities`](defining-your-apps-shareplay-activities.md).

#### Start a Shareplay Session

The app’s toolbar includes a button to start a SharePlay session, but the implementation differs by platform.

For iOS and macOS apps, the button is a [`ShareLink`](https://developer.apple.com/documentation/swiftui/sharelink), which shows the share sheet when tapped or clicked. If a FaceTime call is active, it allows you to start a new SharePlay session; otherwise you can start a new FaceTime call:

```swift
ShareLink(item: PhotoShareActivity(), preview: SharePreview("Share photos")) {
    Image(systemName: "shareplay")
}
```

In visionOS, the app uses a custom button that starts the activity immediately by calling [`activate()`](groupactivity/activate().md) on `PhotoShareActivity` if the person is on a FaceTime call. Otherwise, the system shows the share sheet to help you start a FaceTime call.

```swift
Button {
    Task { @concurrent in
        do {
            // Directly start the group activity.
            if !(try await PhotoShareActivity().activate()) {
                logger.log("The session wasn't created, or it was handed off to an Apple TV.")
            }
        } catch {
            // The session failed to start.
            logger.log("Failed to create a session: \(error.localizedDescription)")
        }
    }
} label: {
    Image(systemName: "shareplay")
}
```

visionOS apps also allow people to start an activity from the Share Window menu in the window bar of an app while in a FaceTime call. To donate the activity to the menu, the main view includes a [`ShareLink`](https://developer.apple.com/documentation/swiftui/sharelink), which is hidden from the UI with the [`hidden()`](https://developer.apple.com/documentation/swiftui/view/hidden()) modifier.

```swift
ShareLink(item: PhotoShareActivity(), preview: SharePreview("Share Images"))
    .hidden()
```

For more information, see [`Presenting SharePlay activities from your app’s UI`](promoting-shareplay-activities-from-your-apps-ui.md).

#### Join and Manage the Activity

When someone starts a SharePlay session, the system creates a [`GroupSession`](groupsession.md) for the custom activity to synchronize content between devices. To join an existing activity, the `observeGroupSessions` function continuously monitors for new `PhotoShareActivity` sessions. When one becomes available, the function starts observing the session state and creates a `SessionController` to manage the session. To ensure that locally uploaded images are shared when the activity begins, the function also uploads those images to the [`GroupSessionJournal`](groupsessionjournal.md) object:

```swift
 private func observeGroupSessions() async {
    // When a new `GroupSession` of `PhotoShareActivity` is available, set up a `SessionController` 
    // to manage the session and join it.
    for await session in PhotoShareActivity.sessions() {
        let sessionController = await SessionController(session, appModel: self)

        self.sessionController = sessionController

        // Create a task on the same actor to observe the group session state and clear the
        // session controller when the group session invalidates.
        Task.immediate(name: "session state observation") {
            for await state in session.$state.values {
                guard self.sessionController?.session.id == session.id else {
                    return
                }

                if case .invalidated = state {
                    self.sessionController = nil
                    return
                }
            }
        }

        // Share existing finished images when the session starts.
        await shareExistingImages(to: sessionController)
    }
}
```

The sample creates a `SessionController` to set up the `GroupSession` with the photo-sharing activity, create the journal object to share images, and handle state synchronization. The session controller then starts observing incoming updates on the `GroupSessionJournal` before adding the person to the session.

```swift
init(_ groupSession: GroupSession<PhotoShareActivity>, appModel: AppModel) async {
   // Keep track of the current session.
   session = groupSession

   // Create a journal using the incoming session.
   groupSessionJournal = GroupSessionJournal(session: session)

   self.appModel = appModel

   // Monitor for incoming attachments.
   observeIncomingImagesTask = observeJournalAttachments()

   // Join the session.
   session.join()
}
```

Because people probably won’t join the call at the same time, the app needs to handle bringing people up to date. `GroupSessionJournal` handles this for you to mitigate re-uploading large attachments. For more information on handling this if you’re syncing other data, see [`Joining and managing a shared activity`](joining-and-managing-a-shared-activity.md). For an example, see [`Implementing SharePlay for immersive spaces in visionOS`](https://developer.apple.com/documentation/visionos/implementing-shareplay-for-immersive-spaces-in-visionos) or [`Building a guessing game for visionOS`](building-a-guessing-game-for-visionos.md).

#### Upload Images

The app uses a [`PhotosPicker`](https://developer.apple.com/documentation/photosui/photospicker) to allow people to upload images from their photo library. For more information on using `PhotosPicker` in SwiftUI, see [`Bringing Photos picker to your SwiftUI app`](https://developer.apple.com/documentation/photokit/bringing-photos-picker-to-your-swiftui-app).

The sample app represents images chosen from the photo picker as instances of `DisplayImage`, a [`Transferable`](https://developer.apple.com/documentation/coretransferable/transferable) structure that stores image data and metadata like the date created and the owner.

When someone chooses an image from the photo picker, the app loads a `Data` object from the [`PhotosPickerItem`](https://developer.apple.com/documentation/photosui/photospickeritem) that represents the image and updates the local images array with that data:

```swift
 if let loadedData = try await photoPickerItem.loadTransferable(type: Data.self) {
    // Data loaded successfully, create the `DisplayImage`.
    var displayImage = DisplayImage(owner: self.name, id: imageID)
    displayImage.imageData = loadedData
    self.localImagesByIdentifier[imageID] = displayImage

    // Clean up the task when complete.
    imageLoadingTasks.removeValue(forKey: imageID)

    // Share the image with other participants, if a session is active.
    await sessionController?.addNewImage(displayImage)
}
```

If the sample app has an existing SharePlay session, the method shares the local images with the other participants. If there isn’t an existing SharePlay session, the UI uses the image data in `localImagesByIdentifier` and initializes an [`Image`](https://developer.apple.com/documentation/swiftui/image) using that data.

#### Synchronize Files Between Participants

To synchronize the images between participants, the app creates a [`GroupSessionJournal`](groupsessionjournal.md) object to add and removes images from the shared session. For an overview of `GroupSessionJournal`, watch the WWDC23 session [`Share files with SharePlay`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10241).

When someone chooses an image with the photos picker during a SharePlay session, the app syncs it with other participants by adding it to the group’s journal using [`add(_:)`](groupsessionjournal/add(_:).md):

```swift
   func addNewImage(_ image: DisplayImage) async {
    do {
        loadingAttachmentCount += 1
        defer { loadingAttachmentCount -= 1 }

        // Add the attachment.
        receivedImages[image.id] = image
        let newAttachment = try await groupSessionJournal.add(image, metadata: image.id)
        attachments[image.id] = newAttachment
    } catch {
        self.logger.log("Error while adding file: \(error.localizedDescription)")
    }
}
```

When another participant adds or removes an attachment, the journal updates the [`attachments`](groupsessionjournal/attachments-swift.property.md) property. The `SessionController` configures the following task when initialized to listen for asynchronous updates to the attachments and executes the task to load them into the app:

```swift
private func observeJournalAttachments() -> Task<Void, Error> {
    return Task {
        for await attachments in groupSessionJournal.attachments {
            await processIncomingAttachments(attachments)
        }
    }
}
```

The `processIncomingAttachments` method loads the contents of the incoming attachment as a `DisplayImage` by calling [`load(_:)`](groupsessionjournal/attachment/load(_:).md) on it, and specifying the `DisplayImage` type. The method saves the data in a dictionary, which the UI iterates over and uses to initialize an [`Image`](https://developer.apple.com/documentation/swiftui/image) to show to all participants:

```swift
private func loadAttachment(_ attachment: GroupSessionJournal.Attachment) async {
    do {
        loadingAttachmentCount += 1
        defer { loadingAttachmentCount -= 1 }
        // Load the image.
        let displayImage = try await attachment.load(DisplayImage.self)
        logger.log("Successfully loaded attachment data for: \(displayImage.id)")

        // Store the attachment reference.
        attachments[displayImage.id] = attachment

        // Add to received images array.
        self.receivedImages[displayImage.id] = displayImage
    } catch {
        logger.log("Failed to process attachment \(attachment.id): \(error)")
    }
}
```

> ❗ **Important**: Don’t call `load(_:)` on attachments you add to the `GroupSessionJournal` object. The sample handles displaying these images by adding them to the `receivedImages` dictionary while adding them to the journal, rather than loading them from the journal’s attachments and adding them then.

For more information on sending and receiving data, see [`Synchronizing data during a SharePlay activity`](synchronizing-data-during-a-shareplay-activity.md).

## See Also

- [Synchronizing data during a SharePlay activity](synchronizing-data-during-a-shareplay-activity.md)
  Send custom messages and data between devices to synchronize content for your activity, and incorporate messages your app receives from other participants.
- [class GroupSessionMessenger](groupsessionmessenger.md)
  An object that transfers app-specific data between the devices joined in a group session.
- [class GroupSessionJournal](groupsessionjournal.md)
  An object that manages file and data transfers between participants joined in a group session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/creating-a-collaborative-photo-gallery-with-shareplay)*