# init(roundedRect:byRoundingCorners:cornerRadii:)

**Framework**: UIKit  
**Kind**: init

Creates and returns a new Bézier path object with a rectangular path rounded at the specified corners.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(roundedRect rect: CGRect, byRoundingCorners corners: UIRectCorner, cornerRadii: CGSize)
```

#### Return Value

A new path object with the rounded rectangular path.

#### Discussion

This method creates a closed subpath, proceeding in a clockwise direction (relative to the default coordinate system) as it creates the necessary line and curve segments.

## Parameters

- `rect`: The rectangle that defines the basic shape of the path.
- `corners`: A bitmask value that identifies the corners that you want rounded. You can use this parameter to round only a subset of the corners of the rectangle.
- `cornerRadii`: The radius of each corner oval. Values larger than half the rectangle’s width or height are clamped appropriately to half the width or height.

## See Also

- [convenience init(rect: CGRect)](uibezierpath/init(rect:).md)
  Creates and returns a new Bézier path object with a rectangular path.
- [convenience init(ovalIn: CGRect)](uibezierpath/init(ovalin:).md)
  Creates and returns a new Bézier path object with an inscribed oval path in the specified rectangle.
- [convenience init(roundedRect: CGRect, cornerRadius: CGFloat)](uibezierpath/init(roundedrect:cornerradius:).md)
  Creates and returns a new Bézier path object with a rounded rectangular path.
- [convenience init(arcCenter: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)](uibezierpath/init(arccenter:radius:startangle:endangle:clockwise:).md)
  Creates and returns a new Bézier path object with an arc of a circle.
- [convenience init(cgPath: CGPath)](uibezierpath/init(cgpath:).md)
  Creates and returns a new Bézier path object with the contents of a Core Graphics path.
- [func reversing() -> UIBezierPath](uibezierpath/reversing.md)
  Creates and returns a new Bézier path object with the reversed contents of the current path.
- [init()](uibezierpath/init.md)
  Creates and returns an empty path object.
- [init?(coder: NSCoder)](uibezierpath/init(coder:).md)
  Creates a Bézier path object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/init(roundedrect:byroundingcorners:cornerradii:))*