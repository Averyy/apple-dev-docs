# init(supportedFeatureSet:)

**Framework**: PaperKit  
**Kind**: init

Creates a markup toolbar view controller.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency init(supportedFeatureSet: FeatureSet)
```

#### Discussion

The feature set limits the tools / actions a person can access from this toolbar. Also set `supportedFeatureSet` on any `PaperMarkupViewController` you use.

## Parameters

- `supportedFeatureSet`: The supported features of this toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuptoolbarviewcontroller/init(supportedfeatureset:))*