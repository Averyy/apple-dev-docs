# delegate

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

Delegate that receives updates as the camera takes snapshots.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
weak var delegate: (any HMCameraSnapshotControlDelegate)? { get set }
```

```objc
@property (nonatomic, weak) id<HMCameraSnapshotControlDelegate> delegate;
```

## See Also

### Observing snapshot activity
- [protocol HMCameraSnapshotControlDelegate](../hmcamerasnapshotcontroldelegate.md)
  A set of methods used to observe the camera’s snapshot activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerasnapshotcontrol/delegate)*