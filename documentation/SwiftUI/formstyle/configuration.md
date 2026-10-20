# FormStyle.Configuration

**Framework**: SwiftUI  
**Kind**: typealias  
**Role**: Type Alias

The properties of a form instance.

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
typealias Configuration = FormStyleConfiguration
```

#### Discussion

You receive a `configuration` parameter of this type — which is an alias for the [`FormStyleConfiguration`](../formstyleconfiguration.md) type — when you implement the required [`makeBody(configuration:)`](./makebody%28configuration%29.md) method in a custom form style implementation.

## See Also

### Creating custom form styles
- [func makeBody(configuration: Self.Configuration) -> Self.Body](./makebody%28configuration%29.md)
  Creates a view that represents the body of a form.
- [associatedtype Body : View](./body.md)
  A view that represents the appearance and interaction of a form.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/formstyle/configuration)*