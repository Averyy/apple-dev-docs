# init(cgPath:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a new Bézier path object with the contents of a Core Graphics path.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(cgPath CGPath: CGPath)
```

```objc
+ (instancetype) bezierPathWithCGPath:(CGPathRef) CGPath;
```

#### Return Value

A new path object with the specified path information.

## Parameters

- `CGPath`: The Core Graphics path from which to obtain the initial path information. If this parameter is `nil`, the method raises an exception.

## See Also

### Creating a Bézier path
- [convenience init(rect: CGRect)](./init%28rect%29.md)
  Creates and returns a new Bézier path object with a rectangular path.
- [convenience init(ovalIn: CGRect)](./init%28ovalin%29.md)
  Creates and returns a new Bézier path object with an inscribed oval path in the specified rectangle.
- [convenience init(roundedRect: CGRect, cornerRadius: CGFloat)](./init%28roundedrect,cornerradius%29.md)
  Creates and returns a new Bézier path object with a rounded rectangular path.
- [convenience init(roundedRect: CGRect, byRoundingCorners: UIRectCorner, cornerRadii: CGSize)](./init%28roundedrect,byroundingcorners,cornerradii%29.md)
  Creates and returns a new Bézier path object with a rectangular path rounded at the specified corners.
- [convenience init(arcCenter: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)](./init%28arccenter,radius,startangle,endangle,clockwise%29.md)
  Creates and returns a new Bézier path object with an arc of a circle.
- [func reversing() -> UIBezierPath](./reversing%28%29.md)
  Creates and returns a new Bézier path object with the reversed contents of the current path.
- [init()](./init%28%29.md)
  Creates and returns an empty path object.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a Bézier path object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/init(cgpath:)-833n8)*