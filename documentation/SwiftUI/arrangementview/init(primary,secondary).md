# init(primary:secondary:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an arrangement view with a primary and secondary view.

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
init(@ContentBuilder primary: () -> Primary, @ContentBuilder secondary: () -> Secondary)
```

## Parameters

- `primary`: The view to display as the primary content in the arrangement.
- `secondary`: The view to display as the secondary content in the arrangement.

## See Also

### Creating an arrangement view
- [init(ArrangementViewStyleConfiguration)](./init%28_%29.md)
  Creates an arrangement view from a style configuration.
- [struct ArrangementViewStyleConfiguration](../arrangementviewstyleconfiguration.md)
  The properties of an arrangement view you provide to create a custom style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/arrangementview/init(primary:secondary:))*