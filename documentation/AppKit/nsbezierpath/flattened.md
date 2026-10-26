# flattened

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A flattened version of the path object.

**Availability**:
- macOS

## Declaration

```swift
@NSCopying
var flattened: NSBezierPath { get }
```

```objc
@property (copy, readonly) NSBezierPath * bezierPathByFlatteningPath;
```

#### Discussion

Flattening a path converts all curved line segments into straight line approximations. The granularity of the approximations is controlled by the path’s current flatness value, which is set using [`defaultFlatness`](./defaultflatness.md).

## See Also

### Creating a Bézier Path
- [init(ovalIn: NSRect)](./init%28ovalin%29.md)
  Creates and returns a new Bézier path object initialized with an oval path inscribed in the specified rectangle.
- [init(rect: NSRect)](./init%28rect%29.md)
  Creates and returns a new Bézier path object initialized with a rectangular path.
- [init(roundedRect: NSRect, xRadius: CGFloat, yRadius: CGFloat)](./init%28roundedrect,xradius,yradius%29.md)
  Creates and returns a new Bézier path object initialized with a rounded rectangular path.
- [init(cgPath: CGPath)](./init%28cgpath%29-96cxk.md)
- [var reversed: NSBezierPath](./reversed.md)
  A path containing the reversed contents of the current path object.
- [+ bezierPath](./bezierpath.md)
  Creates and returns a new Bézier path object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/flattened)*