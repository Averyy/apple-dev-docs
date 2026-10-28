# UICloudSharingControllerDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

The protocol you implement to provide additional information to, and receive notifications from, the CloudKit sharing controller.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
@MainActor
protocol UICloudSharingControllerDelegate : NSObjectProtocol
```

```objc
@protocol UICloudSharingControllerDelegate <NSObject>
```

## Overview

Implement an object that conforms to the [`UICloudSharingControllerDelegate`](./uicloudsharingcontrollerdelegate.md) protocol when you want to:

- Configure a [`UICloudSharingController`](./uicloudsharingcontroller.md) instance.
- Receive notifications from a [`UICloudSharingController`](./uicloudsharingcontroller.md) instance as it attempts to save or remove the [`CKShare`](../CloudKit/ckshare.md) record based on user interactions on the Invitation and People screens.

## Topics

### Configuring the view controller
- [func itemTitle(for: UICloudSharingController) -> String?](./uicloudsharingcontrollerdelegate/itemtitle%28for%29.md)
  Asks the delegate for the title to display on the invitation screen.
- [func itemType(for: UICloudSharingController) -> String?](./uicloudsharingcontrollerdelegate/itemtype%28for%29.md)
  Asks the delegate for the Uniform Type Identifier (UTI) of the item.
- [func itemThumbnailData(for: UICloudSharingController) -> Data?](./uicloudsharingcontrollerdelegate/itemthumbnaildata%28for%29.md)
  Asks the delegate for the thumbnail image data to display on the invitation.
### Processing shared items
- [func cloudSharingController(UICloudSharingController, failedToSaveShareWithError: any Error)](./uicloudsharingcontrollerdelegate/cloudsharingcontroller%28_,failedtosavesharewitherror%29.md)
  Tells the delegate that the CloudKit sharing controller failed to save the share record.
- [func cloudSharingControllerDidStopSharing(UICloudSharingController)](./uicloudsharingcontrollerdelegate/cloudsharingcontrollerdidstopsharing%28_%29.md)
  Tells the delegate that the user has stopped sharing the record.
- [func cloudSharingControllerDidSaveShare(UICloudSharingController)](./uicloudsharingcontrollerdelegate/cloudsharingcontrollerdidsaveshare%28_%29.md)
  Tells the delegate that the CloudKit sharing controller saved the share record.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Customizing the cloud sharing controller behavior
- [var delegate: (any UICloudSharingControllerDelegate)?](./uicloudsharingcontroller/delegate.md)
  A reference to an object that conforms to the CloudKit sharing controller delegate protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate)*