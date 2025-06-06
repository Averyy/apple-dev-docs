# contains(_:)

**Framework**: Create ML  
**Kind**: method

Returns a Boolean value indicating whether the vocabulary contains the given string.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func contains(_ text: String) -> Bool
```

#### Return Value

`true` if the string was found in the vocabulary; otherwise, false.

## Parameters

- `text`: The string to find in the vocabulary.

## See Also

- [func prediction(from: String, maxCount: Int, maxDistance: Double, distanceType: NLDistanceType) throws -> [(text: String, distance: Double)]](mlwordembedding/prediction(from:maxcount:maxdistance:distancetype:).md)
  Predicts neighbors.
- [func distance(between: String, and: String, distanceType: NLDistanceType) -> Double](mlwordembedding/distance(between:and:distancetype:).md)
  Calculates the distance between two strings in the vocabulary space.
- [enum NLDistanceType](../NaturalLanguage/NLDistanceType.md)
  The means of calculating a distance between two locations in a text embedding.
- [func vector(for: String) -> [Double]?](mlwordembedding/vector(for:).md)
  Accesses the vector associated with the given string in the vocabulary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordembedding/contains(_:))*