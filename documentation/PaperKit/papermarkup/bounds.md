# bounds

**Framework**: PaperKit  
**Kind**: property  
**Role**: Instance Property

The bounds of the paper.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var bounds: CGRect { get set }
```

## Discussion

The contents of the paper are positioned relative to its bounds.

## See Also

### Accessing elements
- [var subelements: MarkupOrderedSet](./subelements.md)
  The subelements of the paper markup.
- [var id: MarkupID<PaperMarkup>](./id.md)
  The unique identifier of the markup.
- [var contentsRenderFrame: CGRect](./contentsrenderframe.md)
  The frame that tightly fits the rendered contents on the paper.
- [var featureSet: FeatureSet](./featureset.md)
  The set of features used by this data model.
- [var indexableContent: String?](./indexablecontent.md)
- [var backgroundColor: CGColor?](./backgroundcolor.md)
  The background color of the paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkup/bounds)*