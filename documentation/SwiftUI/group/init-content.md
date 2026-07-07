# init(content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a group of content.

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
@export(implementation)
nonisolated init(@ContentBuilder content: () -> Content)
```

## Parameters

- `content`: A [`ContentBuilder`](contentbuilder.md) that produces the content to group.

## See Also

- [init<Base, Result>(sections: Base, transform: (SectionCollection) -> Result)](group/init(sections:transform:).md)
  Constructs a group from the sections of the given view.
- [init<Base, Result>(subviews: Base, transform: (SubviewsCollection) -> Result)](group/init(subviews:transform:).md)
  Constructs a group from the subviews of the given view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/group/init(content:))*