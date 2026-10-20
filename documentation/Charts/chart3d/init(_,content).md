# init(_:content:)

**Framework**: Swift Charts  
**Kind**: init  
**Role**: Initializer

Creates a 3D chart composed of a series of identifiable marks.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
init<Data, C>(_ data: Data, @Chart3DContentBuilder content: @escaping (Data.Element) -> C) where Content == ForEach<Data, Data.Element.ID, C>, Data : RandomAccessCollection, C : Chart3DContent, Data.Element : Identifiable
```

Available when `Content` conforms to `Chart3DContent`.

#### Discussion

This initializer wraps the data that you provide as input in an implicit [`ForEach`](../../SwiftUI/foreach.md) structure. If you need to represent more than one series in your chart, use [`init(content:)`](./init%28content%29.md) instead.

## Parameters

- `data`: A collection of data that conforms to the [`Identifiable`](../../Swift/identifiable.md) protocol.
- `content`: The mark that the chart should draw for each element in the data collection.

## See Also

### Creating 3D charts
- [init<Data, ID, C>(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) -> C)](./init%28_,id,content%29.md)
  Creates a 3D chart composed of a series of marks.
- [init(content: () -> Content)](./init%28content%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chart3d/init(_:content:))*