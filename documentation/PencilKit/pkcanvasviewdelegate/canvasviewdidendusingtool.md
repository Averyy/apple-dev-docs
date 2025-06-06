# canvasViewDidEndUsingTool(_:)

**Framework**: PencilKit  
**Kind**: method

Tells the delegate that the user ended a drawing sequence with the tool they were using.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func canvasViewDidEndUsingTool(_ canvasView: PKCanvasView)
```

## Parameters

- `canvasView`: The canvas view whose contents changed.

## See Also

- [func canvasViewDidBeginUsingTool(PKCanvasView)](pkcanvasviewdelegate/canvasviewdidbeginusingtool(_:).md)
  Tells the delegate that the user started a new drawing sequence with the currently selected tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkcanvasviewdelegate/canvasviewdidendusingtool(_:))*