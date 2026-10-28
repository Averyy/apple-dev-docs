# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an instance that computes slider ticks on demand over a given constant range.

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
init<V>(_ data: Range<Int>, @SliderTickBuilder<V> content: @escaping (Range<Int>.Element) -> Content) where Data == Range<Int>, V == Content.Value
```

**Other overloads**:

```swift
nonisolated
init<V>(_ data: Data, @SliderTickBuilder<V> content: @escaping (Data.Element) -> Content) where ID == V.ID, V : Identifiable, V == Data.Element, Data.Element == Content.Value
```

## Discussion

The instance only reads the initial value of the provided `data` and doesn’t need to identify ticks across updates.

## Parameters

- `data`: A constant range.
- `content`: The builder that creates ticks based on the range index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/slidertickcontentforeach/init(_:content:)-1ph5q)*