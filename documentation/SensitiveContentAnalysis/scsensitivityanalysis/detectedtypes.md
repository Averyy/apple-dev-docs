# detectedTypes

**Framework**: Sensitive Content Analysis  
**Kind**: property

A property that contains the categories of sensitive content that analysis detects.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var detectedTypes: Set<SCSensitivityAnalysis.ContentType> { get }
```

## Mentions

- [Detecting sensitive content in media and providing intervention options](detecting-nudity-in-media-and-providing-intervention-options.md)
- [Testing your app’s response to sensitive media](testing-your-app-s-response-to-sensitive-media.md)

#### Discussion

The Sensitive Content Analysis framework sets this property when analysis determines that media contains sensitive content. Check this property to determine the specific types of sensitive content, such as [`sexuallyExplicit`](scsensitivityanalysis/contenttype/sexuallyexplicit.md) or [`goreOrViolence`](scsensitivityanalysis/contenttype/goreorviolence.md). The framework populates this set only when [`isSensitive`](scsensitivityanalysis/issensitive.md) is `true`.

For example, the following code checks for specific content types after determining that media is sensitive:

```swift
let analysis = try await analyzer.analyzeImage(at: imageURL)

guard analysis.isSensitive else {
    displayContent(imageURL)
    return
}

// Check for specific harm types.
let detectedTypes = analysis.detectedTypes

if detectedTypes.contains(.sexuallyExplicit) {
    showContentWarning(
        message: "This image may contain nudity.",
        allowAccess: true
    )
}

if detectedTypes.contains(.goreOrViolence) {
    blockContent(
        message: "This image may contain violence or gore.",
        offerResources: true
    )
}
```

## See Also

- [SCSensitivityAnalysis.ContentType](scsensitivityanalysis/contenttype.md)
  A type that identifies a category of sensitive content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scsensitivityanalysis/detectedtypes)*