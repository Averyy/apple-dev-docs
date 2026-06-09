# remove(_:)

**Framework**: PaperKit  
**Kind**: method

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

- [func contains(FeatureSet.Feature) -> Bool](featureset/contains(_:).md)
  Returns a Boolean value that indicates whether the given feature exists in the set.
- [func isSubset(of: FeatureSet) -> Bool](featureset/issubset(of:).md)
  Returns a Boolean value that indicates whether this feature set is a subset of the given feature set.
- [func insert(FeatureSet.Feature)](featureset/insert(_:).md)
  Inserts the given feature in the set if it is not already present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/featureset/remove(_:))*