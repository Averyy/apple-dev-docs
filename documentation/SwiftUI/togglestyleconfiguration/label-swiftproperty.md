# label

**Framework**: SwiftUI  
**Kind**: property

A view that describes the effect of switching the toggle between states.

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
let label: ToggleStyleConfiguration.Label
```

#### Discussion

Use this value in your implementation of the [`makeBody(configuration:)`](togglestyle/makebody(configuration:).md) method when defining a custom [`ToggleStyle`](togglestyle.md). Access it through the that method’s `configuration` parameter.

Because the label is a [`View`](view.md), you can incorporate it into the view hierarchy that you return from your style definition. For example, you can combine the label with a circle image in an [`HStack`](hstack.md):

```swift
HStack {
    Image(systemName: configuration.isOn
        ? "checkmark.circle.fill"
        : "circle")
    configuration.label
}
```

## See Also

- [ToggleStyleConfiguration.Label](togglestyleconfiguration/label-swift.struct.md)
  A type-erased label of a toggle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/togglestyleconfiguration/label-swift.property)*