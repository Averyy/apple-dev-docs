# init(roundedRect:xRadius:yRadius:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a new Bézier path object initialized with a rounded rectangular path.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init(roundedRect rect: NSRect, xRadius: CGFloat, yRadius: CGFloat)
```

```objc
+ (NSBezierPath *) bezierPathWithRoundedRect:(NSRect) rect xRadius:(CGFloat) xRadius yRadius:(CGFloat) yRadius;
```

#### Return Value

A new path object with the rounded rectangular path.

#### Discussion

The path is constructed in a counter-clockwise direction, starting at the top-left corner of the rectangle. If either one of the radius parameters contains the value `0.0`, the returned path is a plain rectangle without rounded corners.

## Parameters

- `rect`: The rectangle that defines the basic shape of the path.
- `xRadius`: The radius of each corner oval along the x-axis. Values larger than half the rectangle’s width are clamped to half the width.
- `yRadius`: The radius of each corner oval along the y-axis. Values larger than half the rectangle’s height are clamped to half the height.

## See Also

### Related Documentation
- [func appendRoundedRect(NSRect, xRadius: CGFloat, yRadius: CGFloat)](./appendroundedrect%28_,xradius,yradius%29.md)
  Appends a rounded rectangular path to the path.
- [+ bezierPath](./bezierpath.md)
  Creates and returns a new Bézier path object.
### Creating a Bézier Path
- [init(ovalIn: NSRect)](./init%28ovalin%29.md)
  Creates and returns a new Bézier path object initialized with an oval path inscribed in the specified rectangle.
- [init(rect: NSRect)](./init%28rect%29.md)
  Creates and returns a new Bézier path object initialized with a rectangular path.
- [init(cgPath: CGPath)](./init%28cgpath%29-96cxk.md)
- [var flattened: NSBezierPath](./flattened.md)
  A flattened version of the path object.
- [var reversed: NSBezierPath](./reversed.md)
  A path containing the reversed contents of the current path object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/init(roundedrect:xradius:yradius:))*