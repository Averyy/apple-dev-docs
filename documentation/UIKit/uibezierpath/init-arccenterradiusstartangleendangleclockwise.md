# init(arcCenter:radius:startAngle:endAngle:clockwise:)

**Framework**: UIKit  
**Kind**: init

Creates and returns a new Bézier path object with an arc of a circle.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(arcCenter center: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)
```

#### Return Value

A new path object with the specified arc.

#### Discussion

This method creates an open subpath. The created arc lies on the perimeter of the specified circle. When drawn in the default coordinate system, the start and end angles are based on the unit circle shown in the following image. For example, specifying a start angle of `0` radians, an end angle of `π` radians, and setting the `clockwise` parameter to [`true`](https://developer.apple.com/documentation/Swift/true) draws the bottom half of the circle. However, specifying the same start and end angles but setting the `clockwise` parameter to [`false`](https://developer.apple.com/documentation/Swift/false) draws the top half of the circle.

![None](https://docs-assets.developer.apple.com/published/fd7ade1defacc38b836731230bf4694d/media-1965853.jpg)

After calling this method, the current point is set to the point on the arc at the end angle of the circle.

## Parameters

- `center`: Specifies the center point of the circle (in the current coordinate system) used to define the arc.
- `radius`: Specifies the radius of the circle used to define the arc.
- `startAngle`: Specifies the starting angle of the arc (measured in radians).
- `endAngle`: Specifies the end angle of the arc (measured in radians).
- `clockwise`: The direction in which to draw the arc.

## See Also

- [convenience init(rect: CGRect)](uibezierpath/init(rect:).md)
  Creates and returns a new Bézier path object with a rectangular path.
- [convenience init(ovalIn: CGRect)](uibezierpath/init(ovalin:).md)
  Creates and returns a new Bézier path object with an inscribed oval path in the specified rectangle.
- [convenience init(roundedRect: CGRect, cornerRadius: CGFloat)](uibezierpath/init(roundedrect:cornerradius:).md)
  Creates and returns a new Bézier path object with a rounded rectangular path.
- [convenience init(roundedRect: CGRect, byRoundingCorners: UIRectCorner, cornerRadii: CGSize)](uibezierpath/init(roundedrect:byroundingcorners:cornerradii:).md)
  Creates and returns a new Bézier path object with a rectangular path rounded at the specified corners.
- [convenience init(cgPath: CGPath)](uibezierpath/init(cgpath:).md)
  Creates and returns a new Bézier path object with the contents of a Core Graphics path.
- [func reversing() -> UIBezierPath](uibezierpath/reversing.md)
  Creates and returns a new Bézier path object with the reversed contents of the current path.
- [init()](uibezierpath/init.md)
  Creates and returns an empty path object.
- [init?(coder: NSCoder)](uibezierpath/init(coder:).md)
  Creates a Bézier path object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/init(arccenter:radius:startangle:endangle:clockwise:))*