# UICollectionLayoutListConfiguration.HeaderMode.firstItemInSection

**Framework**: UIKit  
**Kind**: case

A header mode that styles the first item in a section as a header.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
case firstItemInSection
```

#### Discussion

Choose this header mode when you’re using hierarchical data sources if you want to be able to expand and collapse the header.

When you use this header mode, a [`UICollectionViewListCell`](uicollectionviewlistcell.md) object that appears as the first item in the section automatically uses a header appearance. When you configure your data source, make sure to account for the fact that the first item in the section (at index `0`) represents the header, and the actual items in the section start at index `1`.

By default, lists that use the [`UICollectionLayoutListConfiguration.Appearance.plain`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/plain.md) and [`UICollectionLayoutListConfiguration.Appearance.sidebarPlain`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebarplain.md) list appearances use pinned headers. If you want to opt into this default pinning behavior, use the [`UICollectionLayoutListConfiguration.HeaderMode.supplementary`](uicollectionlayoutlistconfiguration-swift.struct/headermode-swift.enum/supplementary.md) header mode instead.

## See Also

- [UICollectionLayoutListConfiguration.HeaderMode.none](uicollectionlayoutlistconfiguration-swift.struct/headermode-swift.enum/none.md)
  No headers are shown.
- [UICollectionLayoutListConfiguration.HeaderMode.supplementary](uicollectionlayoutlistconfiguration-swift.struct/headermode-swift.enum/supplementary.md)
  A header mode that uses supplementary views to show headers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/headermode-swift.enum/firstiteminsection)*