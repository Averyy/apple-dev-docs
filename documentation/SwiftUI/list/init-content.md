# init(content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a list with the given content.

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
@MainActor
@preconcurrency init(@ViewBuilder content: () -> Content)
```

## Parameters

- `content`: The content of the list.

## See Also

- [init(selection:content:)](list/init(selection:content:).md)
  Creates a list with the given content that supports selecting a single row that cannot be deselcted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/list/init(content:))*