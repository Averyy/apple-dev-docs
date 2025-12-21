# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance that uniquely identifies and creates slider ticks across updates based on the identity of the underlying data.

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
init<V>(_ data: Data, @SliderTickBuilder<V> content: @escaping (Data.Element) -> Content) where ID == V.ID, V : Identifiable, V == Data.Element, Data.Element == Content.Value
```

## Parameters

- `data`: The identified data that the   instance   uses to create slider ticks dynamically.
- `content`: The builder that creates ticks dynamically for each   element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/slidertickcontentforeach/init(_:content:))*