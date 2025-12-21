# cloudSharingControllerDelegate

**Framework**: Shared with You  
**Kind**: property

A reference to an object that conforms to the CloudKit sharing controller delegate protocol.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var cloudSharingControllerDelegate: (any UICloudSharingControllerDelegate)? { get set }
```

## See Also

- [var cloudSharingServiceDelegate: (any NSCloudSharingServiceDelegate)?](swcollaborationview/cloudsharingservicedelegate.md)
  A reference to an object that conforms to the cloud-sharing service delegate protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationview/cloudsharingcontrollerdelegate)*