# contains(_:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

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

### Testing a word embedding
- [func prediction(from: String, maxCount: Int, maxDistance: Double, distanceType: NLDistanceType) throws -> [(text: String, distance: Double)]](./prediction%28from,maxcount,maxdistance,distancetype%29.md)
  Predicts neighbors.
- [func distance(between: String, and: String, distanceType: NLDistanceType) -> Double](./distance%28between,and,distancetype%29.md)
  Calculates the distance between two strings in the vocabulary space.
- [enum NLDistanceType](../../NaturalLanguage/nldistancetype.md)
  The means of calculating a distance between two locations in a text embedding.
- [func vector(for: String) -> [Double]?](./vector%28for%29.md)
  Accesses the vector associated with the given string in the vocabulary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordembedding/contains(_:))*