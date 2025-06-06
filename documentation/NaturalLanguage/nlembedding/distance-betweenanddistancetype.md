# distance(between:and:distanceType:)

**Framework**: Natural Language  
**Kind**: method

Calculates the distance between two strings in the vocabulary space.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@nonobjc
func distance(between firstString: String, and secondString: String, distanceType: NLDistanceType = .cosine) -> NLDistance
```

#### Return Value

The distance associated with `distanceType`.

## Parameters

- `firstString`: A string in the embedding vocabulary.
- `secondString`: Another string in the embedding vocabulary.
- `distanceType`: A means of calculating distance that determines which formula the method uses to evaluate the distance between   and  .

## See Also

- [func neighbors(for: String, maximumCount: Int, distanceType: NLDistanceType) -> [(String, NLDistance)]](nlembedding/neighbors(for:maximumcount:distancetype:)-8f1jc.md)
  Retrieves a limited number of strings near a string in the vocabulary.
- [func neighbors(for: [Double], maximumCount: Int, distanceType: NLDistanceType) -> [(String, NLDistance)]](nlembedding/neighbors(for:maximumcount:distancetype:)-8lp4z.md)
  Retrieves a limited number of strings near a location in the vocabulary space.
- [func enumerateNeighbors(for: String, maximumCount: Int, distanceType: NLDistanceType, using: (String, NLDistance) -> Bool)](nlembedding/enumerateneighbors(for:maximumcount:distancetype:using:)-72jda.md)
  Passes the nearest strings of a string in the vocabulary to a closure.
- [func enumerateNeighbors(for: [Double], maximumCount: Int, distanceType: NLDistanceType, using: (String, NLDistance) -> Bool)](nlembedding/enumerateneighbors(for:maximumcount:distancetype:using:)-6dy4x.md)
  Passes the nearest strings of a location in the vocabulary space to a closure.
- [typealias NLDistance](nldistance.md)
  The distance between two strings in a text embedding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlembedding/distance(between:and:distancetype:))*