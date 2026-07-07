# version1

**Framework**: PaperKit  
**Kind**: property

A new feature set supporting all features in version 1.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static var version1: FeatureSet { get }
```

#### Discussion

To automatically get the latest features that PaperKit adds in new releases use `.latest`, to avoid new releases adding unexpected functionality to your app use a specific version like `.version1`.

## See Also

- [static var version2: FeatureSet](featureset/version2.md)
  A new feature set supporting all features in version 2.
- [static var latest: FeatureSet](featureset/latest.md)
  A new feature set supporting all features.
- [static var empty: FeatureSet](featureset/empty.md)
  A maximally empty feature set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/featureset/version1)*