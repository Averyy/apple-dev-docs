# PKToolPickerItem

**Framework**: PencilKit  
**Kind**: class

The base class for an item in the tool picker.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- visionOS 2.0+

## Declaration

```swift
class PKToolPickerItem
```

## Topics

### Identifying the item
- [var identifier: String](pktoolpickeritem/identifier.md)
  A string that identifies the item in the tool picker.
### Instance Properties
- [var tool: (any PKTool)?](pktoolpickeritem/tool-2ji9h.md)
  A tool for drawing on a PKCanvasView.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [PKToolPickerCustomItem](pktoolpickercustomitem.md)
- [PKToolPickerEraserItem](pktoolpickereraseritem.md)
- [PKToolPickerInkingItem](pktoolpickerinkingitem.md)
- [PKToolPickerLassoItem](pktoolpickerlassoitem.md)
- [PKToolPickerRulerItem](pktoolpickerruleritem.md)
- [PKToolPickerScribbleItem](pktoolpickerscribbleitem.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [init()](pktoolpicker/init.md)
  Creates a new tool picker with a default set of tools.
- [init(toolItems: [PKToolPickerItem])](pktoolpicker/init(toolitems:).md)
  Creates a new tool picker with the tools you specify.
- [class PKToolPickerInkingItem](pktoolpickerinkingitem.md)
  An item that represents an inking tool in the tool picker.
- [class PKToolPickerEraserItem](pktoolpickereraseritem.md)
  An item that represents an eraser tool in the tool picker.
- [class PKToolPickerLassoItem](pktoolpickerlassoitem.md)
  An item that represents a lasso tool in the tool picker.
- [class PKToolPickerRulerItem](pktoolpickerruleritem.md)
  An item that represents a ruler tool in the tool picker.
- [class PKToolPickerScribbleItem](pktoolpickerscribbleitem.md)
  An item that represents a Scribble tool in the tool picker.
- [class PKToolPickerCustomItem](pktoolpickercustomitem.md)
  An item that represents a custom tool in the tool picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpickeritem)*