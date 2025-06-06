# ToggleStyle.Configuration

**Framework**: SwiftUI  
**Kind**: typealias

The properties of a toggle instance.

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
typealias Configuration = ToggleStyleConfiguration
```

#### Discussion

You receive a `configuration` parameter of this type — which is an alias for the [`ToggleStyleConfiguration`](togglestyleconfiguration.md) type — when you implement the required [`makeBody(configuration:)`](togglestyle/makebody(configuration:).md) method in a custom toggle style implementation.

## See Also

- [func makeBody(configuration: Self.Configuration) -> Self.Body](togglestyle/makebody(configuration:).md)
  Creates a view that represents the body of a toggle.
- [struct ToggleStyleConfiguration](togglestyleconfiguration.md)
  The properties of a toggle instance.
- [associatedtype Body : View](togglestyle/body.md)
  A view that represents the appearance and interaction of a toggle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/togglestyle/configuration)*