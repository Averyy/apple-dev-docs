# radioGroup

**Framework**: SwiftUI  
**Kind**: property

A picker style that presents the options as a group of radio buttons.

**Availability**:
- macOS 10.15+

## Declaration

```swift
static var radioGroup: RadioGroupPickerStyle { get }
```

#### Discussion

Use this style when there are two to five options. Consider using [`menu`](pickerstyle/menu.md) when there are more than five options.

For each option’s label, use sentence-style capitalization without ending punctuation, like a period or colon.

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
- [static var segmented: SegmentedPickerStyle](pickerstyle/segmented.md)
  A picker style that presents the options in a segmented control.
- [static var wheel: WheelPickerStyle](pickerstyle/wheel.md)
  A picker style that presents the options in a scrollable wheel that shows the selected option and a few neighboring options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pickerstyle/radiogroup)*