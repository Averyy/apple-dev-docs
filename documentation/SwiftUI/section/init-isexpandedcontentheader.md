# init(isExpanded:content:header:)

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
init(isExpanded: Binding<Bool>, @ContentBuilder content: () -> Content, @ContentBuilder header: () -> Parent)
```

## Parameters

- `isExpanded`: A binding to a Boolean value that determines the section’s expansion state (expanded or collapsed).
- `content`: The section’s content.

## See Also

- [init(_:isExpanded:content:)](section/init(_:isexpanded:content:).md)
  Creates a section with the provided section content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/section/init(isexpanded:content:header:))*