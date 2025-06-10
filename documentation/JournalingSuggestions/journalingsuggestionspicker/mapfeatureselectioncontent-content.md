# mapFeatureSelectionContent(content:)

**Framework**: Journaling Suggestions  
**Kind**: method

Specifies a custom presentation for the currently selected feature.

**Availability**:
- iOS 17.0+

## Declaration

```swift
@MainActor
@preconcurrency func mapFeatureSelectionContent(@MapContentBuilder content: @escaping (MapFeature) -> some MapContent) -> some View
```

#### Discussion

The supported presentation options are `Annotation`, and `Marker`. Other types of map content will be ignored and handled as though no content was returned.

If empty map content is returned, the system presentation will be used.

## Parameters

- `content`: Generates the custom presentation for a given map feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/mapfeatureselectioncontent(content:))*