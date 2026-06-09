# version2

**Framework**: PaperKit  
**Kind**: property

A new feature set supporting all features in version 2.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static var version2: FeatureSet { get }
```

#### Discussion

To automatically get the latest features that PaperKit adds in new releases use `.latest`, to avoid new releases adding unexpected functionality to your app use a specific version like `.version2`.

## See Also

- [static var version1: FeatureSet](featureset/version1.md)
  A new feature set supporting all features in version 1.
- [static var latest: FeatureSet](featureset/latest.md)
  A new feature set supporting all features.
- [static var empty: FeatureSet](featureset/empty.md)
  A maximally empty feature set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/featureset/version2)*