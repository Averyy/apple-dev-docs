# collapsible(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets whether a section can be collapsed by the user.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func collapsible(_ collapsible: Bool) -> some View
```

#### Discussion

This modifier only applies to sections in [`List`](list.md) views that have the [`sidebar`](liststyle/sidebar.md) style.

## See Also

- [init(header: Parent, content: () -> Content)](section/init(header:content:).md)
  Creates a section with a header and the provided section content.
- [init(footer: Footer, content: () -> Content)](section/init(footer:content:).md)
  Creates a section with a footer and the provided section content.
- [init(header: Parent, footer: Footer, content: () -> Content)](section/init(header:footer:content:).md)
  Creates a section with a header, footer, and the provided section content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/section/collapsible(_:))*