# PKToolPickerCustomItem.Configuration

**Framework**: PencilKit  
**Kind**: struct

A configuration that specifies the appearance and behavior of a custom tool item and its contents.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Creating a configuration
- [init(identifier: String, name: String)](pktoolpickercustomitem/configuration-swift.struct/init(identifier:name:).md)
  Create a new configuration with an identifier and a name.
### Identifying the custom tool
- [var identifier: String](pktoolpickercustomitem/configuration-swift.struct/identifier.md)
  A string that uniquely identifies the tool in the picker.
- [var name: String](pktoolpickercustomitem/configuration-swift.struct/name.md)
  A short string to show as the name of the tool in the UI.
### Customizing color
- [var defaultColor: UIColor](pktoolpickercustomitem/configuration-swift.struct/defaultcolor.md)
  The default color for the tool.
- [var allowsColorSelection: Bool](pktoolpickercustomitem/configuration-swift.struct/allowscolorselection.md)
  A Boolean value that determines whether to show the color selection UI for the tool.
### Customizing width
- [var defaultWidth: CGFloat](pktoolpickercustomitem/configuration-swift.struct/defaultwidth.md)
  The default width for the tool.
- [var widthVariants: [CGFloat : UIImage]](pktoolpickercustomitem/configuration-swift.struct/widthvariants.md)
  A dictionary with UI options for selecting width, with each element containing a width value and its corresponding image.
### Providing an image for the tool
- [var imageProvider: ((PKToolPickerCustomItem) -> UIImage)?](pktoolpickercustomitem/configuration-swift.struct/imageprovider.md)
  A closure to provide an image that represents the custom tool item.
### Providing a custom view controller for the tool
- [var viewControllerProvider: ((PKToolPickerCustomItem) -> UIViewController)?](pktoolpickercustomitem/configuration-swift.struct/viewcontrollerprovider.md)
  A closure to provide a view controller above the system controls in the tool attributes popover.
### Instance Properties
- [var toolAttributeControls: PKToolPickerCustomItem.ControlOptions](pktoolpickercustomitem/configuration-swift.struct/toolattributecontrols.md)
  Defines which attribute controls are available to be presented in UI such as the tool attributes popover, or inline in the picker presented from a pencil squeeze. Controls for properties which the tool item does not support will not be presented. Excluding a control here does not hide all UI for adjusting that value. For example, excluding the opacity control here will not remove it from the color picker, if the color picker is otherwise available. Defaults to all controls.

## See Also

- [var color: UIColor](pktoolpickercustomitem/color.md)
  The current color of the custom tool item.
- [var width: CGFloat](pktoolpickercustomitem/width.md)
  The current width of the custom tool item.
- [var configuration: PKToolPickerCustomItem.Configuration](pktoolpickercustomitem/configuration-41nm4.md)
  The configuration of the custom tool item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpickercustomitem/configuration-swift.struct)*