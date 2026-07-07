# init(supportedFeatureSet:additionalActions:)

**Framework**: PaperKit  
**Kind**: init

Creates a markup edit view controller.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency init(supportedFeatureSet: FeatureSet, additionalActions: [UIMenuElement] = [])
```

#### Discussion

`MarkupEditViewController` provides a standard interface for adding to and editing content in a `PaperMarkupViewController`.

## Parameters

- `supportedFeatureSet`: The features to create actions for.
- `additionalActions`: The array of additional actions to provide from the insertion UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupeditviewcontroller/init(supportedfeatureset:additionalactions:))*