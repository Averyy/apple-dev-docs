# UICollectionLayoutListConfiguration.FooterMode.supplementary

**Framework**: UIKit  
**Kind**: case

A footer mode that uses supplementary views to show footers.

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

Choose this footer mode to use supplementary views with [`elementKindSectionFooter`](uicollectionview/elementkindsectionfooter.md) as the section footer.

By default, lists that use the [`UICollectionLayoutListConfiguration.Appearance.plain`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/plain.md) and [`UICollectionLayoutListConfiguration.Appearance.sidebarPlain`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebarplain.md) list appearances use pinned footers. You must use this footer mode if you want to opt into this default pinning behavior.

## See Also

- [UICollectionLayoutListConfiguration.FooterMode.none](uicollectionlayoutlistconfiguration-swift.struct/footermode-swift.enum/none.md)
  No footers are shown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionlayoutlistconfiguration-swift.struct/footermode-swift.enum/supplementary)*