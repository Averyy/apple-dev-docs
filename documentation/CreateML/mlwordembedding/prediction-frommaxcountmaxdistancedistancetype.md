# prediction(from:maxCount:maxDistance:distanceType:)

**Framework**: Create ML  
**Kind**: method

Predicts neighbors.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func prediction(from text: String, maxCount: Int = 10, maxDistance: Double = 2.0, distanceType: NLDistanceType = .cosine) throws -> [(text: String, distance: Double)]
```

#### Return Value

An array of neighboring strings and their distances to the input string.

#### Discussion

The distance values are calculated with a formula determined by [`NLDistanceType`](https://developer.apple.com/documentation/NaturalLanguage/NLDistanceType), such as [`NLDistanceType.cosine`](https://developer.apple.com/documentation/NaturalLanguage/NLDistanceType/cosine).

## Parameters

- `text`: A string in the embedding vocabulary.
- `maxCount`: The largest number of neighboring strings.
- `maxDistance`: The maximum allowed neighbor distance.
- `distanceType`: The type of distance formula to use for evaluating a neighbor’s distance from the input string.

## See Also

- [func distance(between: String, and: String, distanceType: NLDistanceType) -> Double](mlwordembedding/distance(between:and:distancetype:).md)
  Calculates the distance between two strings in the vocabulary space.
- [enum NLDistanceType](../NaturalLanguage/NLDistanceType.md)
  The means of calculating a distance between two locations in a text embedding.
- [func contains(String) -> Bool](mlwordembedding/contains(_:).md)
  Returns a Boolean value indicating whether the vocabulary contains the given string.
- [func vector(for: String) -> [Double]?](mlwordembedding/vector(for:).md)
  Accesses the vector associated with the given string in the vocabulary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordembedding/prediction(from:maxcount:maxdistance:distancetype:))*