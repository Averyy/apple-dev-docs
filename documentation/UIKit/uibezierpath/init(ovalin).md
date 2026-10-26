# init(ovalIn:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a new Bézier path object with an inscribed oval path in the specified rectangle.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(ovalIn rect: CGRect)
```

```objc
+ (instancetype) bezierPathWithOvalInRect:(CGRect) rect;
```

#### Return Value

A new path object with the oval path.

#### Discussion

This method creates a closed subpath that approximates the oval using a sequence of Bézier curves. The path is created in a clockwise direction (relative to the default coordinate system). If the `rect` parameter specifies a square, the inscribed path is a circle.

## Parameters

- `rect`: The rectangle in which to inscribe an oval.

## See Also

### Creating a Bézier path
- [convenience init(rect: CGRect)](./init%28rect%29.md)
  Creates and returns a new Bézier path object with a rectangular path.
- [convenience init(roundedRect: CGRect, cornerRadius: CGFloat)](./init%28roundedrect,cornerradius%29.md)
  Creates and returns a new Bézier path object with a rounded rectangular path.
- [convenience init(roundedRect: CGRect, byRoundingCorners: UIRectCorner, cornerRadii: CGSize)](./init%28roundedrect,byroundingcorners,cornerradii%29.md)
  Creates and returns a new Bézier path object with a rectangular path rounded at the specified corners.
- [convenience init(arcCenter: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)](./init%28arccenter,radius,startangle,endangle,clockwise%29.md)
  Creates and returns a new Bézier path object with an arc of a circle.
- [convenience init(cgPath: CGPath)](./init%28cgpath%29-833n8.md)
  Creates and returns a new Bézier path object with the contents of a Core Graphics path.
- [func reversing() -> UIBezierPath](./reversing%28%29.md)
  Creates and returns a new Bézier path object with the reversed contents of the current path.
- [init()](./init%28%29.md)
  Creates and returns an empty path object.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a Bézier path object from data in an unarchiver.
- [+ bezierPath](./bezierpath.md)
  Creates and returns a new Bézier path object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/init(ovalin:))*