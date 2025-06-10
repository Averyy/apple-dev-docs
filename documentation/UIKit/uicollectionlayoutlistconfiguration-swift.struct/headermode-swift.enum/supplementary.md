# UICollectionLayoutListConfiguration.HeaderMode.supplementary

**Framework**: UIKit  
**Kind**: case

A header mode that uses supplementary views to show headers.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
case supplementary
```

#### Discussion

Choose this header mode to use supplementary views with [`elementKindSectionHeader`](uicollectionview/elementkindsectionheader.md) as the section header.

By default, lists that use the [`UICollectionLayoutListConfiguration.Appearance.plain`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/plain.md) and [`UICollectionLayoutListConfiguration.Appearance.sidebarPlain`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebarplain.md) list appearances use pinned headers. You must use this header mode if you want to opt into this default pinning behavior.

## See Also

- [UICollectionLayoutListConfiguration.HeaderMode.none](uicollectionlayoutlistconfiguration-swift.struct/headermode-swift.enum/none.md)
  No headers are shown.
- [UICollectionLayoutListConfiguration.HeaderMode.firstItemInSection](uicollectionlayoutlistconfiguration-swift.struct/headermode-swift.enum/firstiteminsection.md)
  A header mode that styles the first item in a section as a header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/headermode-swift.enum/supplementary)*