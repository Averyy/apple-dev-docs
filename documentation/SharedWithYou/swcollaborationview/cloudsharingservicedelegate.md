# cloudSharingServiceDelegate

**Framework**: Shared with You  
**Kind**: property  
**Role**: Instance Property

A reference to an object that conforms to the cloud-sharing service delegate protocol.

**Availability**:
- macOS 13.0+

## Declaration

```swift
weak var cloudSharingServiceDelegate: (any NSCloudSharingServiceDelegate)? { get set }
```

```objc
@property (nonatomic, weak) id<NSCloudSharingServiceDelegate> cloudSharingServiceDelegate;
```

## See Also

### Customizing the cloud-sharing behavior
- [var cloudSharingControllerDelegate: (any UICloudSharingControllerDelegate)?](./cloudsharingcontrollerdelegate.md)
  A reference to an object that conforms to the CloudKit sharing controller delegate protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationview/cloudsharingservicedelegate)*