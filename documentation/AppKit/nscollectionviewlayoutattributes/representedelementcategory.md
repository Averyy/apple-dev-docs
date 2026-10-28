# representedElementCategory

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The type of the element.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var representedElementCategory: NSCollectionElementCategory { get }
```

```objc
@property (readonly) NSCollectionElementCategory representedElementCategory;
```

## Discussion

Use this property to distinguish whether the layout attributes apply to an item, a supplementary view, a decoration view, or another type of element presented by the collection view.

## See Also

### Identifying the Element
- [var indexPath: IndexPath?](./indexpath.md)
  The index path of the element.
- [var representedElementKind: String?](./representedelementkind.md)
  The identifier for specific elements of your collection view interface.
- [class let elementKindInterItemGapIndicator: String](../nscollectionview/elementkindinteritemgapindicator.md)
  The element kind string assigned to the attributes object when it represents an inter-item gap.
- [class let elementKindSectionFooter: String](../nscollectionview/elementkindsectionfooter.md)
  A supplementary view that acts as a footer for a given section.
- [class let elementKindSectionHeader: String](../nscollectionview/elementkindsectionheader.md)
  A supplementary view that acts as a header for a given section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutattributes/representedelementcategory)*