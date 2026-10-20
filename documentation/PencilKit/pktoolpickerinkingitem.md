# PKToolPickerInkingItem

**Framework**: PencilKit  
**Kind**: class  
**Role**: Class

An item that represents an inking tool in the tool picker.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 26.0+
- visionOS 2.0+

## Declaration

```swift
class PKToolPickerInkingItem
```

```objc
@interface PKToolPickerInkingItem : PKToolPickerItem
```

#### Overview

An inking item represents a [`PKInkingTool`](./pkinkingtool-swift.struct.md) — a tool for drawing marks in a canvas view — in a [`PKToolPicker`](./pktoolpicker.md).

## Topics

### Accessing the inking tool
- [var inkingTool: PKInkingTool](./pktoolpickerinkingitem/inkingtool-1hcet.md)
  A tool for drawing on a canvas view.
### Initializers
- [convenience init(type: PKInkingTool.InkType, color: UIColor?, width: CGFloat?, azimuth: CGFloat?, identifier: String?)](./pktoolpickerinkingitem/init%28type,color,width,azimuth,identifier%29-7gkxh.md)
  Create a new inking tool item.
- [convenience init(type: PKInkingTool.InkType, color: NSColor?, width: CGFloat?, azimuth: CGFloat?, identifier: String?)](./pktoolpickerinkingitem/init%28type,color,width,azimuth,identifier%29-y8h5.md)
  Create a new inking tool item.
- [convenience init(type: PKInkingTool.InkType, color: NSColor?, width: CGFloat?, identifier: String?)](./pktoolpickerinkingitem/init%28type,color,width,identifier%29-1tsup.md)
  Create a new inking tool item.
- [convenience init(type: PKInkingTool.InkType, color: UIColor?, width: CGFloat?, identifier: String?)](./pktoolpickerinkingitem/init%28type,color,width,identifier%29-7kzdq.md)
  Create a new inking tool item.
### Instance Properties
- [var allowsColorSelection: Bool](./pktoolpickerinkingitem/allowscolorselection.md)
  Present color selection UI to the user. Default value is YES.

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
- [class PKToolPickerEraserItem](./pktoolpickereraseritem.md)
  An item that represents an eraser tool in the tool picker.
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

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpickerinkingitem)*