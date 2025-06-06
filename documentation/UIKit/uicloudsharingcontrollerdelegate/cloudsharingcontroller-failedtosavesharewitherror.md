# cloudSharingController(_:failedToSaveShareWithError:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Tells the delegate that the CloudKit sharing controller failed to save the share record.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func cloudSharingController(_ csc: UICloudSharingController, failedToSaveShareWithError error: any Error)
```

#### Discussion

Implement this method to receive a notification from the [`UICloudSharingController`](uicloudsharingcontroller.md) instance after it fails to save changes to the [`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare) record.

## See Also

- [func cloudSharingControllerDidStopSharing(UICloudSharingController)](uicloudsharingcontrollerdelegate/cloudsharingcontrollerdidstopsharing(_:).md)
  Tells the delegate that the user has stopped sharing the record.
- [func cloudSharingControllerDidSaveShare(UICloudSharingController)](uicloudsharingcontrollerdelegate/cloudsharingcontrollerdidsaveshare(_:).md)
  Tells the delegate that the CloudKit sharing controller saved the share record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicloudsharingcontrollerdelegate/cloudsharingcontroller(_:failedtosavesharewitherror:))*