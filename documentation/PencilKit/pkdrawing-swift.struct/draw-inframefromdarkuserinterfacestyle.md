# draw(in:frame:from:darkUserInterfaceStyle:)

**Framework**: PencilKit  
**Kind**: method

Draws the drawing in the specified rectangle.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
(nonsending) func draw(in cgContext: CGContext, frame: CGRect, from sourceRect: CGRect, darkUserInterfaceStyle: Bool = false) async
```

## Parameters

- `frame`: The rectangle (in the coordinate system of the graphics context) in which   to draw the drawing.
- `sourceRect`: The rectangle (in the drawing coordinate system) from which to draw.
- `darkUserInterfaceStyle`: Use a dark user interface style for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawing-swift.struct/draw(in:frame:from:darkuserinterfacestyle:))*