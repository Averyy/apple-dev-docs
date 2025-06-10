# init(_:id:content:)

**Framework**: Swift Charts  
**Kind**: init

Creates a 3D chart composed of a series of marks.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
init<Data, ID, C>(_ data: Data, id: KeyPath<Data.Element, ID>, @Chart3DContentBuilder content: @escaping (Data.Element) -> C) where Content == ForEach<Data, ID, C>, Data : RandomAccessCollection, ID : Hashable, C : Chart3DContent
```

#### Discussion

This initializer wraps the data that you provide as input in an implicit [`ForEach`](https://developer.apple.com/documentation/SwiftUI/ForEach) structure. If you need to represent more than one series in your chart, use [`init(content:)`](chart3d/init(content:).md) instead.

## Parameters

- `data`: A collection of data.
- `id`: A key path that represents a property of each data element   that can act as a unique identifier for that element. Ensure that   this property conforms to the     protocol.
- `content`: The mark that the chart should draw for each element   in the data collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chart3d/init(_:id:content:))*