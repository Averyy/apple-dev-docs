# cloudSharingControllerDidSaveShare(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the CloudKit sharing controller saved the share record.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func cloudSharingControllerDidSaveShare(_ csc: UICloudSharingController)
```

```objc
- (void) cloudSharingControllerDidSaveShare:(UICloudSharingController *) csc;
```

## Discussion

Implement this method to receive a notification from the [`UICloudSharingController`](../uicloudsharingcontroller.md) instance after it saves changes to the [`CKShare`](../../CloudKit/ckshare.md) record.

## See Also

### Processing shared items
- [func cloudSharingController(UICloudSharingController, failedToSaveShareWithError: any Error)](./cloudsharingcontroller%28_,failedtosavesharewitherror%29.md)
  Tells the delegate that the CloudKit sharing controller failed to save the share record.
- [func cloudSharingControllerDidStopSharing(UICloudSharingController)](./cloudsharingcontrollerdidstopsharing%28_%29.md)
  Tells the delegate that the user has stopped sharing the record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate/cloudsharingcontrollerdidsaveshare(_:))*