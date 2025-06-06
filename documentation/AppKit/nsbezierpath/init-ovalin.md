# init(ovalIn:)

**Framework**: AppKit  
**Kind**: init

Creates and returns a new Bézier path object initialized with an oval path inscribed in the specified rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
init(ovalIn rect: NSRect)
```

#### Return Value

An `NSBezierPath` new path object with the oval path.

#### Discussion

If the `aRect` parameter specifies a square, the inscribed path is a circle. The path is constructed by starting in the lower-right quadrant of the rectangle and adding arc segments counterclockwise to complete the oval.

## Parameters

- `rect`: The rectangle in which to inscribe an oval.

## See Also

- [func appendOval(in: NSRect)](nsbezierpath/appendoval(in:).md)
  Appends an oval path to the path, inscribing the oval in the specified rectangle.
- [init(rect: NSRect)](nsbezierpath/init(rect:).md)
  Creates and returns a new Bézier path object initialized with a rectangular path.
- [init(roundedRect: NSRect, xRadius: CGFloat, yRadius: CGFloat)](nsbezierpath/init(roundedrect:xradius:yradius:).md)
  Creates and returns a new Bézier path object initialized with a rounded rectangular path.
- [init(cgPath: CGPath)](nsbezierpath/init(cgpath:).md)
- [var flattened: NSBezierPath](nsbezierpath/flattened.md)
  A flattened version of the path object.
- [var reversed: NSBezierPath](nsbezierpath/reversed.md)
  A path containing the reversed contents of the current path object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/init(ovalin:))*