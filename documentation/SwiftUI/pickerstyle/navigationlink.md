# navigationLink

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A picker style represented by a navigation link that presents the options by pushing a List-style picker view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@export(implementation)
static var navigationLink: NavigationLinkPickerStyle { get }
```

Available when `Self` is `NavigationLinkPickerStyle`.

## Discussion

In navigation stacks, prefer the default [`menu`](./menu.md) style. Consider the navigation link style when you have a large number of options or your design is better expressed by pushing onto a stack.

To apply this style to a picker, or to a view that contains pickers, use the [`pickerStyle(_:)`](../view/pickerstyle%28_%29.md) modifier.

## See Also

### Getting built-in picker styles
- [static var automatic: DefaultPickerStyle](./automatic.md)
  The default picker style, based on the picker’s context.
- [static var inline: InlinePickerStyle](./inline.md)
  A `PickerStyle` where each option is displayed inline with other views in the current container.
- [static var menu: MenuPickerStyle](./menu.md)
  A picker style that presents the options as a menu when the user presses a button, or as a submenu when nested within a larger menu.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/pickerstyle/navigationlink)*