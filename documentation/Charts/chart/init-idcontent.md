# init(_:id:content:)

**Framework**: Swift Charts  
**Kind**: init

Creates a chart composed of a series of marks.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init<Data, ID, C>(_ data: Data, id: KeyPath<Data.Element, ID>, @ChartContentBuilder content: @escaping (Data.Element) -> C) where Content == ForEach<Data, ID, C>, Data : RandomAccessCollection, ID : Hashable, C : ChartContent
```

#### Discussion

This initializer wraps the data that you provide as input in an implicit [`ForEach`](https://developer.apple.com/documentation/SwiftUI/ForEach) structure. If you need to represent more than one series in your chart, use [`init(content:)`](chart/init(content:).md) instead.

## Parameters

- `data`: A collection of data.
- `id`: A key path that represents a property of each data element   that can act as a unique identifier for that element. Ensure that   this property conforms to the     protocol.
- `content`: The mark that the chart should draw for each element   in the data collection.

## See Also

- [init(content: () -> Content)](chart/init(content:).md)
  Creates a chart composed of any number of data series and individual marks.
- [init<Data, C>(Data, content: (Data.Element) -> C)](chart/init(_:content:).md)
  Creates a chart composed of a series of identifiable marks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chart/init(_:id:content:))*