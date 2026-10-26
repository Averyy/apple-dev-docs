# init(cgPath:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- macOS 14.0+

## Declaration

```swift
init(cgPath: CGPath)
```

```objc
+ (NSBezierPath *) bezierPathWithCGPath:(CGPathRef) cgPath;
```

## See Also

### Creating a Bézier Path
- [init(ovalIn: NSRect)](./init%28ovalin%29.md)
  Creates and returns a new Bézier path object initialized with an oval path inscribed in the specified rectangle.
- [init(rect: NSRect)](./init%28rect%29.md)
  Creates and returns a new Bézier path object initialized with a rectangular path.
- [init(roundedRect: NSRect, xRadius: CGFloat, yRadius: CGFloat)](./init%28roundedrect,xradius,yradius%29.md)
  Creates and returns a new Bézier path object initialized with a rounded rectangular path.
- [var flattened: NSBezierPath](./flattened.md)
  A flattened version of the path object.
- [var reversed: NSBezierPath](./reversed.md)
  A path containing the reversed contents of the current path object.
- [+ bezierPath](./bezierpath.md)
  Creates and returns a new Bézier path object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/init(cgpath:)-96cxk)*