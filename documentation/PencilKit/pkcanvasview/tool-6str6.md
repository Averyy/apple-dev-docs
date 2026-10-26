# tool

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

The currently selected tool used for drawing.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, copy) PKTool * tool;
```

## See Also

### Configuring the drawing environment
- [var isRulerActive: Bool](./isruleractive.md)
  A Boolean value that indicates whether a ruler view is visible on the canvas.
- [var allowsFingerDrawing: Bool](./allowsfingerdrawing.md)
  A Boolean value that indicates whether the canvas accepts input from the user’s finger in addition to Apple Pencil.
- [var drawingPolicy: PKCanvasViewDrawingPolicy](./drawingpolicy.md)
  The policy that controls the types of touches allowed when drawing on the canvas.
- [enum PKCanvasViewDrawingPolicy](../pkcanvasviewdrawingpolicy.md)
  Constants that you use to specify the type of drawing gestures your app permits while the user draws on the canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkcanvasview/tool-6str6)*