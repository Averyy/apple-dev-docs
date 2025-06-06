# PKCanvasViewDelegate

**Framework**: PencilKit  
**Kind**: protocol

Methods for monitoring drawing related changes in a canvas view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol PKCanvasViewDelegate : UIScrollViewDelegate
```

#### Overview

Implement the methods of the [`PKCanvasViewDelegate`](pkcanvasviewdelegate.md) protocol to monitor drawing events in a [`PKCanvasView`](pkcanvasview.md) object. Specifically, determine the start- and end-of-event sequences using the currently selected tool, and determine when those events affect the drawn content.

## Topics

### Responding to drawing-related changes
- [func canvasViewDrawingDidChange(PKCanvasView)](pkcanvasviewdelegate/canvasviewdrawingdidchange(_:).md)
  Tells the delegate that the contents of the current drawing changed.
- [func canvasViewDidFinishRendering(PKCanvasView)](pkcanvasviewdelegate/canvasviewdidfinishrendering(_:).md)
  Tells the delegate that the previously drawn content is ready to display.
### Responding to new event sequences
- [func canvasViewDidBeginUsingTool(PKCanvasView)](pkcanvasviewdelegate/canvasviewdidbeginusingtool(_:).md)
  Tells the delegate that the user started a new drawing sequence with the currently selected tool.
- [func canvasViewDidEndUsingTool(PKCanvasView)](pkcanvasviewdelegate/canvasviewdidendusingtool(_:).md)
  Tells the delegate that the user ended a drawing sequence with the tool they were using.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIScrollViewDelegate](../UIKit/UIScrollViewDelegate.md)

## See Also

- [var delegate: (any PKCanvasViewDelegate)?](pkcanvasview/delegate.md)
  The object you use to respond to changes in the drawn content or with the selected tool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkcanvasviewdelegate)*