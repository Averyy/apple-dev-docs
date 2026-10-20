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

## See Also

### Creating an arrangement view
- [init(primary: () -> Primary, secondary: () -> Secondary)](./init%28primary,secondary%29.md)
  Creates an arrangement view with a primary and secondary view.
- [struct ArrangementViewStyleConfiguration](../arrangementviewstyleconfiguration.md)
  The properties of an arrangement view you provide to create a custom style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/arrangementview/init(_:))*