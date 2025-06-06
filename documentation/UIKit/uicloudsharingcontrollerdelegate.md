# UICloudSharingControllerDelegate

**Framework**: UIKit  
**Kind**: protocol

The protocol you implement to provide additional information to, and receive notifications from, the CloudKit sharing controller.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UICloudSharingControllerDelegate : NSObjectProtocol
```

#### Overview

Implement an object that conforms to the [`UICloudSharingControllerDelegate`](uicloudsharingcontrollerdelegate.md) protocol when you want to:

- Configure a [`UICloudSharingController`](uicloudsharingcontroller.md) instance.
- Receive notifications from a [`UICloudSharingController`](uicloudsharingcontroller.md) instance as it attempts to save or remove the [`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare) record based on user interactions on the Invitation and People screens.

## Topics

### Configuring the view controller
- [func itemTitle(for: UICloudSharingController) -> String?](uicloudsharingcontrollerdelegate/itemtitle(for:).md)
  Asks the delegate for the title to display on the invitation screen.
- [func itemType(for: UICloudSharingController) -> String?](uicloudsharingcontrollerdelegate/itemtype(for:).md)
  Asks the delegate for the Uniform Type Identifier (UTI) of the item.
- [func itemThumbnailData(for: UICloudSharingController) -> Data?](uicloudsharingcontrollerdelegate/itemthumbnaildata(for:).md)
  Asks the delegate for the thumbnail image data to display on the invitation.
### Processing shared items
- [func cloudSharingController(UICloudSharingController, failedToSaveShareWithError: any Error)](uicloudsharingcontrollerdelegate/cloudsharingcontroller(_:failedtosavesharewitherror:).md)
  Tells the delegate that the CloudKit sharing controller failed to save the share record.
- [func cloudSharingControllerDidStopSharing(UICloudSharingController)](uicloudsharingcontrollerdelegate/cloudsharingcontrollerdidstopsharing(_:).md)
  Tells the delegate that the user has stopped sharing the record.
- [func cloudSharingControllerDidSaveShare(UICloudSharingController)](uicloudsharingcontrollerdelegate/cloudsharingcontrollerdidsaveshare(_:).md)
  Tells the delegate that the CloudKit sharing controller saved the share record.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any UICloudSharingControllerDelegate)?](uicloudsharingcontroller/delegate.md)
  A reference to an object that conforms to the CloudKit sharing controller delegate protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate)*