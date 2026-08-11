# contentsRenderFrame

**Framework**: PaperKit  
**Kind**: property

The frame that tightly fits the rendered contents on the paper.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var contentsRenderFrame: CGRect { get }
```

#### Discussion

This frame includes padding around `contentsFrame` to ensure it includes all the rendered aspects of the content. For example, this frame will include the strokes, and shadows of any contents.

## See Also

- [var subelements: MarkupOrderedSet](papermarkup/subelements.md)
  The subelements of the paper markup.
- [var id: MarkupID<PaperMarkup>](papermarkup/id.md)
  The unique identifier of the markup.
- [var bounds: CGRect](papermarkup/bounds.md)
  The bounds of the paper.
- [var featureSet: FeatureSet](papermarkup/featureset.md)
  The set of features used by this data model.
- [var indexableContent: String?](papermarkup/indexablecontent.md)
- [var backgroundColor: CGColor?](papermarkup/backgroundcolor.md)
  The background color of the paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkup/contentsrenderframe)*