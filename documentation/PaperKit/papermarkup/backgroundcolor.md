# backgroundColor

**Framework**: PaperKit  
**Kind**: property  
**Role**: Instance Property

The background color of the paper.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var backgroundColor: CGColor? { get set }
```

#### Discussion

Default is `nil`, which uses a default color based on the current user interface style.

## See Also

### Accessing elements
- [var subelements: MarkupOrderedSet](./subelements.md)
  The subelements of the paper markup.
- [var id: MarkupID<PaperMarkup>](./id.md)
  The unique identifier of the markup.
- [var bounds: CGRect](./bounds.md)
  The bounds of the paper.
- [var contentsRenderFrame: CGRect](./contentsrenderframe.md)
  The frame that tightly fits the rendered contents on the paper.
- [var featureSet: FeatureSet](./featureset.md)
  The set of features used by this data model.
- [var indexableContent: String?](./indexablecontent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkup/backgroundcolor)*