# MLStreamingVisualizable

**Framework**: Create ML  
**Kind**: protocol

A sequence of image visualizations for machine learning types.

**Availability**:
- macOS 10.15+

## Declaration

```swift
protocol MLStreamingVisualizable : MLVisualizable
```

## Topics

### Seeing the next visualization
- [var hasFinishedStreaming: Bool](mlstreamingvisualizable/hasfinishedstreaming.md)
  A Boolean value that indicates whether the stream has provided its final iteration.
- [func nextIteration()](mlstreamingvisualizable/nextiteration.md)
  Advances the visualization stream to the next iteration.

## Relationships

### Inherits From
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [MLVisualizable](mlvisualizable.md)

## See Also

- [protocol MLVisualizable](mlvisualizable.md)
  An image visualization of machine learning types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstreamingvisualizable)*