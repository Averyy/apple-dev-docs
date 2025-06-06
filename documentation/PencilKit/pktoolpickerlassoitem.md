# PKToolPickerLassoItem

**Framework**: PencilKit  
**Kind**: class

An item that represents a lasso tool in the tool picker.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
class PKToolPickerLassoItem
```

#### Overview

A lasso item represents a [`PKLassoTool`](pklassotool-swift.struct.md) — a tool for selecting stroked lines and shapes in a canvas view — in a [`PKToolPicker`](pktoolpicker.md).

## Topics

### Creating a lasso item
- [init()](pktoolpickerlassoitem/init.md)
  Creates a new lasso item.
### Accessing the lasso tool
- [var lassoTool: PKLassoTool](pktoolpickerlassoitem/lassotool-2xuhy.md)
  A lasso tool for selecting parts of a drawing.

## Relationships

### Inherits From
- [PKToolPickerItem](pktoolpickeritem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [init()](pktoolpicker/init.md)
  Creates a new tool picker with a default set of tools.
- [init(toolItems: [PKToolPickerItem])](pktoolpicker/init(toolitems:).md)
  Creates a new tool picker with the tools you specify.
- [class PKToolPickerInkingItem](pktoolpickerinkingitem.md)
  An item that represents an inking tool in the tool picker.
- [class PKToolPickerEraserItem](pktoolpickereraseritem.md)
  An item that represents an eraser tool in the tool picker.
- [class PKToolPickerRulerItem](pktoolpickerruleritem.md)
  An item that represents a ruler tool in the tool picker.
- [class PKToolPickerScribbleItem](pktoolpickerscribbleitem.md)
  An item that represents a Scribble tool in the tool picker.
- [class PKToolPickerCustomItem](pktoolpickercustomitem.md)
  An item that represents a custom tool in the tool picker.
- [class PKToolPickerItem](pktoolpickeritem.md)
  The base class for an item in the tool picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpickerlassoitem)*