# delegate

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

Delegate that receives updates as the camera stream changes.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
weak var delegate: (any HMCameraStreamControlDelegate)? { get set }
```

```objc
@property (nonatomic, weak) id<HMCameraStreamControlDelegate> delegate;
```

## See Also

### Observing stream activity
- [protocol HMCameraStreamControlDelegate](../hmcamerastreamcontroldelegate.md)
  A protocol that gives the delegate updates on the camera stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerastreamcontrol/delegate)*