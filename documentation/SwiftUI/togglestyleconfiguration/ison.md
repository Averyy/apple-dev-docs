# isOn

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

A binding to a state property that indicates whether the toggle is on.

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
@Binding
var isOn: Bool { get nonmutating set }
```

#### Discussion

Because this value is a [`Binding`](../binding.md), you can both read and write it in your implementation of the [`makeBody(configuration:)`](../togglestyle/makebody%28configuration%29.md) method when defining a custom [`ToggleStyle`](../togglestyle.md). Access it through that method’s `configuration` parameter.

Read this value to set the appearance of the toggle. For example, you can choose between empty and filled circles based on the `isOn` value:

```swift
Image(systemName: configuration.isOn
    ? "checkmark.circle.fill"
    : "circle")
```

Write this value when the user takes an action that’s meant to change the state of the toggle. For example, you can toggle it inside the `action` closure of a [`Button`](../button.md) instance:

```swift
Button {
    configuration.isOn.toggle()
} label: {
    // Draw the toggle.
}
```

## See Also

### Managing the toggle state
- [var isMixed: Bool](./ismixed.md)
  Whether the [`Toggle`](../toggle.md) is currently in a mixed state.
- [var $isOn: Binding<Bool>](./dollarison.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/togglestyleconfiguration/ison)*