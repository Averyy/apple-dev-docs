# UICloudSharingController

**Framework**: UIKit  
**Kind**: class

A view controller that presents standard screens for adding and removing people from a CloudKit share record.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICloudSharingController
```

#### Overview

CloudKit Sharing provides real-time collaboration between one or more people using your app. A user takes certain steps to make collaboration possible, from inviting people to participate in the collaboration to setting restrictions on what participants can do. To provide these steps to a user, you must make changes to your app. With [`UICloudSharingController`](uicloudsharingcontroller.md), the changes require minimum effort.

The [`UICloudSharingController`](uicloudsharingcontroller.md) view controller class provides screens, presented within your app, for managing the people, permissions, and access rights associated with a [`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare) record. The controller, along with a few lines of your own code, facilitates the setup and management of online sharing between users, making it possible for a user to:

- Invite people to view or collaborate on a shared record
- Set the access rights determining who can access the shared record (only people invited or anyone with the share link)
- Set general or individual permissions (read-only or read/write)
- Remove access from one or more participants
- Stop participating (if the user is a participant)
- Stop sharing with all participants (if the user is the owner of the shared record)

The controller provides these different actions to the user based on the user’s role. If the user is the individual sharing the record (where the record is an instance of [`CKRecord`](https://developer.apple.com/documentation/CloudKit/CKRecord) representing the data to share), then the user is called the . A user who has access to the shared record and isn’t the owner is known as a . There’s no need for you to specify the user’s role. The controller determines the role automatically.

##### Inviting Participants to a New Share

The user who owns the data, represented as a [`CKRecord`](https://developer.apple.com/documentation/CloudKit/CKRecord), can invite others to view or collaborate on changes to the data. To invite participants, the owner sends the share link to the other people. To provide this capability in your app, create an instance of [`UICloudSharingController`](uicloudsharingcontroller.md) using the [`init(preparationHandler:)`](uicloudsharingcontroller/init(preparationhandler:).md) initializer method. You use this initializer method only when the owner isn’t already sharing the record.

After creating the controller, you present it. The controller displays the Invitation screen. Using this screen, the owner can add participants and set restrictions on the shared record. Once done, the owner sends the share link to the participants.

However, before the owner can send the share link, CloudKit must generate the link. This link generation happens when saving a new [`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare) record, but when do you save it? You save the share record in the `preparationHandler:`.

After the owner’s selections are complete, the controller invokes the preparation handler provided in the initializer call. In the handler, you create a new [`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare) instance, initializing it with the [`CKRecord`](https://developer.apple.com/documentation/CloudKit/CKRecord) instance that represents the data to share. (This record is called the “root record.”) Next, you save the share and root records using [`CKModifyRecordsOperation`](https://developer.apple.com/documentation/CloudKit/CKModifyRecordsOperation). Finally, you return the shared record to the controller or return an error if the save failed. See the following code for an example of this in action.

##### Adding and Removing Participants From an Existing Share

To allow the owner of an existing share to manage the participants, create the [`UICloudSharingController`](uicloudsharingcontroller.md) instance using the [`init(share:container:)`](uicloudsharingcontroller/init(share:container:).md) initializer method.

After you create the controller, present it to show the People screen. From this screen, the owner can:

- Add and remove participants
- Change the share’s access options from private to public, or public to private
- Change the share’s permissions from read-only to read/write, or vice versa
- Stop sharing with all participants

> **Note**:  If all participants have left the share, the controller presents the Invitation screen, not the People screen, when [`init(share:container:)`](uicloudsharingcontroller/init(share:container:).md) is used to create the controller instance.

 If all participants have left the share, the controller presents the Invitation screen, not the People screen, when [`init(share:container:)`](uicloudsharingcontroller/init(share:container:).md) is used to create the controller instance.

##### Viewing Participants and Leaving a Share

To allow a participant to view the list of participants and remove themselves from a share, create the [`UICloudSharingController`](uicloudsharingcontroller.md) instance using the [`init(share:container:)`](uicloudsharingcontroller/init(share:container:).md) initializer method.

After you create the controller, present it to show the People screen. From this screen, the participant can:

- View the list of participants
- Copy the share link to send to others (if the owner has made the share publicly available)
- Leave the share

##### Presenting the Controller

[`UICloudSharingController`](uicloudsharingcontroller.md) is designed for use in a popover. Therefore, you should always set the [`popoverPresentationController`](uiviewcontroller/popoverpresentationcontroller.md) source information before presenting the Cloud sharing controller. Doing this ensures that the [`UICloudSharingController`](uicloudsharingcontroller.md) instance is displayed properly across all device types.

> ❗ **Important**:  Presenting the Cloud sharing controller in an iPad app without setting the popover presentation controller causes a run-time error.

 Presenting the Cloud sharing controller in an iPad app without setting the popover presentation controller causes a run-time error.

The following code shows an example of setting the [`popoverPresentationController`](uiviewcontroller/popoverpresentationcontroller.md) before presenting a Cloud sharing controller.

##### Configuring the Controller

By default, the [`UICloudSharingController`](uicloudsharingcontroller.md) user interface displays a generic thumbnail image and title to the user. You can, however, change these to app-specific representations of the shared record. You accomplish this by setting the controller’s [`delegate`](uicloudsharingcontroller/delegate.md) property to an object that conforms to the [`UICloudSharingControllerDelegate`](uicloudsharingcontrollerdelegate.md) protocol, making sure to implement the [`itemThumbnailData(for:)`](uicloudsharingcontrollerdelegate/itemthumbnaildata(for:).md) and [`itemTitle(for:)`](uicloudsharingcontrollerdelegate/itemtitle(for:).md) delegate methods.

You can also show or hide the permission and access options presented to the user by setting the [`availablePermissions`](uicloudsharingcontroller/availablepermissions.md) property on the [`UICloudSharingController`](uicloudsharingcontroller.md) instance.

## Topics

### Creating the cloud sharing controller
- [init(preparationHandler: (UICloudSharingController, (CKShare?, CKContainer?, (any Error)?) -> Void) -> Void)](uicloudsharingcontroller/init(preparationhandler:).md)
  Initializes the CloudKit sharing controller with a preparation handler intending to save a new share record.
- [init(share: CKShare, container: CKContainer)](uicloudsharingcontroller/init(share:container:).md)
  Initializes the CloudKit sharing view controller with a CloudKit share record and container to manage participants and restrictions.
### Customizing the cloud sharing controller behavior
- [var delegate: (any UICloudSharingControllerDelegate)?](uicloudsharingcontroller/delegate.md)
  A reference to an object that conforms to the CloudKit sharing controller delegate protocol.
- [protocol UICloudSharingControllerDelegate](uicloudsharingcontrollerdelegate.md)
  The protocol you implement to provide additional information to, and receive notifications from, the CloudKit sharing controller.
### Configuring the permissions
- [var availablePermissions: UICloudSharingController.PermissionOptions](uicloudsharingcontroller/availablepermissions.md)
  A combination of permission and access options made available to the user when viewing screens presented by the CloudKit sharing controller.
- [UICloudSharingController.PermissionOptions](uicloudsharingcontroller/permissionoptions.md)
  A set of options that determine the permission options available to the user when viewing the Cloud sharing controller screens.
### Getting the share
- [var share: CKShare?](uicloudsharingcontroller/share.md)
  A reference to the CloudKit share record used by the CloudKit sharing controller.
### Getting an activity item source
- [func activityItemSource() -> any UIActivityItemSource](uicloudsharingcontroller/activityitemsource.md)
  The activity item object that can be used by an activity view controller.

## Relationships

### Inherits From
- [UIViewController](uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UIContentContainer](uicontentcontainer.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UIStateRestoring](uistaterestoring.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontroller)*