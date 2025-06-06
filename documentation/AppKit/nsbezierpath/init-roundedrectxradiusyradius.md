# init(roundedRect:xRadius:yRadius:)

**Framework**: AppKit  
**Kind**: init

Creates and returns a new Bézier path object initialized with a rounded rectangular path.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init(roundedRect rect: NSRect, xRadius: CGFloat, yRadius: CGFloat)
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

- [func appendRoundedRect(NSRect, xRadius: CGFloat, yRadius: CGFloat)](nsbezierpath/appendroundedrect(_:xradius:yradius:).md)
  Appends a rounded rectangular path to the path.
- [init(ovalIn: NSRect)](nsbezierpath/init(ovalin:).md)
  Creates and returns a new Bézier path object initialized with an oval path inscribed in the specified rectangle.
- [init(rect: NSRect)](nsbezierpath/init(rect:).md)
  Creates and returns a new Bézier path object initialized with a rectangular path.
- [init(cgPath: CGPath)](nsbezierpath/init(cgpath:).md)
- [var flattened: NSBezierPath](nsbezierpath/flattened.md)
  A flattened version of the path object.
- [var reversed: NSBezierPath](nsbezierpath/reversed.md)
  A path containing the reversed contents of the current path object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbezierpath/init(roundedrect:xradius:yradius:))*