# latest

**Framework**: PaperKit  
**Kind**: property

A new feature set supporting all features.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static var latest: FeatureSet { get }
```

#### Discussion

To automatically get the latest features that PaperKit adds in new releases use `.latest`, to avoid new releases adding unexpected functionality to your app use a specific version like `.version1`.

## See Also

- [static var version1: FeatureSet](featureset/version1.md)
  A new feature set supporting all features in version 1.
- [static var empty: FeatureSet](featureset/empty.md)
  A maximally empty feature set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/featureset/latest)*