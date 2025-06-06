# init(footer:content:)

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
init(footer: Footer, @ViewBuilder content: () -> Content)
```

## Parameters

- `footer`: A view to use as the section’s footer.
- `content`: The section’s content.

## See Also

- [init(header: Parent, content: () -> Content)](section/init(header:content:).md)
  Creates a section with a header and the provided section content.
- [init(header: Parent, footer: Footer, content: () -> Content)](section/init(header:footer:content:).md)
  Creates a section with a header, footer, and the provided section content.
- [func collapsible(Bool) -> some View](section/collapsible(_:).md)
  Sets whether a section can be collapsed by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/section/init(footer:content:))*