# cloudSharingControllerDelegate

**Framework**: Shared with You  
**Kind**: property  
**Role**: Instance Property

A reference to an object that conforms to the CloudKit sharing controller delegate protocol.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
weak var cloudSharingControllerDelegate: (any UICloudSharingControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak) id<UICloudSharingControllerDelegate> cloudSharingControllerDelegate;
```

## See Also

### Customizing the cloud-sharing behavior
- [var cloudSharingServiceDelegate: (any NSCloudSharingServiceDelegate)?](./cloudsharingservicedelegate.md)
  A reference to an object that conforms to the cloud-sharing service delegate protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationview/cloudsharingcontrollerdelegate)*