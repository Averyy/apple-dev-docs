# UICollectionLayoutListHeaderModeSupplementary

**Framework**: UIKit  
**Kind**: case  
**Role**: Enumeration Case

A header mode that uses supplementary views to show headers.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```c
UICollectionLayoutListHeaderModeSupplementary
```

#### Discussion

Choose this header mode to use supplementary views with [`elementKindSectionHeader`](../uicollectionview/elementkindsectionheader.md) as the section header.

By default, lists that use the [`UICollectionLayoutListAppearancePlain`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearanceplain.md) and [`UICollectionLayoutListAppearanceSidebarPlain`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebarplain.md) list appearances use pinned headers. You must use this header mode if you want to opt into this default pinning behavior.

## See Also

### Header modes
- [UICollectionLayoutListHeaderModeNone](./uicollectionlayoutlistheadermodenone.md)
  No headers are shown.
- [UICollectionLayoutListHeaderModeFirstItemInSection](./uicollectionlayoutlistheadermodefirstiteminsection.md)
  A header mode that styles the first item in a section as a header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistheadermode/uicollectionlayoutlistheadermodesupplementary)*