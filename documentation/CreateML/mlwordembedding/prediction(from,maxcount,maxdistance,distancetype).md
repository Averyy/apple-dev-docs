# prediction(from:maxCount:maxDistance:distanceType:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Predicts neighbors.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func prediction(from text: String, maxCount: Int = 10, maxDistance: Double = 2.0, distanceType: NLDistanceType = .cosine) throws -> [(text: String, distance: Double)]
```

## Return Value

An array of neighboring strings and their distances to the input string.

## Discussion

The distance values are calculated with a formula determined by [`NLDistanceType`](../../NaturalLanguage/nldistancetype.md), such as [`NLDistanceType.cosine`](../../NaturalLanguage/nldistancetype/cosine.md).

## Parameters

- `text`: A string in the embedding vocabulary.
- `maxCount`: The largest number of neighboring strings.
- `maxDistance`: The maximum allowed neighbor distance.
- `distanceType`: The type of distance formula to use for evaluating a neighbor’s distance from the input string.

## See Also

### Testing a word embedding
- [func distance(between: String, and: String, distanceType: NLDistanceType) -> Double](./distance%28between,and,distancetype%29.md)
  Calculates the distance between two strings in the vocabulary space.
- [enum NLDistanceType](../../NaturalLanguage/nldistancetype.md)
  The means of calculating a distance between two locations in a text embedding.
- [func contains(String) -> Bool](./contains%28_%29.md)
  Returns a Boolean value indicating whether the vocabulary contains the given string.
- [func vector(for: String) -> [Double]?](./vector%28for%29.md)
  Accesses the vector associated with the given string in the vocabulary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordembedding/prediction(from:maxcount:maxdistance:distancetype:))*