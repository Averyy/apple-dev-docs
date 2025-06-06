# tool

**Framework**: PencilKit  
**Kind**: property

The currently selected tool used for drawing.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency var tool: any PKTool { get set }
```

## See Also

- [var isRulerActive: Bool](pkcanvasview/isruleractive.md)
  A Boolean value that indicates whether a ruler view is visible on the canvas.
- [var allowsFingerDrawing: Bool](pkcanvasview/allowsfingerdrawing.md)
  A Boolean value that indicates whether the canvas accepts input from the user’s finger in addition to Apple Pencil.
- [var drawingPolicy: PKCanvasViewDrawingPolicy](pkcanvasview/drawingpolicy.md)
  The policy that controls the types of touches allowed when drawing on the canvas.
- [enum PKCanvasViewDrawingPolicy](pkcanvasviewdrawingpolicy.md)
  Constants that you use to specify the type of drawing gestures your app permits while the user draws on the canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkcanvasview/tool-1kj57)*