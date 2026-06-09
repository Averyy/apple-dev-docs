# tabs

**Framework**: SwiftUI  
**Kind**: property

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
static var tabs: TabsPickerStyle { get }
```

#### Discussion

On macOS, this style produces a segmented picker with a visual treatment that distinguishes tab navigation from value selection. On iOS, tvOS, and visionOS, the visual appearance matches that of the standard standard `.segmented` style. On all supported platforms, VoiceOver announces options as tabs.

```swift
Picker("View", selection: $view) {
    Text("Events").tag(Views.events)
    Text("Reminders").tag(Views.reminders)
}
.pickerStyle(.tabs)
```

To apply this style to a picker, or to a view that contains pickers, use the [`pickerStyle(_:)`](view/pickerstyle(_:).md) modifier.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pickerstyle/tabs)*