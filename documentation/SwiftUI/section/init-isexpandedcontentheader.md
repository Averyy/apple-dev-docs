# init(isExpanded:content:header:)

**Framework**: SwiftUI  
**Kind**: init

Creates a section with a header, the provided section content, and a binding representing the section’s expansion state.

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
init(isExpanded: Binding<Bool>, @ViewBuilder content: () -> Content, @ViewBuilder header: () -> Parent)
```

## Parameters

- `isExpanded`: A binding to a Boolean value that determines the section’s   expansion state (expanded or collapsed).
- `content`: The section’s content.
- `header`: A view to use as the section’s header.

## See Also

- [init(_:isExpanded:content:)](section/init(_:isexpanded:content:).md)
  Creates a section with the provided section content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/section/init(isexpanded:content:header:))*