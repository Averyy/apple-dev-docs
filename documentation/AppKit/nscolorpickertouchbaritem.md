# NSColorPickerTouchBarItem

**Framework**: AppKit  
**Kind**: class

A bar item that provides a system-defined color picker.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
@MainActor
class NSColorPickerTouchBarItem
```

#### Overview

For design guidance, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/macos/touch-bar/touch-bar-controls-and-views/#color-pickers).

## Topics

### Creating a color picker item
- [class func colorPicker(withIdentifier: NSTouchBarItem.Identifier) -> Self](nscolorpickertouchbaritem/colorpicker(withidentifier:).md)
  Creates a bar item with the standard color picker icon.
- [class func textColorPicker(withIdentifier: NSTouchBarItem.Identifier) -> Self](nscolorpickertouchbaritem/textcolorpicker(withidentifier:).md)
  Creates a bar item with the standard text color picker icon.
- [class func strokeColorPicker(withIdentifier: NSTouchBarItem.Identifier) -> Self](nscolorpickertouchbaritem/strokecolorpicker(withidentifier:).md)
  Creates a bar item with the standard stroke color picker icon.
- [class func colorPicker(withIdentifier: NSTouchBarItem.Identifier, buttonImage: UIImage) -> Self](nscolorpickertouchbaritem/colorpicker(withidentifier:buttonimage:).md)
  Creates a color picker bar item using the supplied image as its icon.
### Configuring the color picker
- [var colorList: NSColorList!](nscolorpickertouchbaritem/colorlist.md)
  The list of colors displayed in the color picker.
- [var allowedColorSpaces: [NSColorSpace]?](nscolorpickertouchbaritem/allowedcolorspaces.md)
  Controls the color spaces that the color picker can produce.
- [var showsAlpha: Bool](nscolorpickertouchbaritem/showsalpha.md)
  A Boolean value that controls whether the color picker allows picking of colors with alpha values other than `1.0`.
- [var isEnabled: Bool](nscolorpickertouchbaritem/isenabled.md)
  A Boolean value that determines whether the color picker is enabled.
### Obtaining the selected color
- [var color: UIColor](nscolorpickertouchbaritem/color.md)
  The picker’s currently selected color.
- [var target: AnyObject?](nscolorpickertouchbaritem/target.md)
  An object that is notified when a user interacts with the color picker.
- [var action: Selector?](nscolorpickertouchbaritem/action.md)
  The selector on the target object that is invoked when a user interacts with the color picker.
### Configuring bar customization
- [var customizationLabel: String!](nscolorpickertouchbaritem/customizationlabel.md)
  The user-visible string identifying this item during touch bar customization.

## Relationships

### Inherits From
- [NSTouchBarItem](nstouchbaritem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSColorPicker](nscolorpicker.md)
  An abstract superclass that implements the default color picking protocol.
- [class NSColorWell](nscolorwell.md)
  A control that displays a color value and lets the user change that color value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickertouchbaritem)*