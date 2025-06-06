# canvasViewDidFinishRendering(_:)

**Framework**: PencilKit  
**Kind**: method

Tells the delegate that the previously drawn content is ready to display.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func canvasViewDidFinishRendering(_ canvasView: PKCanvasView)
```

#### Discussion

The [`PKCanvasView`](pkcanvasview.md) object calls this method when you assign a new drawing to its [`drawing`](pkcanvasview/drawing.md) property, when the user zooms in on the canvas, or when the canvas scrolls.

## Parameters

- `canvasView`: The canvas view whose contents changed.

## See Also

- [func canvasViewDrawingDidChange(PKCanvasView)](pkcanvasviewdelegate/canvasviewdrawingdidchange(_:).md)
  Tells the delegate that the contents of the current drawing changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkcanvasviewdelegate/canvasviewdidfinishrendering(_:))*