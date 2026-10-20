# force

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

The amount of force applied by the touch.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var force: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat force;
```

#### Discussion

This is a value predetermined by the system and isn’t user specific. A value of 1.0 represents the force of an average touch.

## See Also

### Getting the point’s touch data
- [var altitude: CGFloat](./altitude.md)
  The altitude of this point in radians.
- [var azimuth: CGFloat](./azimuth.md)
  The azimuth of this point in radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokepointreference/force)*