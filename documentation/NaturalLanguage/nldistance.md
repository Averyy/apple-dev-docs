# NLDistance

**Framework**: Natural Language  
**Kind**: typealias  
**Role**: Type Alias

The distance between two strings in a text embedding.

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
typealias NLDistance = Double
```

```c
typedef double NLDistance;
```

#### Discussion

The meaning of an [`NLDistance`](./nldistance.md) is directly related to the [`NLDistanceType`](./nldistancetype.md) you use when you call a method that uses it. For example, if you use the [`neighborsForString:maximumCount:distanceType:`](./nlembedding/neighborsforstring_maximumcount_distancetype_.md) method and use [`NLDistanceType.cosine`](./nldistancetype/cosine.md) for the `distanceType` parameter, the method calculates the cosine distance and returns it as an [`NLDistance`](./nldistance.md).

## Topics

### Calculating Distance
- [enum NLDistanceType](./nldistancetype.md)
  The means of calculating a distance between two locations in a text embedding.

## See Also

### Finding strings and their distances in an embedding
- [func neighbors(for: String, maximumCount: Int, distanceType: NLDistanceType) -> [(String, NLDistance)]](./nlembedding/neighbors%28for,maximumcount,distancetype%29-8f1jc.md)
  Retrieves a limited number of strings near a string in the vocabulary.
- [func neighbors(for: [Double], maximumCount: Int, distanceType: NLDistanceType) -> [(String, NLDistance)]](./nlembedding/neighbors%28for,maximumcount,distancetype%29-8lp4z.md)
  Retrieves a limited number of strings near a location in the vocabulary space.
- [func enumerateNeighbors(for: String, maximumCount: Int, distanceType: NLDistanceType, using: (String, NLDistance) -> Bool)](./nlembedding/enumerateneighbors%28for,maximumcount,distancetype,using%29-72jda.md)
  Passes the nearest strings of a string in the vocabulary to a closure.
- [func enumerateNeighbors(for: [Double], maximumCount: Int, distanceType: NLDistanceType, using: (String, NLDistance) -> Bool)](./nlembedding/enumerateneighbors%28for,maximumcount,distancetype,using%29-6dy4x.md)
  Passes the nearest strings of a location in the vocabulary space to a closure.
- [func distance(between: String, and: String, distanceType: NLDistanceType) -> NLDistance](./nlembedding/distance%28between,and,distancetype%29.md)
  Calculates the distance between two strings in the vocabulary space.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nldistance)*