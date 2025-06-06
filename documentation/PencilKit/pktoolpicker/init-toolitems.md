# init(toolItems:)

**Framework**: PencilKit  
**Kind**: init

Creates a new tool picker with the tools you specify.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
init(toolItems items: [PKToolPickerItem])
```

#### Discussion

Use this initializer to create a tool picker with the tools you specify, which the picker displays in the custom order you provide during initialization. You can add system tools, such as the eraser and ruler, and custom tools in the same picker.

The following code shows how to create a tool picker with several system tools. For an example of creating a custom tool, see [`PKToolPickerCustomItem`](pktoolpickercustomitem.md).

```swift
// Create system items for the Scribble tool, ruler, and eraser.
let scribbleItem = PKToolPickerScribbleItem()
let rulerItem = PKToolPickerRulerItem()
let eraserItem = PKToolPickerEraserItem(type: .fixedWidthBitmap, width: 10.0)

// Create system items for several inking tools, including two pens and a watercolor brush.
let firstPen = PKToolPickerInkingItem(type: .pen, color: .red, width: 5.0)
let secondPen = PKToolPickerInkingItem(type: .pen, color: .blue, width: 5.0, identifier: "com.example.second-pen")
let watercolorBrush = PKToolPickerInkingItem(type: .watercolor, color: .green, width: 5.0)

// Create a picker with the tools in a custom order.
let items = [firstPen, secondPen, watercolorBrush, scribbleItem, eraserItem, rulerItem]
let picker = PKToolPicker(toolItems: items)
```

## Parameters

- `items`: An array of items to show in the picker, in the order you specify. Specify at least one item. If this array contains multiple tool items with the same identifier, the picker only shows the first instance of that item.

## See Also

- [init()](pktoolpicker/init.md)
  Creates a new tool picker with a default set of tools.
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
- [class PKToolPickerItem](pktoolpickeritem.md)
  The base class for an item in the tool picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpicker/init(toolitems:))*