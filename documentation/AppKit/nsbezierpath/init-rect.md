# init(rect:)

**Framework**: AppKit  
**Kind**: init

Creates and returns a new Bézier path object initialized with a rectangular path.

**Availability**:
- macOS ?+

## Declaration

```swift
init(rect: NSRect)
```

#### Return Value

A new path object with the rectangular path.

#### Discussion

The path is constructed by starting at the origin of `aRect` and adding line segments in a counterclockwise direction.

## Parameters

- `rect`: The rectangle describing the path to create.

## See Also

- [class func fill(NSRect)](nsbezierpath/fill(_:).md)
  Fills the specified rectangular path with the current fill color.
- [class func stroke(NSRect)](nsbezierpath/stroke(_:).md)
  Strokes the path of the specified rectangle using the current stroke color and the default drawing attributes.
- [func appendRect(NSRect)](nsbezierpath/appendrect(_:).md)
  Appends a rectangular path to the path.
- [init(ovalIn: NSRect)](nsbezierpath/init(ovalin:).md)
  Creates and returns a new Bézier path object initialized with an oval path inscribed in the specified rectangle.
- [init(roundedRect: NSRect, xRadius: CGFloat, yRadius: CGFloat)](nsbezierpath/init(roundedrect:xradius:yradius:).md)
  Creates and returns a new Bézier path object initialized with a rounded rectangular path.
- [init(cgPath: CGPath)](nsbezierpath/init(cgpath:).md)
- [var flattened: NSBezierPath](nsbezierpath/flattened.md)
  A flattened version of the path object.
- [var reversed: NSBezierPath](nsbezierpath/reversed.md)
  A path containing the reversed contents of the current path object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/init(rect:))*