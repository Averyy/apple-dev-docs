# distance(between:and:distanceType:)

**Framework**: Create ML  
**Kind**: method

Calculates the distance between two strings in the vocabulary space.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func distance(between first: String, and second: String, distanceType: NLDistanceType = .cosine) -> Double
```

#### Return Value

The distance

## Parameters

- `first`: A string in the embedding vocabulary.
- `second`: Another string in the embedding vocabulary.
- `distanceType`: The metric to use to calculate the distance between the first and second strings.

## See Also

- [func prediction(from: String, maxCount: Int, maxDistance: Double, distanceType: NLDistanceType) throws -> [(text: String, distance: Double)]](mlwordembedding/prediction(from:maxcount:maxdistance:distancetype:).md)
  Predicts neighbors.
- [enum NLDistanceType](../NaturalLanguage/NLDistanceType.md)
  The means of calculating a distance between two locations in a text embedding.
- [func contains(String) -> Bool](mlwordembedding/contains(_:).md)
  Returns a Boolean value indicating whether the vocabulary contains the given string.
- [func vector(for: String) -> [Double]?](mlwordembedding/vector(for:).md)
  Accesses the vector associated with the given string in the vocabulary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordembedding/distance(between:and:distancetype:))*