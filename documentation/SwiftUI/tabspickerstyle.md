# TabsPickerStyle

**Framework**: SwiftUI  
**Kind**: struct

A picker style that presents options as segmented tabs.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct TabsPickerStyle
```

#### Overview

On macOS, this style produces a segmented picker with a visual treatment that distinguishes tab navigation from value selection. On iOS, tvOS, and visionOS, the visual appearance matches that of the standard standard `.segmented` style. On all supported platforms, VoiceOver announces options as tabs.

```swift
Picker("View", selection: $view) {
    Text("Events").tag(Views.events)
    Text("Reminders").tag(Views.reminders)
}
.pickerStyle(.tabs)
```

To apply this style to a picker, or to a view that contains pickers, use the [`pickerStyle(_:)`](view/pickerstyle(_:).md) modifier.

You can also use [`tabs`](pickerstyle/tabs.md) to construct this style.

## Topics

### Creating the picker style
- [init()](tabspickerstyle/init.md)
  Creates a tabs picker style.

## Relationships

### Conforms To
- [PickerStyle](pickerstyle.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabspickerstyle)*