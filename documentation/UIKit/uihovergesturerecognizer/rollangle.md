# rollAngle

**Framework**: UIKit  
**Kind**: property

A value that represents the current barrel-roll angle of Apple Pencil.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- visionOS 1.2+

## Declaration

```swift
@MainActor
var rollAngle: CGFloat { get }
```

#### Discussion

For models of Apple Pencil that don’t support barrel-roll angle data, the value of this property is `0`.

## See Also

- [var altitudeAngle: CGFloat](uihovergesturerecognizer/altitudeangle.md)
  A value that represents the altitude angle of the hovering pointing device.
- [func azimuthAngle(in: UIView?) -> CGFloat](uihovergesturerecognizer/azimuthangle(in:).md)
  A value that represents the azimuth angle of the hovering pointing device in the specified view.
- [func azimuthUnitVector(in: UIView?) -> CGVector](uihovergesturerecognizer/azimuthunitvector(in:).md)
  A value that represents the azimuth unit vector of the hovering pointing device in the specified view.
- [var zOffset: CGFloat](uihovergesturerecognizer/zoffset.md)
  A value that represents the normalized distance between the screen and a hovering pointing device, such as Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihovergesturerecognizer/rollangle)*