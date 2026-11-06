# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an arrangement view from a style configuration.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- macOS 27.1+
- tvOS 27.1+
- visionOS 27.1+
- watchOS 27.1+

## Declaration

```swift
nonisolated
init(_ configuration: ArrangementViewStyleConfiguration)
```

Available when `Primary` is `ArrangementViewStyleConfiguration.Primary` and `Secondary` is `ArrangementViewStyleConfiguration.Secondary`.

## Discussion

Use this initializer to implement a custom [`ArrangementViewStyle`](../arrangementviewstyle.md) that composes another arrangement view. Your style can apply its customizations, such as appearance or layout adjustments, while deferring the arrangement of primary and secondary content to the arrangement view:

```swift
struct CustomArrangementViewStyle: ArrangementViewStyle {
    func makeBody(configuration: Configuration) -> some View {
        ArrangementView(configuration)
            .font(.callout)
            .tint(customTint)
    }
}
```

## Parameters

- `configuration`: The style configuration to use.

## See Also

### Creating an arrangement view
- [init(primary: () -> Primary, secondary: () -> Secondary)](./init%28primary,secondary%29.md)
  Creates an arrangement view with a primary and secondary view.
- [struct ArrangementViewStyleConfiguration](../arrangementviewstyleconfiguration.md)
  The properties of an arrangement view you provide to create a custom style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/arrangementview/init(_:))*