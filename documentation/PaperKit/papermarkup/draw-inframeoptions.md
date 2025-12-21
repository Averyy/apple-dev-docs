# draw(in:frame:options:)

**Framework**: PaperKit  
**Kind**: method

Draws the entire paper contents in the specified rectangle.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
(nonsending) func draw(in context: CGContext, frame: CGRect, options: RenderingOptions = RenderingOptions()) async
```

#### Discussion

To draw a cropped portion of a paper data model, modify the `bounds` of the paper being drawn.

## Parameters

- `context`: The graphics context to render into.
- `frame`: The rectangle (in the coordinate system of the graphics context) in which   to draw the paper.
- `options`: The rendering options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkup/draw(in:frame:options:))*