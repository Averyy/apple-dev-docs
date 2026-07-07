# insert(_:)

**Framework**: PaperKit  
**Kind**: method

Inserts the given feature in the set if it is not already present.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
mutating func insert(_ newFeature: FeatureSet.Feature)
```

## Parameters

- `newFeature`: A feature to insert into the set.

## See Also

- [func contains(FeatureSet.Feature) -> Bool](featureset/contains(_:).md)
  Returns a Boolean value that indicates whether the given feature exists in the set.
- [func isSubset(of: FeatureSet) -> Bool](featureset/issubset(of:).md)
  Returns a Boolean value that indicates whether this feature set is a subset of the given feature set.
- [func remove(FeatureSet.Feature)](featureset/remove(_:).md)
  Removes the given feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/featureset/insert(_:))*