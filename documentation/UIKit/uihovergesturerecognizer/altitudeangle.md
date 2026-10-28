# altitudeAngle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A value that represents the altitude angle of the hovering pointing device.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- visionOS 1.0+

## Declaration

```swift
var altitudeAngle: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat altitudeAngle;
```

## Discussion

This value is `0` for devices that don’t support altitude.

## See Also

### Supporting Apple Pencil hover
- [func azimuthAngle(in: UIView?) -> CGFloat](./azimuthangle%28in%29.md)
  A value that represents the azimuth angle of the hovering pointing device in the specified view.
- [func azimuthUnitVector(in: UIView?) -> CGVector](./azimuthunitvector%28in%29.md)
  A value that represents the azimuth unit vector of the hovering pointing device in the specified view.
- [var rollAngle: CGFloat](./rollangle.md)
  A value that represents the current barrel-roll angle of Apple Pencil.
- [var zOffset: CGFloat](./zoffset.md)
  A value that represents the normalized distance between the screen and a hovering pointing device, such as Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihovergesturerecognizer/altitudeangle)*