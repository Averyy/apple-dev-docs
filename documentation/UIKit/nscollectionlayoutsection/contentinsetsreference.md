# contentInsetsReference

**Framework**: UIKit  
**Kind**: property

The boundary to reference when defining content insets.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var contentInsetsReference: UIContentInsetsReference { get set }
```

#### Discussion

This property represents the reference point to use when defining [`contentInsets`](nscollectionlayoutsection/contentinsets.md).

The default value of this property is [`UIContentInsetsReference.automatic`](uicontentinsetsreference/automatic.md), which means the section follows the layout configuration’s [`contentInsetsReference`](uicollectionviewcompositionallayoutconfiguration/contentinsetsreference.md).

## See Also

- [var interGroupSpacing: CGFloat](nscollectionlayoutsection/intergroupspacing.md)
  The amount of space between the groups in the section.
- [var contentInsets: NSDirectionalEdgeInsets](nscollectionlayoutsection/contentinsets.md)
  The amount of space between the content of the section and its boundaries.
- [var supplementaryContentInsetsReference: UIContentInsetsReference](nscollectionlayoutsection/supplementarycontentinsetsreference.md)
  The reference boundary for content insets on boundary supplementary items.
- [enum UIContentInsetsReference](uicontentinsetsreference.md)
  Constants that describe the reference point of the content insets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutsection/contentinsetsreference)*