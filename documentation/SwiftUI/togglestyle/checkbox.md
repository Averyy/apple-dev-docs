# checkbox

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A toggle style that displays a checkbox followed by its label.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@export(implementation)
nonisolated static var checkbox: CheckboxToggleStyle { get }
```

Available when `Self` is `CheckboxToggleStyle`.

## Discussion

Apply this style to a [`Toggle`](../toggle.md) or to a view hierarchy that contains toggles using the [`toggleStyle(_:)`](../view/togglestyle%28_%29.md) modifier:

```swift
Toggle("Close windows when quitting an app", isOn: $doesClose)
    .toggleStyle(.checkbox)
```

The style produces a label that describes the purpose of the toggle and a checkbox that shows the toggle’s state. To change the toggle’s state, the user clicks the checkbox or its label:

![A screenshot of a box with a checkmark in it, appearing to the left](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/ToggleStyle-checkbox-1-macOS@2x.png)

The style aligns the trailing edge of the checkbox with the leading edge of the label, and takes as much horizontal space as it needs to fit the label, up to the amount offered by the toggle’s parent view.

This is the default style in macOS in most contexts when you don’t set a style, or when you apply the [`automatic`](./automatic.md) style. A [`Form`](../form.md) is a convenient way to present a collection of checkboxes with proper spacing and alignment. For guidance on using checkboxes in your user interface, see [Toggles](https://developer.apple.com/design/human-interface-guidelines/toggles) in the Human Interface Guidelines.

## See Also

### Getting built-in toggle styles
- [static var automatic: DefaultToggleStyle](./automatic.md)
  The default toggle style.
- [static var button: ButtonToggleStyle](./button.md)
  A toggle style that displays as a button with its label as the title.
- [static var `switch`: SwitchToggleStyle](./switch.md)
  A toggle style that displays a leading label and a trailing switch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/togglestyle/checkbox)*