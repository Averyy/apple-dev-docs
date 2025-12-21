# Section

**Framework**: SwiftUI  
**Kind**: struct

A container view that you can use to add hierarchy within certain views.

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
struct Section<Parent, Content, Footer>
```

## Mentions

- [Grouping data with lazy stack views](grouping-data-with-lazy-stack-views.md)
- [Displaying data in lists](displaying-data-in-lists.md)
- [Populating SwiftUI menus with adaptive controls](populating-swiftui-menus-with-adaptive-controls.md)
- [Suggesting search terms](suggesting-search-terms.md)

#### Overview

Use `Section` instances in views like [`List`](list.md), [`Picker`](picker.md), and [`Form`](form.md) to organize content into separate sections. Each section has custom content that you provide on a per-instance basis. You can also provide headers and footers for each section.

##### Collapsible Sections

Create sections that expand and collapse by using an initializer that accepts an `isExpanded` binding. A collapsible section in a [`List`](list.md) that uses the [`sidebar`](liststyle/sidebar.md) style shows a disclosure indicator next to the section’s header. Tapping on the disclosure indicator toggles the appearance of the section’s content.

> **Note**: Not all contexts provide a default control to trigger collapse or expansion.

## Topics

### Creating a section
- [init(content:)](section/init(content:).md)
  Creates a section with the provided section content.
- [init(_:content:)](section/init(_:content:).md)
  Creates a section with the provided section content.
### Adding headers and footers
- [init(content:header:)](section/init(content:header:).md)
  Creates a section with a header and the provided section content.
- [init(content: () -> Content, footer: () -> Footer)](section/init(content:footer:).md)
  Creates a section with a footer and the provided section content.
- [init(content: () -> Content, header: () -> Parent, footer: () -> Footer)](section/init(content:header:footer:).md)
  Creates a section with a header, footer, and the provided section content.
### Controlling collapsibility
- [init(_:isExpanded:content:)](section/init(_:isexpanded:content:).md)
  Creates a section with the provided section content.
- [init(isExpanded:content:header:)](section/init(isexpanded:content:header:).md)
  Creates a section with a header, the provided section content, and a binding representing the section’s expansion state.
### Deprecated symbols
- [init(header: Parent, content: () -> Content)](section/init(header:content:).md)
  Creates a section with a header and the provided section content.
- [init(footer: Footer, content: () -> Content)](section/init(footer:content:).md)
  Creates a section with a footer and the provided section content.
- [init(header: Parent, footer: Footer, content: () -> Content)](section/init(header:footer:content:).md)
  Creates a section with a header, footer, and the provided section content.
- [func collapsible(Bool) -> some View](section/collapsible(_:).md)
  Sets whether a section can be collapsed by the user.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [TableRowContent](tablerowcontent.md)
- [View](view.md)

## See Also

- [struct SectionCollection](sectioncollection.md)
  An opaque collection representing the sections of view.
- [struct SectionConfiguration](sectionconfiguration.md)
  Specifies the contents of a section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/section)*