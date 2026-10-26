# PKToolPickerCustomItemConfiguration

**Framework**: PencilKit  
**Kind**: class  
**Role**: Class

A configuration that specifies the appearance and behavior of a custom tool item and its contents.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```objc
@interface PKToolPickerCustomItemConfiguration : NSObject
```

## Topics

### Creating a configuration
- [- initWithIdentifier:name:](./pktoolpickercustomitemconfiguration/initwithidentifier_name_.md)
  Create a new configuration with an identifier and a name.
### Identifying the custom item
- [identifier](./pktoolpickercustomitemconfiguration/identifier.md)
  A string that uniquely identifies the tool in the picker.
- [name](./pktoolpickercustomitemconfiguration/name.md)
  A short string to show as the name of the tool in the UI.
### Customizing color
- [defaultColor](./pktoolpickercustomitemconfiguration/defaultcolor.md)
  The default color for the tool.
- [allowsColorSelection](./pktoolpickercustomitemconfiguration/allowscolorselection.md)
  A Boolean value that determines whether to show the color selection UI for the tool.
### Customizing width
- [defaultWidth](./pktoolpickercustomitemconfiguration/defaultwidth.md)
  The default width for the tool.
- [widthVariants](./pktoolpickercustomitemconfiguration/widthvariants.md)
  A dictionary with UI options for selecting width, with each element containing a width value and its corresponding image.
### Providing an image for the tool
- [imageProvider](./pktoolpickercustomitemconfiguration/imageprovider.md)
  A closure that provides an image for the tool.
### Providing a custom view controller for the tool
- [viewControllerProvider](./pktoolpickercustomitemconfiguration/viewcontrollerprovider.md)
  A closure to provide a view controller above the system controls in the tool attributes popover.
### Instance Properties
- [toolAttributeControls](./pktoolpickercustomitemconfiguration/toolattributecontrols.md)
  Defines which attribute controls are available to be presented in UI such as the tool attributes popover, or inline in the picker presented from a pencil squeeze. Controls for properties which the tool item does not support will not be presented. Excluding a control here does not hide all UI for adjusting that value. For example, excluding the opacity control here will not remove it from the color picker, if the color picker is otherwise available. Defaults to all controls.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Configuring the custom item
- [var color: UIColor](./pktoolpickercustomitem/color.md)
  The current color of the custom tool item.
- [var width: CGFloat](./pktoolpickercustomitem/width.md)
  The current width of the custom tool item.
- [configuration](./pktoolpickercustomitem/configuration-v7e5.md)
  The configuration of the custom tool item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pktoolpickercustomitemconfiguration)*