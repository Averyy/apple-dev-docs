# vector(for:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

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

### Testing a word embedding
- [func prediction(from: String, maxCount: Int, maxDistance: Double, distanceType: NLDistanceType) throws -> [(text: String, distance: Double)]](./prediction%28from,maxcount,maxdistance,distancetype%29.md)
  Predicts neighbors.
- [func distance(between: String, and: String, distanceType: NLDistanceType) -> Double](./distance%28between,and,distancetype%29.md)
  Calculates the distance between two strings in the vocabulary space.
- [enum NLDistanceType](../../NaturalLanguage/nldistancetype.md)
  The means of calculating a distance between two locations in a text embedding.
- [func contains(String) -> Bool](./contains%28_%29.md)
  Returns a Boolean value indicating whether the vocabulary contains the given string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordembedding/vector(for:))*