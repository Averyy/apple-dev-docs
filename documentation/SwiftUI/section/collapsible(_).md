# collapsible(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets whether a section can be collapsed by the user.

**Availability**:
- macOS 10.15+ - Deprecated in 27.2

> **Deprecated**: To disable collapsibility in macOS 14 and later, use one of the [`Section`](../section.md) initializers that lacks collapsibility.

## Declaration

```swift
func collapsible(_ collapsible: Bool) -> some View
```

Available when `Parent` conforms to `View`, `Content` conforms to `View`, and `Footer` conforms to `View`.

#### Discussion

This modifier only applies to sections in [`List`](../list.md) views that have the [`sidebar`](../liststyle/sidebar.md) style.

## See Also

### Deprecated
- [init(header: Parent, content: () -> Content)](./init%28header,content%29.md)
  Creates a section with a header and the provided section content.
- [init(footer: Footer, content: () -> Content)](./init%28footer,content%29.md)
  Creates a section with a footer and the provided section content.
- [init(header: Parent, footer: Footer, content: () -> Content)](./init%28header,footer,content%29.md)
  Creates a section with a header, footer, and the provided section content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/section/collapsible(_:))*