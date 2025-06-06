# makeBody(configuration:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Creates a view that represents the body of a button.

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
@ViewBuilder
@MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

#### Discussion

The system calls this method for each [`Button`](button.md) instance in a view hierarchy where this style is the current button style.

## See Also

- [PrimitiveButtonStyle.Configuration](primitivebuttonstyle/configuration.md)
  The properties of a button.
- [associatedtype Body : View](primitivebuttonstyle/body.md)
  A view that represents the body of a button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/primitivebuttonstyle/makebody(configuration:))*