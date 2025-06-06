# checkbox

**Framework**: SwiftUI  
**Kind**: property

A toggle style that displays a checkbox followed by its label.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency static var checkbox: CheckboxToggleStyle { get }
```

#### Discussion

Apply this style to a [`Toggle`](toggle.md) or to a view hierarchy that contains toggles using the [`toggleStyle(_:)`](view/togglestyle(_:).md) modifier:

```swift
Toggle("Close windows when quitting an app", isOn: $doesClose)
    .toggleStyle(.checkbox)
```

The style produces a label that describes the purpose of the toggle and a checkbox that shows the toggle’s state. To change the toggle’s state, the user clicks the checkbox or its label:

![A screenshot of a box with a checkmark in it, appearing to the left](https://docs-assets.developer.apple.com/published/44cc20451e73db1b6a205127be5f0e85/ToggleStyle-checkbox-1-macOS%402x.png)

The style aligns the trailing edge of the checkbox with the leading edge of the label, and takes as much horizontal space as it needs to fit the label, up to the amount offered by the toggle’s parent view.

This is the default style in macOS in most contexts when you don’t set a style, or when you apply the [`automatic`](togglestyle/automatic.md) style. A [`Form`](form.md) is a convenient way to present a collection of checkboxes with proper spacing and alignment. For guidance on using checkboxes in your user interface, see [`Toggles`](https://developer.apple.com/design/Human-Interface-Guidelines/toggles) in the Human Interface Guidelines.

## See Also

- [static var automatic: DefaultToggleStyle](togglestyle/automatic.md)
  The default toggle style.
- [static var button: ButtonToggleStyle](togglestyle/button.md)
  A toggle style that displays as a button with its label as the title.
- [static var `switch`: SwitchToggleStyle](togglestyle/switch.md)
  A toggle style that displays a leading label and a trailing switch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/togglestyle/checkbox)*