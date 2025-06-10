# init(markup:supportedFeatureSet:)

**Framework**: PaperKit  
**Kind**: init

Create a new `PaperMarkupViewController` with the provided data model.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency init(markup: PaperMarkup? = nil, supportedFeatureSet: FeatureSet)
```

#### Discussion

The canvas limits the edits that a person can make so they’re compatible with the feature set specified. If you set a `supportedFeatureSet`, also use a similar feature set to configure any `MarkupToolbarViewController` or `MarkupEditViewController` you use.

## Parameters

- `markup`: The data model to show on this canvas.   The default value is  .
- `supportedFeatureSet`: The supported features of this toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/init(markup:supportedfeatureset:))*