# cloudSharingControllerDidStopSharing(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user has stopped sharing the record.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func cloudSharingControllerDidStopSharing(_ csc: UICloudSharingController)
```

```objc
- (void) cloudSharingControllerDidStopSharing:(UICloudSharingController *) csc;
```

#### Discussion

Implement this method to receive a notification from the [`UICloudSharingController`](../uicloudsharingcontroller.md) instance after the user who owns the [`CKShare`](../../CloudKit/ckshare.md) record stops sharing it with all participants.

## See Also

### Processing shared items
- [func cloudSharingController(UICloudSharingController, failedToSaveShareWithError: any Error)](./cloudsharingcontroller%28_,failedtosavesharewitherror%29.md)
  Tells the delegate that the CloudKit sharing controller failed to save the share record.
- [func cloudSharingControllerDidSaveShare(UICloudSharingController)](./cloudsharingcontrollerdidsaveshare%28_%29.md)
  Tells the delegate that the CloudKit sharing controller saved the share record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate/cloudsharingcontrollerdidstopsharing(_:))*