# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance that uniquely identifies and creates map content across updates based on the identity of the underlying data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
init(_ data: Data, @MapContentBuilder content: @escaping (Data.Element) -> Content) where ID == Data.Element.ID, Data.Element : Identifiable
```

#### Discussion

It’s important that the `id` of a data element doesn’t change unless you replace the data element with a new data element that has a new identity. If the `id` of a data element changes, the content view generated from that data element loses any current state and animations.

## Parameters

- `data`: The identified data that the [`ForEach`](foreach.md) instance uses to create map content dynamically.
- `content`: The map content builder that creates map content dynamically.

## See Also

- [init(Data)](foreach/init(_:).md)
  Creates an instance that uniquely identifies and creates table rows across updates based on the identity of the underlying data.
- [init(_:id:content:)](foreach/init(_:id:content:).md)
  Creates an instance that uniquely identifies and creates map content across updates based on the provided key path to the underlying data’s identifier.
- [init<V>(sections: V, content: (SectionConfiguration) -> Content)](foreach/init(sections:content:).md)
  Creates an instance that uniquely identifies and creates views across updates based on the sections of a given view.
- [init<V>(subviews: V, content: (Subview) -> Content)](foreach/init(subviews:content:).md)
  Creates an instance that uniquely identifies and creates views across updates based on the subviews of a given view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/foreach/init(_:content:))*