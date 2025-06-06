# azimuthAngle(in:)

**Framework**: UIKit  
**Kind**: method

A value that represents the azimuth angle of the hovering pointing device in the specified view.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func azimuthAngle(in view: UIView?) -> CGFloat
```

#### Return Value

A [`CGFloat`](https://developer.apple.com/documentation/CoreFoundation/CGFloat-swift.struct) that represents the azimuth angle of the hovering pointing device.

#### Discussion

If the specified view is `nil`, the method returns the azimuth angle of the hovering pointing device in the gesture recognizer’s window.

This method returns `0` for devices that don’t support azimuth.

## Parameters

- `view`: The view the angle is relative to.

## See Also

- [var altitudeAngle: CGFloat](uihovergesturerecognizer/altitudeangle.md)
  A value that represents the altitude angle of the hovering pointing device.
- [func azimuthUnitVector(in: UIView?) -> CGVector](uihovergesturerecognizer/azimuthunitvector(in:).md)
  A value that represents the azimuth unit vector of the hovering pointing device in the specified view.
- [var rollAngle: CGFloat](uihovergesturerecognizer/rollangle.md)
  A value that represents the current barrel-roll angle of Apple Pencil.
- [var zOffset: CGFloat](uihovergesturerecognizer/zoffset.md)
  A value that represents the normalized distance between the screen and a hovering pointing device, such as Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihovergesturerecognizer/azimuthangle(in:))*