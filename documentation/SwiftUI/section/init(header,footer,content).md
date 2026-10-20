# init(header:footer:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a section with a header, footer, and the provided section content.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2 (renamed: Section(content:header:footer:))
- iPadOS 13.0+ - Deprecated in 27.2 (renamed: Section(content:header:footer:))
- Mac Catalyst 13.0+ - Deprecated in 27.2 (renamed: Section(content:header:footer:))
- macOS 10.15+ - Deprecated in 27.2 (renamed: Section(content:header:footer:))
- tvOS 13.0+ - Deprecated in 27.2 (renamed: Section(content:header:footer:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: Section(content:header:footer:))
- watchOS 6.0+ - Deprecated in 27.2 (renamed: Section(content:header:footer:))

> **Deprecated**: Use [`init(content:header:footer:)`](./init%28content,header,footer%29.md) instead.

## Declaration

```swift
init(header: Parent, footer: Footer, @ContentBuilder content: () -> Content)
```

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and `Footer` conforms to `View`.

## Parameters

- `header`: A view to use as the section’s header.
- `footer`: A view to use as the section’s footer.
- `content`: The section’s content.

## See Also

### Deprecated
- [init(header: Parent, content: () -> Content)](./init%28header,content%29.md)
  Creates a section with a header and the provided section content.
- [init(footer: Footer, content: () -> Content)](./init%28footer,content%29.md)
  Creates a section with a footer and the provided section content.
- [func collapsible(Bool) -> some View](./collapsible%28_%29.md)
  Sets whether a section can be collapsed by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/section/init(header:footer:content:))*