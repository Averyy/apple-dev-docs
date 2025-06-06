# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a section with the provided content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(_ titleKey: LocalizedStringKey, @TabContentBuilder<SelectionValue> content: () -> Content) where Header == Text, Footer == EmptyView
```

## Parameters

- `titleKey`: The localized string key label for the section’s header.
- `content`: The section’s content.

## See Also

- [init(content:)](tabsection/init(content:).md)
  Creates a section with the provided section content.
- [init(content:header:)](tabsection/init(content:header:).md)
  Creates a section with a header and the provided section content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tabsection/init(_:content:))*