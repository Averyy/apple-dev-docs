# canvasViewDrawingDidChange(_:)

**Framework**: PencilKit  
**Kind**: method

Tells the delegate that the contents of the current drawing changed.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func canvasViewDrawingDidChange(_ canvasView: PKCanvasView)
```

## Parameters

- `canvasView`: The canvas view whose contents changed.

## See Also

- [func canvasViewDidFinishRendering(PKCanvasView)](pkcanvasviewdelegate/canvasviewdidfinishrendering(_:).md)
  Tells the delegate that the previously drawn content is ready to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkcanvasviewdelegate/canvasviewdrawingdidchange(_:))*