# init(content:footer:)

**Framework**: SwiftUI  
**Kind**: init

Creates a section with a footer and the provided section content.

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
init(@ViewBuilder content: () -> Content, @ViewBuilder footer: () -> Footer)
```

## Parameters

- `content`: The section’s content.
- `footer`: A view to use as the section’s footer.

## See Also

- [init(content:header:)](section/init(content:header:).md)
  Creates a section with a header and the provided section content.
- [init(content: () -> Content, header: () -> Parent, footer: () -> Footer)](section/init(content:header:footer:).md)
  Creates a section with a header, footer, and the provided section content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/section/init(content:footer:))*