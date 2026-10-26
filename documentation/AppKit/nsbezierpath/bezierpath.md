# bezierPath

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates and returns a new Bézier path object.

**Availability**:
- macOS

## Declaration

```objc
+ (NSBezierPath *) bezierPath;
```

#### Return Value

A new empty path object.

## See Also

### Creating a Bézier Path
- [init(ovalIn: NSRect)](./init%28ovalin%29.md)
  Creates and returns a new Bézier path object initialized with an oval path inscribed in the specified rectangle.
- [init(rect: NSRect)](./init%28rect%29.md)
  Creates and returns a new Bézier path object initialized with a rectangular path.
- [init(roundedRect: NSRect, xRadius: CGFloat, yRadius: CGFloat)](./init%28roundedrect,xradius,yradius%29.md)
  Creates and returns a new Bézier path object initialized with a rounded rectangular path.
- [init(cgPath: CGPath)](./init%28cgpath%29-96cxk.md)
- [var flattened: NSBezierPath](./flattened.md)
  A flattened version of the path object.
- [var reversed: NSBezierPath](./reversed.md)
  A path containing the reversed contents of the current path object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/bezierpath)*