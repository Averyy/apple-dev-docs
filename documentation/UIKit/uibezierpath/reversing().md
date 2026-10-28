# reversing()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Creates and returns a new Bézier path object with the reversed contents of the current path.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func reversing() -> UIBezierPath
```

```objc
- (UIBezierPath *) bezierPathByReversingPath;
```

## Return Value

A new path object with the same path shape but for which the path has been created in the reverse direction.

## Discussion

Reversing a path does not necessarily change the appearance of the path when rendered. Instead, it changes the direction in which path segments are drawn. For example, reversing the path of a rectangle (whose line segments are normally drawn starting at the origin and proceeding in a counterclockwise direction) causes its line segments to be drawn in a clockwise direction instead. Drawing a reversed path could affect the appearance of a filled pattern, depending on the pattern and the fill rule in use.

This method reverses each whole or partial subpath in the path object individually.

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
- [convenience init(cgPath: CGPath)](./init%28cgpath%29-833n8.md)
  Creates and returns a new Bézier path object with the contents of a Core Graphics path.
- [init()](./init%28%29.md)
  Creates and returns an empty path object.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a Bézier path object from data in an unarchiver.
- [+ bezierPath](./bezierpath.md)
  Creates and returns a new Bézier path object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/reversing())*