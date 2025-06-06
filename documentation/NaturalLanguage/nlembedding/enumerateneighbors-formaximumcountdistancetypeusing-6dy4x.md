# enumerateNeighbors(for:maximumCount:distanceType:using:)

**Framework**: Natural Language  
**Kind**: method

Passes the nearest strings of a location in the vocabulary space to a closure.

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
func enumerateNeighbors(for vector: [Double], maximumCount maxCount: Int, distanceType: NLDistanceType = .cosine, using block: (String, NLDistance) -> Bool)
```

## Parameters

- `vector`: A location in the vocabulary space.
- `maxCount`: The largest number of times the method calls  .
- `distanceType`: A means of calculating distance that determines which formula the method uses to evaluate a neighbor’s distance from  .
- `block`: The closure returns a Boolean that indicates whether to stop enumerating neighbors.

## See Also

- [func neighbors(for: String, maximumCount: Int, distanceType: NLDistanceType) -> [(String, NLDistance)]](nlembedding/neighbors(for:maximumcount:distancetype:)-8f1jc.md)
  Retrieves a limited number of strings near a string in the vocabulary.
- [func neighbors(for: [Double], maximumCount: Int, distanceType: NLDistanceType) -> [(String, NLDistance)]](nlembedding/neighbors(for:maximumcount:distancetype:)-8lp4z.md)
  Retrieves a limited number of strings near a location in the vocabulary space.
- [func enumerateNeighbors(for: String, maximumCount: Int, distanceType: NLDistanceType, using: (String, NLDistance) -> Bool)](nlembedding/enumerateneighbors(for:maximumcount:distancetype:using:)-72jda.md)
  Passes the nearest strings of a string in the vocabulary to a closure.
- [func distance(between: String, and: String, distanceType: NLDistanceType) -> NLDistance](nlembedding/distance(between:and:distancetype:).md)
  Calculates the distance between two strings in the vocabulary space.
- [typealias NLDistance](nldistance.md)
  The distance between two strings in a text embedding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlembedding/enumerateneighbors(for:maximumcount:distancetype:using:)-6dy4x)*