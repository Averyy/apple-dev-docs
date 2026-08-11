# contains(_:)

**Framework**: PaperKit  
**Kind**: method

Returns a Boolean value that indicates whether the given feature exists in the set.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func contains(_ feature: FeatureSet.Feature) -> Bool
```

#### Return Value

`true` if member exists in the set; otherwise, `false`.

## Parameters

- `feature`: A feature to look for in the set.

## See Also

- [func isSubset(of: FeatureSet) -> Bool](featureset/issubset(of:).md)
  Returns a Boolean value that indicates whether this feature set is a subset of the given feature set.
- [func insert(FeatureSet.Feature)](featureset/insert(_:).md)
  Inserts the given feature in the set if it is not already present.
- [func remove(FeatureSet.Feature)](featureset/remove(_:).md)
  Removes the given feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/featureset/contains(_:))*