# remove(_:)

**Framework**: PaperKit  
**Kind**: method  
**Role**: Instance Method

Removes the given feature.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
mutating func remove(_ feature: FeatureSet.Feature)
```

## Parameters

- `feature`: The feature to remove from the set.

## See Also

### Checking features
- [func contains(FeatureSet.Feature) -> Bool](./contains%28_%29.md)
  Returns a Boolean value that indicates whether the given feature exists in the set.
- [func isSubset(of: FeatureSet) -> Bool](./issubset%28of%29.md)
  Returns a Boolean value that indicates whether this feature set is a subset of the given feature set.
- [func insert(FeatureSet.Feature)](./insert%28_%29.md)
  Inserts the given feature in the set if it is not already present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/featureset/remove(_:))*