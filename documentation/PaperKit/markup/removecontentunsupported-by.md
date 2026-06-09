# removeContentUnsupported(by:)

**Framework**: PaperKit  
**Kind**: method  
**Required**: Yes

Removes all content not supported by the provided feature set.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func removeContentUnsupported(by featureSet: FeatureSet) -> Bool
```

#### Return Value

True if this was successful and the feature set is now supported.

#### Discussion

If the returned value is `true` then `self.featureSet.isSubset(of: featureSet)` will be `true`.

## Parameters

- `featureSet`: The feature set to limit this markup to.

## See Also

- [var featureSet: FeatureSet](markup/featureset.md)
  The set of features used by this markup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markup/removecontentunsupported(by:))*