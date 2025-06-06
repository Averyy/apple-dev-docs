# NLDistanceType

**Framework**: Natural Language  
**Kind**: enum

The means of calculating a distance between two locations in a text embedding.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
enum NLDistanceType
```

#### Overview

The meaning of an [`NLDistance`](nldistance.md) is directly related to the [`NLDistanceType`](nldistancetype.md) you use when you call a method that uses it. For example, if you use the [`neighborsForString:maximumCount:distanceType:`](nlembedding/neighborsforstring:maximumcount:distancetype:.md) method and use [`NLDistanceType.cosine`](nldistancetype/cosine.md) for the `distanceType` parameter, the method calculates the cosine distance and returns it as an [`NLDistance`](nldistance.md).

## Topics

### Distance Types
- [NLDistanceType.cosine](nldistancetype/cosine.md)
  A method of calculating distance by using cosine similarity.
### Initializers
- [init?(rawValue: Int)](nldistancetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nldistancetype)*