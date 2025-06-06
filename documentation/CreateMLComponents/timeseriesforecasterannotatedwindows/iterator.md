# TimeSeriesForecasterAnnotatedWindows.Iterator

**Framework**: Create ML Components  
**Kind**: struct

A time-series forecaster batch sequence iterator.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct Iterator
```

## Topics

### Instance Methods
- [func next() -> AnnotatedFeature<MLShapedArray<Scalar>, MLShapedArray<Scalar>>?](timeseriesforecasterannotatedwindows/iterator/next.md)
  Advances to the next element and returns it, or `nil` if no next element exists.
### Type Aliases
- [TimeSeriesForecasterAnnotatedWindows.Iterator.Element](timeseriesforecasterannotatedwindows/iterator/element.md)
  The type of element traversed by the iterator.

## Relationships

### Conforms To
- [IteratorProtocol](../Swift/IteratorProtocol.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesforecasterannotatedwindows/iterator)*