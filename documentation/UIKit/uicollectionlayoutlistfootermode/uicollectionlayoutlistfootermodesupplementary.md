# UICollectionLayoutListFooterModeSupplementary

**Framework**: UIKit  
**Kind**: case  
**Role**: Enumeration Case

A footer mode that uses supplementary views to show footers.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```c
UICollectionLayoutListFooterModeSupplementary
```

## Discussion

Choose this footer mode to use supplementary views with [`elementKindSectionFooter`](../uicollectionview/elementkindsectionfooter.md) as the section footer.

By default, lists that use the [`UICollectionLayoutListAppearancePlain`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearanceplain.md) and [`UICollectionLayoutListAppearanceSidebarPlain`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebarplain.md) list appearances use pinned footers. You must use this footer mode if you want to opt into this default pinning behavior.

## See Also

### Footer modes
- [UICollectionLayoutListFooterModeNone](./uicollectionlayoutlistfootermodenone.md)
  No footers are shown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistfootermode/uicollectionlayoutlistfootermodesupplementary)*