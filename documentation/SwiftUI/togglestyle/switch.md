# switch

**Framework**: SwiftUI  
**Kind**: property

A toggle style that displays a leading label and a trailing switch.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency static var `switch`: SwitchToggleStyle { get }
```

#### Discussion

Apply this style to a [`Toggle`](toggle.md) or to a view hierarchy that contains toggles using the [`toggleStyle(_:)`](view/togglestyle(_:).md) modifier:

```swift
Toggle("Enhance Sound", isOn: $isEnhanced)
    .toggleStyle(.switch)
```

The style produces a label that describes the purpose of the toggle and a switch that shows the toggle’s state. The user taps or clicks the switch to change the toggle’s state. The default appearance is similar across platforms, although the way you use switches in your user interface varies a little, as described in [`Toggles`](https://developer.apple.com/design/Human-Interface-Guidelines/toggles) in the Human Interface Guidelines.

In iOS, iPadOS, watchOS, and tvOS, the label and switch fill as much horizontal space as the toggle’s parent offers by aligning the label’s leading edge and the switch’s trailing edge with the containing view’s respective leading and trailing edges. In macOS, the style uses a minimum of horizontal space by aligning the trailing edge of the label with the leading edge of the switch. SwiftUI helps you to manage the spacing and alignment when this style appears in a [`Form`](form.md).

SwiftUI uses this style as the default for iOS, iPadOS, watchOS, and tvOS in most contexts when you don’t set a style, or when you apply the [`automatic`](togglestyle/automatic.md) style.

## See Also

- [static var automatic: DefaultToggleStyle](togglestyle/automatic.md)
  The default toggle style.
- [static var button: ButtonToggleStyle](togglestyle/button.md)
  A toggle style that displays as a button with its label as the title.
- [static var checkbox: CheckboxToggleStyle](togglestyle/checkbox.md)
  A toggle style that displays a checkbox followed by its label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/togglestyle/switch)*