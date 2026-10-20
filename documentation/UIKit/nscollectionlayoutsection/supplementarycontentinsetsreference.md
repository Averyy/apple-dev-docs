# supplementaryContentInsetsReference

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The reference boundary for content insets on boundary supplementary items.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var supplementaryContentInsetsReference: UIContentInsetsReference { get set }
```

```objc
@property (nonatomic) UIContentInsetsReference supplementaryContentInsetsReference;
```

#### Discussion

This property represents the reference boundary to use when defining [`contentInsets`](../nscollectionlayoutitem/contentinsets.md) on [`NSCollectionLayoutBoundarySupplementaryItem`](../nscollectionlayoutboundarysupplementaryitem.md) objects.

The default value of this property is [`UIContentInsetsReference.automatic`](../uicontentinsetsreference/automatic.md), which means any insets specified on a [`NSCollectionLayoutBoundarySupplementaryItem`](../nscollectionlayoutboundarysupplementaryitem.md) follow the layout configuration’s [`contentInsetsReference`](../uicollectionviewcompositionallayoutconfiguration/contentinsetsreference.md).

## See Also

### Configuring section spacing
- [var interGroupSpacing: CGFloat](./intergroupspacing.md)
  The amount of space between the groups in the section.
- [var contentInsets: NSDirectionalEdgeInsets](./contentinsets.md)
  The amount of space between the content of the section and its boundaries.
- [var contentInsetsReference: UIContentInsetsReference](./contentinsetsreference.md)
  The boundary to reference when defining content insets.
- [enum UIContentInsetsReference](../uicontentinsetsreference.md)
  Constants that describe the reference point of the content insets.
- [var supplementariesFollowContentInsets: Bool](./supplementariesfollowcontentinsets.md)
  A Boolean value that indicates whether the section’s supplementary items follow the specified content insets for the section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutsection/supplementarycontentinsetsreference)*