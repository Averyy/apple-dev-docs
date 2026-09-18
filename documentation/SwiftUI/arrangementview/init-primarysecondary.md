# init(primary:secondary:)

**Framework**: SwiftUI  
**Kind**: init

Creates an arrangement view with a primary and secondary view.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
nonisolated
init(@ContentBuilder primary: () -> Primary, @ContentBuilder secondary: () -> Secondary)
```

## Parameters

- `primary`: The view to display as the primary content in the arrangement.
- `secondary`: The view to display as the secondary content in the arrangement.

## See Also

- [init(ArrangementViewStyleConfiguration)](arrangementview/init(_:).md)
  Creates an arrangement view from a style configuration.
- [struct ArrangementViewStyleConfiguration](arrangementviewstyleconfiguration.md)
  The properties of an arrangement view used to create its custom style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/arrangementview/init(primary:secondary:))*