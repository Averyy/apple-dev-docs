# init(sections:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance that uniquely identifies and creates views across updates based on the sections of a given view.

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
init<V>(sections view: V, @ContentBuilder content: @escaping (SectionConfiguration) -> Content) where Data == ForEachSectionCollection<Content>, ID == SectionConfiguration.ID, Content : View, V : View
```

## Parameters

- `view`: The view to extract the sections of.
- `content`: The content builder that creates views from sections

## See Also

- [init(Data)](foreach/init(_:).md)
  Creates an instance that uniquely identifies and creates table rows across updates based on the identity of the underlying data.
- [init(_:content:)](foreach/init(_:content:).md)
  Creates an instance that uniquely identifies and creates map content across updates based on the identity of the underlying data.
- [init(_:id:content:)](foreach/init(_:id:content:).md)
  Creates an instance that uniquely identifies and creates map content across updates based on the provided key path to the underlying data’s identifier.
- [init<V>(subviews: V, content: (Subview) -> Content)](foreach/init(subviews:content:).md)
  Creates an instance that uniquely identifies and creates views across updates based on the subviews of a given view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/foreach/init(sections:content:))*