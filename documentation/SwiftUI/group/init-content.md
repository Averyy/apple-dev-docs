# init(content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a group of map content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
init(@MapContentBuilder content: () -> Content)
```

## Parameters

- `content`: A map content builder that produces the map content to group.

## See Also

- [init<Base, Result>(sections: Base, transform: (SectionCollection) -> Result)](group/init(sections:transform:).md)
  Constructs a group from the sections of the given view.
- [init<Base, Result>(subviews: Base, transform: (SubviewsCollection) -> Result)](group/init(subviews:transform:).md)
  Constructs a group from the subviews of the given view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/group/init(content:))*