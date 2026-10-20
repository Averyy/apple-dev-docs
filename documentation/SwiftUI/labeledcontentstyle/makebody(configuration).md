# makeBody(configuration:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a view that represents the body of labeled content.

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
@ContentBuilder
@MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

## See Also

### Creating custom labeled content styles
- [LabeledContentStyle.Configuration](./configuration.md)
  The properties of a labeled content instance.
- [associatedtype Body : View](./body.md)
  A view that represents the appearance and behavior of labeled content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/labeledcontentstyle/makebody(configuration:))*