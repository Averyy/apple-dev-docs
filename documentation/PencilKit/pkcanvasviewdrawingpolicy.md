# PKCanvasViewDrawingPolicy

**Framework**: PencilKit  
**Kind**: enum

Constants that you use to specify the type of drawing gestures your app permits while the user draws on the canvas.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
enum PKCanvasViewDrawingPolicy
```

## Topics

### Drawing policies
- [PKCanvasViewDrawingPolicy.default](pkcanvasviewdrawingpolicy/default.md)
  The default input type to use for drawing on a canvas.
- [PKCanvasViewDrawingPolicy.anyInput](pkcanvasviewdrawingpolicy/anyinput.md)
  Allows drawing on the canvas from any input source.
- [PKCanvasViewDrawingPolicy.pencilOnly](pkcanvasviewdrawingpolicy/pencilonly.md)
  Pencil touches are the only input that draw on the canvas.
### Initializers
- [init?(rawValue: UInt)](pkcanvasviewdrawingpolicy/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var tool: any PKTool](pkcanvasview/tool-1kj57.md)
  The currently selected tool used for drawing.
- [var isRulerActive: Bool](pkcanvasview/isruleractive.md)
  A Boolean value that indicates whether a ruler view is visible on the canvas.
- [var allowsFingerDrawing: Bool](pkcanvasview/allowsfingerdrawing.md)
  A Boolean value that indicates whether the canvas accepts input from the user’s finger in addition to Apple Pencil.
- [var drawingPolicy: PKCanvasViewDrawingPolicy](pkcanvasview/drawingpolicy.md)
  The policy that controls the types of touches allowed when drawing on the canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkcanvasviewdrawingpolicy)*