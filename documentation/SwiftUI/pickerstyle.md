# PickerStyle

**Framework**: SwiftUI  
**Kind**: protocol

A type that specifies the appearance and interaction of all pickers within a view hierarchy.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
protocol PickerStyle
```

## Topics

### Getting built-in picker styles
- [static var automatic: DefaultPickerStyle](pickerstyle/automatic.md)
  The default picker style, based on the picker’s context.
- [static var inline: InlinePickerStyle](pickerstyle/inline.md)
  A `PickerStyle` where each option is displayed inline with other views in the current container.
- [static var menu: MenuPickerStyle](pickerstyle/menu.md)
  A picker style that presents the options as a menu when the user presses a button, or as a submenu when nested within a larger menu.
- [static var navigationLink: NavigationLinkPickerStyle](pickerstyle/navigationlink.md)
  A picker style represented by a navigation link that presents the options by pushing a List-style picker view.
- [static var palette: PalettePickerStyle](pickerstyle/palette.md)
  A picker style that presents the options as a row of compact elements.
- [static var radioGroup: RadioGroupPickerStyle](pickerstyle/radiogroup.md)
  A picker style that presents the options as a group of radio buttons.
- [static var segmented: SegmentedPickerStyle](pickerstyle/segmented.md)
  A picker style that presents the options in a segmented control.
- [static var wheel: WheelPickerStyle](pickerstyle/wheel.md)
  A picker style that presents the options in a scrollable wheel that shows the selected option and a few neighboring options.
### Supporting types
- [struct DefaultPickerStyle](defaultpickerstyle.md)
  The default picker style, based on the picker’s context.
- [struct InlinePickerStyle](inlinepickerstyle.md)
  A `PickerStyle` where each option is displayed inline with other views in the current container.
- [struct MenuPickerStyle](menupickerstyle.md)
  A picker style that presents the options as a menu when the user presses a button, or as a submenu when nested within a larger menu.
- [struct NavigationLinkPickerStyle](navigationlinkpickerstyle.md)
  A picker style represented by a navigation link that presents the options by pushing a List-style picker view.
- [struct PalettePickerStyle](palettepickerstyle.md)
  A picker style that presents the options as a row of compact elements.
- [struct RadioGroupPickerStyle](radiogrouppickerstyle.md)
  A picker style that presents the options as a group of radio buttons.
- [struct SegmentedPickerStyle](segmentedpickerstyle.md)
  A picker style that presents the options in a segmented control.
- [struct WheelPickerStyle](wheelpickerstyle.md)
  A picker style that presents the options in a scrollable wheel that shows the selected option and a few neighboring options.
### Deprecated styles
- [struct PopUpButtonPickerStyle](popupbuttonpickerstyle.md)
  A picker style that presents the options as a menu when the user presses a button.

## Relationships

### Conforming Types
- [DefaultPickerStyle](defaultpickerstyle.md)
- [InlinePickerStyle](inlinepickerstyle.md)
- [MenuPickerStyle](menupickerstyle.md)
- [NavigationLinkPickerStyle](navigationlinkpickerstyle.md)
- [PalettePickerStyle](palettepickerstyle.md)
- [PopUpButtonPickerStyle](popupbuttonpickerstyle.md)
- [RadioGroupPickerStyle](radiogrouppickerstyle.md)
- [SegmentedPickerStyle](segmentedpickerstyle.md)
- [WheelPickerStyle](wheelpickerstyle.md)

## See Also

- [func pickerStyle<S>(S) -> some View](view/pickerstyle(_:).md)
  Sets the style for pickers within this view.
- [func datePickerStyle<S>(S) -> some View](view/datepickerstyle(_:).md)
  Sets the style for date pickers within this view.
- [protocol DatePickerStyle](datepickerstyle.md)
  A type that specifies the appearance and interaction of all date pickers within a view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pickerstyle)*