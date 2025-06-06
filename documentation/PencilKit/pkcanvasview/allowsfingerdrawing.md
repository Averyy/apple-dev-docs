# allowsFingerDrawing

**Framework**: PencilKit  
**Kind**: property

A Boolean value that indicates whether the canvas accepts input from the user’s finger in addition to Apple Pencil.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsFingerDrawing: Bool { get set }
```

## See Also

- [var tool: any PKTool](pkcanvasview/tool-1kj57.md)
  The currently selected tool used for drawing.
- [var isRulerActive: Bool](pkcanvasview/isruleractive.md)
  A Boolean value that indicates whether a ruler view is visible on the canvas.
- [var drawingPolicy: PKCanvasViewDrawingPolicy](pkcanvasview/drawingpolicy.md)
  The policy that controls the types of touches allowed when drawing on the canvas.
- [enum PKCanvasViewDrawingPolicy](pkcanvasviewdrawingpolicy.md)
  Constants that you use to specify the type of drawing gestures your app permits while the user draws on the canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkcanvasview/allowsfingerdrawing)*