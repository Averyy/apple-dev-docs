# cloudSharingControllerDidStopSharing(_:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the user has stopped sharing the record.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func cloudSharingControllerDidStopSharing(_ csc: UICloudSharingController)
```

#### Discussion

Implement this method to receive a notification from the [`UICloudSharingController`](uicloudsharingcontroller.md) instance after the user who owns the [`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare) record stops sharing it with all participants.

## See Also

- [func cloudSharingController(UICloudSharingController, failedToSaveShareWithError: any Error)](uicloudsharingcontrollerdelegate/cloudsharingcontroller(_:failedtosavesharewitherror:).md)
  Tells the delegate that the CloudKit sharing controller failed to save the share record.
- [func cloudSharingControllerDidSaveShare(UICloudSharingController)](uicloudsharingcontrollerdelegate/cloudsharingcontrollerdidsaveshare(_:).md)
  Tells the delegate that the CloudKit sharing controller saved the share record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate/cloudsharingcontrollerdidstopsharing(_:))*