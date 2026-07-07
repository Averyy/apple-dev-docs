# isSubset(of:)

**Framework**: PaperKit  
**Kind**: method

Returns a Boolean value that indicates whether this feature set is a subset of the given feature set.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func isSubset(of other: FeatureSet) -> Bool
```

#### Return Value

`true` if the feature set is a subset of `other`; otherwise, `false`.

## Parameters

- `other`: Another feature set.

## See Also

- [func contains(FeatureSet.Feature) -> Bool](featureset/contains(_:).md)
  Returns a Boolean value that indicates whether the given feature exists in the set.
- [func insert(FeatureSet.Feature)](featureset/insert(_:).md)
  Inserts the given feature in the set if it is not already present.
- [func remove(FeatureSet.Feature)](featureset/remove(_:).md)
  Removes the given feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/featureset/issubset(of:))*