# representedElementKind

**Framework**: AppKit  
**Kind**: property

The identifier for specific elements of your collection view interface.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var representedElementKind: String? { get }
```

#### Discussion

For supplementary and decoration views, you use this string to distinguish between views in a given section. You also use this string to identify the intended purpose of the view in your collection view interface.

When the value of the [`representedElementCategory`](nscollectionviewlayoutattributes/representedelementcategory.md) property is [`NSCollectionElementCategory.item`](nscollectionelementcategory/item.md), this property is `nil`.

## See Also

- [var representedElementCategory: NSCollectionElementCategory](nscollectionviewlayoutattributes/representedelementcategory.md)
  The type of the element.
- [var indexPath: IndexPath?](nscollectionviewlayoutattributes/indexpath.md)
  The index path of the element.
- [class let elementKindInterItemGapIndicator: String](nscollectionview/elementkindinteritemgapindicator.md)
  The element kind string assigned to the attributes object when it represents an inter-item gap.
- [class let elementKindSectionFooter: String](nscollectionview/elementkindsectionfooter.md)
  A supplementary view that acts as a footer for a given section.
- [class let elementKindSectionHeader: String](nscollectionview/elementkindsectionheader.md)
  A supplementary view that acts as a header for a given section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutattributes/representedelementkind)*