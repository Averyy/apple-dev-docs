# flattened

**Framework**: AppKit  
**Kind**: property

A flattened version of the path object.

**Availability**:
- macOS ?+

## Declaration

```swift
@NSCopying
var flattened: NSBezierPath { get }
```

#### Discussion

Flattening a path converts all curved line segments into straight line approximations. The granularity of the approximations is controlled by the path’s current flatness value, which is set using [`defaultFlatness`](nsbezierpath/defaultflatness.md).

## See Also

- [init(ovalIn: NSRect)](nsbezierpath/init(ovalin:).md)
  Creates and returns a new Bézier path object initialized with an oval path inscribed in the specified rectangle.
- [init(rect: NSRect)](nsbezierpath/init(rect:).md)
  Creates and returns a new Bézier path object initialized with a rectangular path.
- [init(roundedRect: NSRect, xRadius: CGFloat, yRadius: CGFloat)](nsbezierpath/init(roundedrect:xradius:yradius:).md)
  Creates and returns a new Bézier path object initialized with a rounded rectangular path.
- [init(cgPath: CGPath)](nsbezierpath/init(cgpath:).md)
- [var reversed: NSBezierPath](nsbezierpath/reversed.md)
  A path containing the reversed contents of the current path object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/flattened)*