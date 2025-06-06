# init(ovalIn:)

**Framework**: UIKit  
**Kind**: init

Creates and returns a new Bézier path object with an inscribed oval path in the specified rectangle.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(ovalIn rect: CGRect)
```

#### Return Value

A new path object with the oval path.

#### Discussion

This method creates a closed subpath that approximates the oval using a sequence of Bézier curves. The path is created in a clockwise direction (relative to the default coordinate system). If the `rect` parameter specifies a square, the inscribed path is a circle.

## Parameters

- `rect`: The rectangle in which to inscribe an oval.

## See Also

- [convenience init(rect: CGRect)](uibezierpath/init(rect:).md)
  Creates and returns a new Bézier path object with a rectangular path.
- [convenience init(roundedRect: CGRect, cornerRadius: CGFloat)](uibezierpath/init(roundedrect:cornerradius:).md)
  Creates and returns a new Bézier path object with a rounded rectangular path.
- [convenience init(roundedRect: CGRect, byRoundingCorners: UIRectCorner, cornerRadii: CGSize)](uibezierpath/init(roundedrect:byroundingcorners:cornerradii:).md)
  Creates and returns a new Bézier path object with a rectangular path rounded at the specified corners.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/init(ovalin:))*