# PKEraserToolReference

**Framework**: PencilKit  
**Kind**: class

A tool for erasing previously drawn content in a canvas view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class PKEraserToolReference
```

#### Overview

A [`PKEraserTool`](pkerasertool-swift.struct.md) object supports the deletion of content from a [`PKCanvasView`](pkcanvasview.md) object. The eraser tool’s type determines whether the canvas removes entire items or just the portion of an item that it touches.

Create an eraser tool programmatically or display a [`PKToolPicker`](pktoolpicker.md) object and let the user select the eraser. Assign the resulting object to the [`tool`](pkcanvasview/tool-6str6.md) property of your [`PKCanvasView`](pkcanvasview.md) object. The canvas uses any subsequent touch sequences to erase content on the canvas.

## Topics

### Creating an eraser tool
- [init(eraserType: __PKEraserType)](pkerasertoolreference/init(erasertype:).md)
  Creates an eraser tool object that removes objects wholly or partially from a canvas view.
- [init(eraserType: __PKEraserType, width: CGFloat)](pkerasertoolreference/init(erasertype:width:).md)
### Getting the eraser type
- [var eraserType: __PKEraserType](pkerasertoolreference/erasertype.md)
  The behavior adopted by the eraser when deleting content.
### Getting the width information
- [var width: CGFloat](pkerasertoolreference/width.md)
  The width of the eraser.
- [class func defaultWidth(for: __PKEraserType) -> CGFloat](pkerasertoolreference/defaultwidth(for:).md)
  The default width for the specified eraser type.
- [class func minimumWidth(for: __PKEraserType) -> CGFloat](pkerasertoolreference/minimumwidth(for:).md)
  The minimum width for the specified eraser type.
- [class func maximumWidth(for: __PKEraserType) -> CGFloat](pkerasertoolreference/maximumwidth(for:).md)
  The maximum width for the specified eraser type.

## Relationships

### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkerasertoolreference)*