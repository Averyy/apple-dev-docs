# PKToolPickerEraserItem

**Framework**: PencilKit  
**Kind**: class  
**Role**: Class

An item that represents an eraser tool in the tool picker.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- visionOS 2.0+

## Declaration

```swift
class PKToolPickerEraserItem
```

```objc
@interface PKToolPickerEraserItem : PKToolPickerItem
```

#### Overview

An eraser item represents a [`PKEraserTool`](./pkerasertool-swift.struct.md) — a tool for erasing content in a canvas view — in a [`PKToolPicker`](./pktoolpicker.md).

## Topics

### Creating an eraser item
- [convenience init(type: PKEraserTool.EraserType)](./pktoolpickereraseritem/init%28type%29.md)
  Creates a new eraser item.
- [convenience init(type: PKEraserTool.EraserType, width: CGFloat)](./pktoolpickereraseritem/init%28type,width%29.md)
  Creates a new eraser item with the specified width.
- [- initWithEraserType:](./pktoolpickereraseritem/initwitherasertype_.md)
  Creates a new eraser item.
- [- initWithEraserType:width:](./pktoolpickereraseritem/initwitherasertype_width_.md)
  Creates a new eraser item with the specified width.
### Accessing the eraser tool
- [var eraserTool: PKEraserTool](./pktoolpickereraseritem/erasertool-92wqj.md)
  An eraser tool for erasing parts of a drawing.
- [eraserTool](./pktoolpickereraseritem/erasertool-4q3hp.md)
  An eraser tool for erasing parts of a drawing.

## Relationships

### Inherits From
- [PKToolPickerItem](./pktoolpickeritem.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating a tool picker
- [init()](./pktoolpicker/init%28%29.md)
  Creates a new tool picker with a default set of tools.
- [init(toolItems: [PKToolPickerItem])](./pktoolpicker/init%28toolitems%29.md)
  Creates a new tool picker with the tools you specify.
- [class PKToolPickerInkingItem](./pktoolpickerinkingitem.md)
  An item that represents an inking tool in the tool picker.
- [class PKToolPickerLassoItem](./pktoolpickerlassoitem.md)
  An item that represents a lasso tool in the tool picker.
- [class PKToolPickerRulerItem](./pktoolpickerruleritem.md)
  An item that represents a ruler tool in the tool picker.
- [class PKToolPickerScribbleItem](./pktoolpickerscribbleitem.md)
  An item that represents a Scribble tool in the tool picker.
- [class PKToolPickerCustomItem](./pktoolpickercustomitem.md)
  An item that represents a custom tool in the tool picker.
- [class PKToolPickerItem](./pktoolpickeritem.md)
  The base class for an item in the tool picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpickereraseritem)*