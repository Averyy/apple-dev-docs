# init(_:id:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance that uniquely identifies and creates map content across updates based on the provided key path to the underlying data’s identifier.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
init(_ data: Data, id: KeyPath<Data.Element, ID>, @MapContentBuilder content: @escaping (Data.Element) -> Content)
```

## Mentions

- [Creating performant scrollable stacks](creating-performant-scrollable-stacks.md)

#### Discussion

It’s important that the `id` of a data element doesn’t change, unless the data element has been replaced with a new data element that has a new identity. If the `id` of a data element changes, then the map content generated from that data element will lose any current state and animations.

## Parameters

- `data`: The data that the   instance uses to create map   content dynamically.
- `id`: The key path to the provided data’s identifier.
- `content`: The map content builder that creates map content   dynamically.

## See Also

- [init(Data)](foreach/init(_:).md)
  Creates an instance that uniquely identifies and creates table rows across updates based on the identity of the underlying data.
- [init(_:content:)](foreach/init(_:content:).md)
  Creates an instance that uniquely identifies and creates map content across updates based on the identity of the underlying data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/foreach/init(_:id:content:))*