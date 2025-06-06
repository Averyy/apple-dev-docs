# Creating a camera experience for the Lock Screen

**Framework**: LockedCameraCapture

Offer your app’s camera experience on locked devices from Control Center, the Lock Screen, and the Action button.

#### Overview

A locked camera capture extension allows people to access your app’s camera experience quickly from a WidgetKit control in Control Center, from the Lock Screen, or with the Action button. The lifecycle of a capture extension involves capturing content while a device is locked and allowing someone to continue to your app, once authenticated, to view or complete a task with the captured content.

While your capture extension is active, the system places the following restrictions to ensure people’s security and privacy:

- The capture extension can’t access the network.
- The capture extension can’t read from or write to the App Group’s shared container.
- When the system suspends the capture extension, it erases the capture extension’s container directory. An extension typically suspends when someone dismisses the extension by swiping up from the bottom of the screen or by pressing the side button.
- The app extension terminates shortly after launch if it doesn’t have an active camera view that uses [`AVCaptureEventInteraction`](https://developer.apple.com/documentation/AVKit/AVCaptureEventInteraction) to handle events from the hardware buttons, or if access to the camera hasn’t been requested.

##### Add a Locked Camera Capture Extension to Your Project

The Locked Camera Capture Extension template provides everything you need to start building your capture extension:

1. Open your app project in Xcode and choose File > New > Target.
2. From the Application Extension group, select Capture Extension, and click Next.
3. Enter the name of your extension.
4. Click Finish.

The template creates an extension target that contains an implementation of [`LockedCameraCaptureUIScene`](lockedcameracaptureuiscene.md) that uses a [`UIImagePickerController`](https://developer.apple.com/documentation/UIKit/UIImagePickerController) to capture content using the rear camera.

> **Note**: The capture extension inherits camera permissions from your app. If the person hasn’t granted access, the system prompts them to authenticate and unlock their device. It then opens the app and the app requests access. For more information about requesting camera access, refer to [`Requesting authorization to capture and save media`](https://developer.apple.com/documentation/AVFoundation/requesting-authorization-to-capture-and-save-media).

The capture extension inherits camera permissions from your app. If the person hasn’t granted access, the system prompts them to authenticate and unlock their device. It then opens the app and the app requests access. For more information about requesting camera access, refer to [`Requesting authorization to capture and save media`](https://developer.apple.com/documentation/AVFoundation/requesting-authorization-to-capture-and-save-media).

##### Launch Your App Extension

Create a control widget that launches the capture extension when the device is locked. People will need to add your app’s control to Control Center, the Lock screen, or configure the Action button with it.

Pass data between your app and your app extension on launch with [`CameraCaptureIntent`](https://developer.apple.com/documentation/AppIntents/CameraCaptureIntent). The `appContext` of the `CameraCaptureIntent` data contains up to four KB of user-specific data. Use this data to configure your capture extension’s UI. For example, you can enable previously purchased camera filters, or remember if someone was using the front or rear camera last. Your app or capture extension reads from and writes to the `appContext`. It represents the state of your extension or app when it launches. Use the `CameraCaptureIntent` perform function to deep link to the capture experience in your app. Include the `CameraCaptureIntent` in your app target, control widget extension target, and camera capture extension target. To learn more, refer to [`CameraCaptureIntent`](https://developer.apple.com/documentation/AppIntents/CameraCaptureIntent).

The following code uses a `CameraCaptureIntent` to read the camera’s direction, the front or the rear, from the intent’s `appContext`:

```swift
struct MyAppCaptureIntent: CameraCaptureIntent {
    typealias AppContext = MyAppContext
    static let title = "MyAppCaptureIntent"
    static let description = IntentDescription("Capture photos and videos with MyApp.")

    @MainActor
    func perform() async throws -> some IntentResult {
        do {
            if let context = try await MyAppCaptureIntent.appContext {
                // Read the camera direction from the appContext.
                return context.cameraDirection
            }
        } catch {
            // Handle error condition.
        }
        return .result()
    }
}
```

The following code updates the `appContext` of a `CameraCaptureIntent` when someone changes the direction of the camera in the app:

```swift
Button {
    Task {
        do {
            // Change the direction of the camera.
            ...
            // Update the appContext with the new camera direction.
            try await MyAppCaptureIntent.updateAppContext(content.contextData())
        } catch {
            // Log the error and display to the user.
        }
    }
} label: {
    Image(systemName: “arrow.triangle.2.circlepath.camera”)
    .font(Font.system(size: 44, weight: .medium))
}
```

##### Capture Images and Videos

Once you’ve added your locked camera capture extension to your project, you’re ready to build a view to capture content with.

Display the capture view with [`LockedCameraCaptureUIScene`](lockedcameracaptureuiscene.md). `LockedCameraCaptureUIScene` has a [`LockedCameraCaptureSession`](lockedcameracapturesession.md) property that contains information on where to store captured content, and initiates requests to open the app extension’s containing app.

Create an instance to your capture view in the closure of the `LockedCameraCaptureUIScene`, passing the `LockedCameraCaptureSession` object to the view.

The following code creates an extension with a capture view, passing the `LockedCameraCaptureSession` object to it:

```swift
@main
struct MyCameraCaptureExtension: LockedCameraCaptureExtension {
	var body: some LockedCameraCaptureExtensionScene {
		// The LockedCameraCaptureUIScene contains your extension UI.
		LockedCameraCaptureUIScene { session in
			// The capture view to display.
			Viewfinder(session: session)
		}
	}
} 
```

In your capture view, create a view that starts an active camera session that uses `AVCaptureEventInteraction`. `UIImagePickerController` uses `AVCaptureEventInteraction`, but you can create custom capture views. To learn more about creating custom capture views, refer to [`Setting Up a Capture Session`](https://developer.apple.com/documentation/AVFoundation/setting-up-a-capture-session).

The following code shows how to use UIImagePickerController to capture content in your extension. UIImagePickerController uses AVCaptureEventInteraction and ensures the system won’t terminate your extension after launch:

```swift
struct Viewfinder: UIViewControllerRepresentable {
	// The session variable contains information on where to store captured content
	// and may initiate a request to open the containing app.
	let session: LockedCameraCaptureSession
	var sourceType: UIImagePickerController.SourceType = .camera
	
	init(session: LockedCameraCaptureSession) {
		self.session = session
	}
 
	func makeUIViewController(context: UIViewControllerRepresentableContext<ImagePicker>) -> UIImagePickerController {
		let imagePicker = UIImagePickerController()
		imagePicker.sourceType = sourceType
		imagePicker.mediaTypes = [UTType.image.identifier, UTType.movie.identifier]
		imagePicker.cameraDevice = .rear
 
		return imagePicker
	}
 
	func updateUIViewController(_ uiViewController: UIImagePickerController, context: UIViewControllerRepresentableContext<ImagePicker>) {}
}
```

##### Save Captured Content

Use [`PhotoKit`](https://developer.apple.com/documentation/PhotoKit) or [`sessionContentURL`](lockedcameracapturesession/sessioncontenturl.md) from `LockedCameraCaptureSession` to store all captured content. The URL is a temporary directory that’s created when the app extension launches, within the capture extension’s containing app’s data container. The system erases and resets any content saved to the capture extension’s data container when the capture extension suspends or terminates.

##### Launch Your App From the Capture Extension

You can provide a way for someone to launch your app from the capture extension, making it easy for them to continue a flow using the captured content that requires access not available within the capture extension. For example, you can help someone quickly post a video to a social network, or tap a button to begin editing an image.

Call [`openApplication(for:)`](lockedcameracapturesession/openapplication(for:).md) on the `LockedCameraCaptureSession` to launch the capture extension’s containing app. If the device isn’t authenticated, the system asks the person to authenticate before it launches the app. Provide an `NSUserActivity` that contains the relevant information your app needs to take someone to the correct area of the app. Create your `NSUserActivity` with the [`NSUserActivityTypeLockedCameraCapture`](nsuseractivitytypelockedcameracapture.md) activity type. The `NSUserActivityTypeLockedCameraCapture` activity type tells your app that it was launched from your capture extension.

The systems throws `ApplicationLaunchError` if the application fails to launch. `failureReason` allows you to update the UI, and let someone know why the application wasn’t launched. Failure to authorize and unlock the device is a common reason this error is thrown.

The following code shows a function in the capture extension that uses `openApplication(for:)` to open the capture extension’s containing app. It passes the `NSUserActivityTypeLockedCameraCapture` activity type to let the app know it is being launched from the capture extension. This function also handles the `ApplicationLaunchError` to display an error if the app can’t launch.

```swift
func launchApp(with session: LockedCameraCaptureSession, info: String) {
	Task {
		do {
			let activity = NSUserActivityTypeLockedCameraCapture
			activity.userInfo = [UserInfoKey: info]
			try await session.openApplication(for: activity)
		} catch {
			StatusManager.displayError("Unable to open app - \(error.localizedDescription)")
		}
	}
}
```

##### Access Captured Content in Your App

Use the [`sessionContentUpdates`](lockedcameracapturemanager/sessioncontentupdates.md) `AsyncSequence` from the [`LockedCameraCaptureManager`](lockedcameracapturemanager.md) object in the app to process captured content from the capture extension sessions and move the captured content where it belongs long-term. The sequence begins with the URLs of the current session content directories. The sequence continues providing updates about any newly added or removed session content directories. When transitioning from the capture extension to the app, the most recent session content directory may become available shortly after your app launches.

When you’re done with each directory, use the [`invalidateSessionContent(at:)`](lockedcameracapturemanager/invalidatesessioncontent(at:).md) method on `LockedCameraCaptureManager`. After you invalidate the directory, the system deletes it.

The following code uses `sessionContentUpdates` to process captured content from the capture extension within the app:

```swift
for await update in LockedCameraCaptureManager.shared.sessionContentUpdates {
    switch update {
    case .initial(let urls):
        // Process captured content from existing session content directories.
        break
    case .added(let url):
        // Process captured content from a new session content directory.
        break
    case .removed(let url):
        // Process captured content from a removed session content directory.
        break
    default:
        // An unknown sessionContentUpdate was received.
        break
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/lockedcameracapture/creating-a-camera-experience-for-the-lock-screen)*