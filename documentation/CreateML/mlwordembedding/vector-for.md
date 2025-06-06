# vector(for:)

**Framework**: Create ML  
**Kind**: method

Accesses the vector associated with the given string in the vocabulary.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func vector(for text: String) -> [Double]?
```

#### Return Value

The vector associated with the string if present in the word embedding; otherwise, `nil`.

## Parameters

- `text`: A string in the vocabulary.

## See Also

- [func prediction(from: String, maxCount: Int, maxDistance: Double, distanceType: NLDistanceType) throws -> [(text: String, distance: Double)]](mlwordembedding/prediction(from:maxcount:maxdistance:distancetype:).md)
  Predicts neighbors.
- [func distance(between: String, and: String, distanceType: NLDistanceType) -> Double](mlwordembedding/distance(between:and:distancetype:).md)
  Calculates the distance between two strings in the vocabulary space.
- [enum NLDistanceType](../NaturalLanguage/NLDistanceType.md)
  The means of calculating a distance between two locations in a text embedding.
- [func contains(String) -> Bool](mlwordembedding/contains(_:).md)
  Returns a Boolean value indicating whether the vocabulary contains the given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordembedding/vector(for:))*