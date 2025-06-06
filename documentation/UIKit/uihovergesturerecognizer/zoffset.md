# zOffset

**Framework**: UIKit  
**Kind**: property

A value that represents the normalized distance between the screen and a hovering pointing device, such as Apple Pencil.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var zOffset: CGFloat { get }
```

#### Discussion

This value is `1` at the maximum distance from the screen and approaches `0` as the pointing device gets closer to the screen. This value is `0` for devices that don’t support [`zOffset`](uihovergesturerecognizer/zoffset.md).

For example, a drawing app might use the value of this property to generate a preview that indicates where a hovering Apple Pencil touches down on an iPad screen. For more information, see [`Adopting hover support for Apple Pencil`](adopting-hover-support-for-apple-pencil.md).

## See Also

- [var altitudeAngle: CGFloat](uihovergesturerecognizer/altitudeangle.md)
  A value that represents the altitude angle of the hovering pointing device.
- [func azimuthAngle(in: UIView?) -> CGFloat](uihovergesturerecognizer/azimuthangle(in:).md)
  A value that represents the azimuth angle of the hovering pointing device in the specified view.
- [func azimuthUnitVector(in: UIView?) -> CGVector](uihovergesturerecognizer/azimuthunitvector(in:).md)
  A value that represents the azimuth unit vector of the hovering pointing device in the specified view.
- [var rollAngle: CGFloat](uihovergesturerecognizer/rollangle.md)
  A value that represents the current barrel-roll angle of Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihovergesturerecognizer/zoffset)*