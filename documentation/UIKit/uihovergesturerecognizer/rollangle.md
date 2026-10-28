# rollAngle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A value that represents the current barrel-roll angle of Apple Pencil.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- visionOS 1.2+

## Declaration

```swift
var rollAngle: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat rollAngle;
```

## Discussion

For models of Apple Pencil that don’t support barrel-roll angle data, the value of this property is `0`.

## See Also

### Supporting Apple Pencil hover
- [var altitudeAngle: CGFloat](./altitudeangle.md)
  A value that represents the altitude angle of the hovering pointing device.
- [func azimuthAngle(in: UIView?) -> CGFloat](./azimuthangle%28in%29.md)
  A value that represents the azimuth angle of the hovering pointing device in the specified view.
- [func azimuthUnitVector(in: UIView?) -> CGVector](./azimuthunitvector%28in%29.md)
  A value that represents the azimuth unit vector of the hovering pointing device in the specified view.
- [var zOffset: CGFloat](./zoffset.md)
  A value that represents the normalized distance between the screen and a hovering pointing device, such as Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihovergesturerecognizer/rollangle)*