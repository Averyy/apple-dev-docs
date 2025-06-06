# representedElementCategory

**Framework**: AppKit  
**Kind**: property

The type of the element.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var representedElementCategory: NSCollectionElementCategory { get }
```

#### Discussion

Use this property to distinguish whether the layout attributes apply to an item, a supplementary view, a decoration view, or another type of element presented by the collection view.

## See Also

- [var indexPath: IndexPath?](nscollectionviewlayoutattributes/indexpath.md)
  The index path of the element.
- [var representedElementKind: String?](nscollectionviewlayoutattributes/representedelementkind.md)
  The identifier for specific elements of your collection view interface.
- [class let elementKindInterItemGapIndicator: String](nscollectionview/elementkindinteritemgapindicator.md)
  The element kind string assigned to the attributes object when it represents an inter-item gap.
- [class let elementKindSectionFooter: String](nscollectionview/elementkindsectionfooter.md)
  A supplementary view that acts as a footer for a given section.
- [class let elementKindSectionHeader: String](nscollectionview/elementkindsectionheader.md)
  A supplementary view that acts as a header for a given section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutattributes/representedelementcategory)*