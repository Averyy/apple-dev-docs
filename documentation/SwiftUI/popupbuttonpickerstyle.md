# PopUpButtonPickerStyle

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A picker style that presents the options as a menu when the user presses a button.

**Availability**:
- macOS 10.15+ - Deprecated in 27.2

> **Deprecated**: Use [`MenuPickerStyle`](./menupickerstyle.md) instead.

## Declaration

```swift
struct PopUpButtonPickerStyle
```

## Overview

Use this style when there are more than five options. Consider using [`RadioGroupPickerStyle`](./radiogrouppickerstyle.md) when there are fewer than five options.

The button itself indicates the selected option. You can include additional controls in the set of options, such as a button to customize the list of options.

To apply this style to a picker, or to a view that contains pickers, use the [`pickerStyle(_:)`](./view/pickerstyle%28_%29.md) modifier.

### Creating the picker style

- [`init()`](./popupbuttonpickerstyle/init%28%29.md)

## Topics

### Initializers
- [init()](./popupbuttonpickerstyle/init%28%29.md)
  Creates a pop-up button picker style.

## Relationships

### Conforms To
- [PickerStyle](./pickerstyle.md)

## See Also

### Supporting types
- [struct DefaultPickerStyle](./defaultpickerstyle.md)
  The default picker style, based on the picker’s context.
- [struct InlinePickerStyle](./inlinepickerstyle.md)
  A `PickerStyle` where each option is displayed inline with other views in the current container.
- [struct MenuPickerStyle](./menupickerstyle.md)
  A picker style that presents the options as a menu when the user presses a button, or as a submenu when nested within a larger menu.
- [struct NavigationLinkPickerStyle](./navigationlinkpickerstyle.md)
  A picker style represented by a navigation link that presents the options by pushing a List-style picker view.
- [struct PalettePickerStyle](./palettepickerstyle.md)
  A picker style that presents the options as a row of compact elements.
- [struct RadioGroupPickerStyle](./radiogrouppickerstyle.md)
  A picker style that presents the options as a group of radio buttons.
- [struct SegmentedPickerStyle](./segmentedpickerstyle.md)
  A picker style that presents the options in a segmented control.
- [struct TabsPickerStyle](./tabspickerstyle.md)
  A picker style that presents options as segmented tabs.
- [struct WheelPickerStyle](./wheelpickerstyle.md)
  A picker style that presents the options in a scrollable wheel that shows the selected option and a few neighboring options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/popupbuttonpickerstyle)*