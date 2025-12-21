# draw(at:)

**Framework**: Foundation  
**Kind**: method

Draws the attributed string starting at the specified point in the current graphics context.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func draw(at point: CGPoint)
```

#### Discussion

This method draws the entire string starting at the specified point. This method draws the line using the attributes specified in the attributed string itself. If newline characters are present in the string, those characters are honored and cause subsequent text to be placed on the next line underneath the starting point.

There must be either a focused view or an active graphics context when you call this method.

## Parameters

- `point`: The point in the current graphics context where you want to start drawing the string. The coordinate system of the graphics context is usually defined by the view in which you are drawing.

## See Also

- [func size() -> CGSize](nsattributedstring/size.md)
  Returns the size necessary to draw the string.
- [func lockFocus()](../AppKit/NSView/lockFocus.md)
  Locks the focus on the view, so subsequent commands take effect in the view’s window and coordinate system.
- [func draw(in: CGRect)](nsattributedstring/draw(in:).md)
  Draws the attributed string inside the specified bounding rectangle in the current graphics context.
- [func draw(with: CGRect, options: NSStringDrawingOptions, context: NSStringDrawingContext?)](nsattributedstring/draw(with:options:context:).md)
  Draws the attributed string in the specified bounding rectangle using the provided options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/draw(at:))*