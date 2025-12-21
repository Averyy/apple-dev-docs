# init(_:id:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance that uniquely identifies and creates slider ticks across updates based on the provided key path to the underlying data’s identifier.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
nonisolated
init<V>(_ data: Data, id: KeyPath<Data.Element, ID>, @SliderTickBuilder<V> content: @escaping (Data.Element) -> Content) where V == Data.Element, Data.Element == Content.Value
```

#### Discussion

It’s important that the `id` of a data element doesn’t change, unless SwiftUI considers the data element to have been replaced with a new data element that has a new identity. If the `id` of a data element changes, then the marks generated from that data element will lose any current state and animations.

## Parameters

- `data`: The data that the   instance uses to create mark items   dynamically.
- `id`: The key path to the provided data’s identifier.
- `content`: The builder that creates ticks dynamically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/slidertickcontentforeach/init(_:id:content:))*