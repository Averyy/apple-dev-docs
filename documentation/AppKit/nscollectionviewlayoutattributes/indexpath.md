# indexPath

**Framework**: AppKit  
**Kind**: property

The index path of the element.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var indexPath: IndexPath? { get set }
```

#### Discussion

Use the index path to locate information about the item in your app’s data structures. For supplementary and decoration views, you must also use the [`representedElementKind`](nscollectionviewlayoutattributes/representedelementkind.md) property to identify the element.

## See Also

- [var representedElementCategory: NSCollectionElementCategory](nscollectionviewlayoutattributes/representedelementcategory.md)
  The type of the element.
- [var representedElementKind: String?](nscollectionviewlayoutattributes/representedelementkind.md)
  The identifier for specific elements of your collection view interface.
- [class let elementKindInterItemGapIndicator: String](nscollectionview/elementkindinteritemgapindicator.md)
  The element kind string assigned to the attributes object when it represents an inter-item gap.
- [class let elementKindSectionFooter: String](nscollectionview/elementkindsectionfooter.md)
  A supplementary view that acts as a footer for a given section.
- [class let elementKindSectionHeader: String](nscollectionview/elementkindsectionheader.md)
  A supplementary view that acts as a header for a given section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutattributes/indexpath)*