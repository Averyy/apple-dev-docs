# reversed

**Framework**: AppKit  
**Kind**: property

A path containing the reversed contents of the current path object.

**Availability**:
- macOS ?+

## Declaration

```swift
@NSCopying
var reversed: NSBezierPath { get }
```

#### Discussion

The reversed path does not necessarily have a different appearance when rendered. Instead, it changes the direction in which path segments are drawn. For example, reversing the path of a rectangle (whose line segments are normally drawn starting at the origin and proceeding in a counterclockwise direction) causes its line segments to be drawn in a clockwise direction instead. Drawing a reversed path could affect the appearance of a filled pattern, depending on the pattern and the fill rule in use.

The path in this property is created by reversing each whole or partial subpath in the path object individually.

## See Also

- [init(ovalIn: NSRect)](nsbezierpath/init(ovalin:).md)
  Creates and returns a new Bézier path object initialized with an oval path inscribed in the specified rectangle.
- [init(rect: NSRect)](nsbezierpath/init(rect:).md)
  Creates and returns a new Bézier path object initialized with a rectangular path.
- [init(roundedRect: NSRect, xRadius: CGFloat, yRadius: CGFloat)](nsbezierpath/init(roundedrect:xradius:yradius:).md)
  Creates and returns a new Bézier path object initialized with a rounded rectangular path.
- [init(cgPath: CGPath)](nsbezierpath/init(cgpath:).md)
- [var flattened: NSBezierPath](nsbezierpath/flattened.md)
  A flattened version of the path object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/reversed)*