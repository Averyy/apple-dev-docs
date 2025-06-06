# init(_:isExpanded:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a section with the provided section content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init(_ titleKey: LocalizedStringKey, isExpanded: Binding<Bool>, @ViewBuilder content: () -> Content)
```

## Parameters

- `titleKey`: The key for the section’s localized title, which describes   the contents of the section.
- `isExpanded`: A binding to a Boolean value that determines the section’s   expansion state (expanded or collapsed).
- `content`: The section’s content.

## See Also

- [init(isExpanded:content:header:)](section/init(isexpanded:content:header:).md)
  Creates a section with a header, the provided section content, and a binding representing the section’s expansion state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/section/init(_:isexpanded:content:))*