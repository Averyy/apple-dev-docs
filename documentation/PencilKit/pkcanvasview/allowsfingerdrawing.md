# allowsFingerDrawing

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the canvas accepts input from the user’s finger in addition to Apple Pencil.

**Availability**:
- iOS 13.0+ - Deprecated in 14.0
- iPadOS 13.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`drawingPolicy`](./drawingpolicy.md) instead.

## Declaration

```swift
var allowsFingerDrawing: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsFingerDrawing;
```

## See Also

### Configuring the drawing environment
- [var tool: any PKTool](./tool-1kj57.md)
  The currently selected tool used for drawing.
- [var isRulerActive: Bool](./isruleractive.md)
  A Boolean value that indicates whether a ruler view is visible on the canvas.
- [var drawingPolicy: PKCanvasViewDrawingPolicy](./drawingpolicy.md)
  The policy that controls the types of touches allowed when drawing on the canvas.
- [enum PKCanvasViewDrawingPolicy](../pkcanvasviewdrawingpolicy.md)
  Constants that you use to specify the type of drawing gestures your app permits while the user draws on the canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkcanvasview/allowsfingerdrawing)*