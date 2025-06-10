# UIContentInsetsReference

**Framework**: UIKit  
**Kind**: enum

Constants that describe the reference point of the content insets.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum UIContentInsetsReference
```

## Topics

### Constants
- [UIContentInsetsReference.automatic](uicontentinsetsreference/automatic.md)
  Content insets use the system default reference point.
- [UIContentInsetsReference.none](uicontentinsetsreference/none.md)
  Content insets don’t have a reference point in relation to other insets.
- [UIContentInsetsReference.safeArea](uicontentinsetsreference/safearea.md)
  Content insets use a reference point in relation to the safe area.
- [UIContentInsetsReference.layoutMargins](uicontentinsetsreference/layoutmargins.md)
  Content insets use a reference point in relation to the layout margins.
- [UIContentInsetsReference.readableContent](uicontentinsetsreference/readablecontent.md)
  Content insets use a reference point in relation to the readable content guide.
### Initializers
- [init?(rawValue: Int)](uicontentinsetsreference/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var interGroupSpacing: CGFloat](nscollectionlayoutsection/intergroupspacing.md)
  The amount of space between the groups in the section.
- [var contentInsets: NSDirectionalEdgeInsets](nscollectionlayoutsection/contentinsets.md)
  The amount of space between the content of the section and its boundaries.
- [var contentInsetsReference: UIContentInsetsReference](nscollectionlayoutsection/contentinsetsreference.md)
  The boundary to reference when defining content insets.
- [var supplementaryContentInsetsReference: UIContentInsetsReference](nscollectionlayoutsection/supplementarycontentinsetsreference.md)
  The reference boundary for content insets on boundary supplementary items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentinsetsreference)*