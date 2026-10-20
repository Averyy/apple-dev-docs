# init(_:content:)

**Framework**: Swift Charts  
**Kind**: init  
**Role**: Initializer

Creates a chart composed of a series of identifiable marks.

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
init<Data, C>(_ data: Data, @ContentBuilder content: @escaping (Data.Element) -> C) where Content == ForEach<Data, Data.Element.ID, C>, Data : RandomAccessCollection, C : ChartContent, Data.Element : Identifiable
```

#### Discussion

This initializer wraps the data that you provide as input in an implicit [`ForEach`](../../SwiftUI/foreach.md) structure. If you need to represent more than one series in your chart, use [`init(content:)`](./init%28content%29.md) instead.

## Parameters

- `data`: A collection of data that conforms to the [`Identifiable`](../../Swift/identifiable.md) protocol.
- `content`: The mark that the chart should draw for each element in the data collection.

## See Also

### Creating a chart
- [init(content: () -> Content)](./init%28content%29.md)
  Creates a chart composed of any number of data series and individual marks.
- [init<Data, ID, C>(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) -> C)](./init%28_,id,content%29.md)
  Creates a chart composed of a series of marks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chart/init(_:content:))*