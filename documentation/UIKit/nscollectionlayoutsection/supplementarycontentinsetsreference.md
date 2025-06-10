# supplementaryContentInsetsReference

**Framework**: UIKit  
**Kind**: property

The reference boundary for content insets on boundary supplementary items.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var supplementaryContentInsetsReference: UIContentInsetsReference { get set }
```

#### Discussion

This property represents the reference boundary to use when defining [`contentInsets`](nscollectionlayoutitem/contentinsets.md) on [`NSCollectionLayoutBoundarySupplementaryItem`](nscollectionlayoutboundarysupplementaryitem.md) objects.

The default value of this property is [`UIContentInsetsReference.automatic`](uicontentinsetsreference/automatic.md), which means any insets specified on a [`NSCollectionLayoutBoundarySupplementaryItem`](nscollectionlayoutboundarysupplementaryitem.md) follow the layout configuration’s [`contentInsetsReference`](uicollectionviewcompositionallayoutconfiguration/contentinsetsreference.md).

## See Also

- [var interGroupSpacing: CGFloat](nscollectionlayoutsection/intergroupspacing.md)
  The amount of space between the groups in the section.
- [var contentInsets: NSDirectionalEdgeInsets](nscollectionlayoutsection/contentinsets.md)
  The amount of space between the content of the section and its boundaries.
- [var contentInsetsReference: UIContentInsetsReference](nscollectionlayoutsection/contentinsetsreference.md)
  The boundary to reference when defining content insets.
- [enum UIContentInsetsReference](uicontentinsetsreference.md)
  Constants that describe the reference point of the content insets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutsection/supplementarycontentinsetsreference)*