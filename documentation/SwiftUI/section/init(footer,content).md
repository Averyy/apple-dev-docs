# init(footer:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a section with a footer and the provided section content.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2 (renamed: Section(content:footer:))
- iPadOS 13.0+ - Deprecated in 27.2 (renamed: Section(content:footer:))
- Mac Catalyst 13.0+ - Deprecated in 27.2 (renamed: Section(content:footer:))
- macOS 10.15+ - Deprecated in 27.2 (renamed: Section(content:footer:))
- tvOS 13.0+ - Deprecated in 27.2 (renamed: Section(content:footer:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: Section(content:footer:))
- watchOS 6.0+ - Deprecated in 27.2 (renamed: Section(content:footer:))

> **Deprecated**: Use [`init(content:footer:)`](./init%28content,footer%29.md) instead.

## Declaration

```swift
init(footer: Footer, @ContentBuilder content: () -> Content)
```

Available when `Parent` is `EmptyView`, `Content` conforms to `View`, and `Footer` conforms to `View`.

## Parameters

- `footer`: A view to use as the section’s footer.
- `content`: The section’s content.

## See Also

### Deprecated
- [init(header: Parent, content: () -> Content)](./init%28header,content%29.md)
  Creates a section with a header and the provided section content.
- [init(header: Parent, footer: Footer, content: () -> Content)](./init%28header,footer,content%29.md)
  Creates a section with a header, footer, and the provided section content.
- [func collapsible(Bool) -> some View](./collapsible%28_%29.md)
  Sets whether a section can be collapsed by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/section/init(footer:content:))*