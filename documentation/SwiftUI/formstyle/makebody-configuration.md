# makeBody(configuration:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates a view that represents the body of a form.

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
@ViewBuilder
@MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

#### Return Value

A view that has behavior and appearance that enables it to function as a [`Form`](form.md).

## Parameters

- `configuration`: The properties of the form.

## See Also

- [FormStyle.Configuration](formstyle/configuration.md)
  The properties of a form instance.
- [associatedtype Body : View](formstyle/body.md)
  A view that represents the appearance and interaction of a form.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/formstyle/makebody(configuration:))*