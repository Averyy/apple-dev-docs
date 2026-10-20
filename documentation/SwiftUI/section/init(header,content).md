# init(header:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a section with a header and the provided section content.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2 (renamed: Section(content:header:))
- iPadOS 13.0+ - Deprecated in 27.2 (renamed: Section(content:header:))
- Mac Catalyst 13.0+ - Deprecated in 27.2 (renamed: Section(content:header:))
- macOS 10.15+ - Deprecated in 27.2 (renamed: Section(content:header:))
- tvOS 13.0+ - Deprecated in 27.2 (renamed: Section(content:header:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: Section(content:header:))
- watchOS 6.0+ - Deprecated in 27.2 (renamed: Section(content:header:))

> **Deprecated**: Use `init(content:header:)-29e2l` instead.

## Declaration

```swift
init(header: Parent, @ContentBuilder content: () -> Content)
```

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and `Footer` is `EmptyView`.

## Parameters

- `header`: A view to use as the section’s header.
- `content`: The section’s content.

## See Also

### Deprecated
- [init(footer: Footer, content: () -> Content)](./init%28footer,content%29.md)
  Creates a section with a footer and the provided section content.
- [init(header: Parent, footer: Footer, content: () -> Content)](./init%28header,footer,content%29.md)
  Creates a section with a header, footer, and the provided section content.
- [func collapsible(Bool) -> some View](./collapsible%28_%29.md)
  Sets whether a section can be collapsed by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/section/init(header:content:))*