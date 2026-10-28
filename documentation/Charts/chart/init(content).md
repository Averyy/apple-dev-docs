# init(content:)

**Framework**: Swift Charts  
**Kind**: init  
**Role**: Initializer

Creates a chart composed of any number of data series and individual marks.

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
init(@ContentBuilder content: () -> Content)
```

## Discussion

This initializer draws the marks that you specify in the `content` input. You can provide individual marks, or marks produced by one or more [`ForEach`](../../SwiftUI/foreach.md) constructs, or any combination of these. As a convenience when you have exactly one `ForEach` in your chart’s content, you can use either the [`init(_:content:)`](./init%28_,content%29.md) or [`init(_:id:content:)`](./init%28_,id,content%29.md) initializer instead, either of which wraps the content in an implicit `ForEach`.

## Parameters

- `content`: A chart content builder that returns the marks that the chart should draw.

## See Also

### Creating a chart
- [init<Data, C>(Data, content: (Data.Element) -> C)](./init%28_,content%29.md)
  Creates a chart composed of a series of identifiable marks.
- [init<Data, ID, C>(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) -> C)](./init%28_,id,content%29.md)
  Creates a chart composed of a series of marks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chart/init(content:))*