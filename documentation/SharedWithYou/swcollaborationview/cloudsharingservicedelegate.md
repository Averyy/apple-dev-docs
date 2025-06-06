# cloudSharingServiceDelegate

**Framework**: Shared With You  
**Kind**: property

A reference to an object that conforms to the cloud-sharing service delegate protocol.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
weak var cloudSharingServiceDelegate: (any NSCloudSharingServiceDelegate)? { get set }
```

## See Also

- [var cloudSharingControllerDelegate: (any UICloudSharingControllerDelegate)?](swcollaborationview/cloudsharingcontrollerdelegate.md)
  A reference to an object that conforms to the CloudKit sharing controller delegate protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationview/cloudsharingservicedelegate)*