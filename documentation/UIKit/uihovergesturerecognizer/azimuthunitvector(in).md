# azimuthUnitVector(in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

A value that represents the azimuth unit vector of the hovering pointing device in the specified view.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- visionOS 1.0+

## Declaration

```swift
func azimuthUnitVector(in view: UIView?) -> CGVector
```

```objc
- (CGVector) azimuthUnitVectorInView:(UIView *) view;
```

## Return Value

A [`CGVector`](../../CoreFoundation/cgvector.md) that represents the azimuth unit vector of the hovering pointing device.

## Discussion

If the specified view is `nil`, the method returns the azimuth unit vector of the hovering pointing device in the gesture recognizer’s window.

This method returns an empty vector for devices that don’t support azimuth.

## Parameters

- `view`: The view the vector is relative to.

## See Also

### Supporting Apple Pencil hover
- [var altitudeAngle: CGFloat](./altitudeangle.md)
  A value that represents the altitude angle of the hovering pointing device.
- [func azimuthAngle(in: UIView?) -> CGFloat](./azimuthangle%28in%29.md)
  A value that represents the azimuth angle of the hovering pointing device in the specified view.
- [var rollAngle: CGFloat](./rollangle.md)
  A value that represents the current barrel-roll angle of Apple Pencil.
- [var zOffset: CGFloat](./zoffset.md)
  A value that represents the normalized distance between the screen and a hovering pointing device, such as Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uihovergesturerecognizer/azimuthunitvector(in:))*