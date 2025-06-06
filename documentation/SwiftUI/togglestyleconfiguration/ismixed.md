# isMixed

**Framework**: SwiftUI  
**Kind**: property

Whether the [`Toggle`](toggle.md) is currently in a mixed state.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var isMixed: Bool
```

#### Discussion

Use this property to determine whether the toggle style should render a mixed state presentation. A mixed state corresponds to an underlying collection with a mix of true and false Bindings. To toggle the state, use the `Bool.toggle()` method on the [`isOn`](togglestyleconfiguration/ison.md) binding.

In the following example, a custom style uses the `isMixed` property to render the correct toggle state using symbols:

```swift
struct SymbolToggleStyle: ToggleStyle {
    func makeBody(configuration: Configuration) -> some View {
        Button {
            configuration.isOn.toggle()
        } label: {
            Image(
                systemName: configuration.isMixed
                ? "minus.circle.fill" : configuration.isOn
                ? "checkmark.circle.fill" : "circle.fill")
            configuration.label
        }
    }
}
```

## See Also

- [var isOn: Bool](togglestyleconfiguration/ison.md)
  A binding to a state property that indicates whether the toggle is on.
- [var $isOn: Binding<Bool>](togglestyleconfiguration/$ison.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/togglestyleconfiguration/ismixed)*