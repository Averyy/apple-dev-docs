# menu

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A picker style that presents the options as a menu when the user presses a button, or as a submenu when nested within a larger menu.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
static var menu: MenuPickerStyle { get }
```

Available when `Self` is `MenuPickerStyle`.

## Mentions

- [Populating SwiftUI menus with adaptive controls](../populating-swiftui-menus-with-adaptive-controls.md)

## Discussion

Use this style when there are more than five options. Consider using [`inline`](./inline.md) when there are fewer than five options.

The button itself indicates the selected option. You can include additional controls in the set of options, such as a button to customize the list of options.

To apply this style to a picker, or to a view that contains pickers, use the [`pickerStyle(_:)`](../view/pickerstyle%28_%29.md) modifier.

## See Also

### Getting built-in picker styles
- [static var automatic: DefaultPickerStyle](./automatic.md)
  The default picker style, based on the picker’s context.
- [static var inline: InlinePickerStyle](./inline.md)
  A `PickerStyle` where each option is displayed inline with other views in the current container.
- [static var navigationLink: NavigationLinkPickerStyle](./navigationlink.md)
  A picker style represented by a navigation link that presents the options by pushing a List-style picker view.
- [static var palette: PalettePickerStyle](./palette.md)
  A picker style that presents the options as a row of compact elements.
- [static var radioGroup: RadioGroupPickerStyle](./radiogroup.md)
  A picker style that presents the options as a group of radio buttons.
- [static var segmented: SegmentedPickerStyle](./segmented.md)
  A picker style that presents the options in a segmented control.
- [static var tabs: TabsPickerStyle](./tabs.md)
  A picker style that presents options as segmented tabs.
- [static var wheel: WheelPickerStyle](./wheel.md)
  A picker style that presents the options in a scrollable wheel that shows the selected option and a few neighboring options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pickerstyle/menu)*