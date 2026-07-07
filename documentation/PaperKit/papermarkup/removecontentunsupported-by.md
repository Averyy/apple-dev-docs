# removeContentUnsupported(by:)

**Framework**: PaperKit  
**Kind**: method

Remove all contents that is not supported by the provided feature set.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
mutating func removeContentUnsupported(by featureSet: FeatureSet)
```

#### Discussion

After calling this method `featureSet.isSubset(of: features)` will be `true`.

## Parameters

- `featureSet`: The feature set to limit this data model to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkup/removecontentunsupported(by:))*