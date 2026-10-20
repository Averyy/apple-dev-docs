# supplementariesFollowContentInsets

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the section’s supplementary items follow the specified content insets for the section.

**Availability**:
- iOS 13.0+ - Deprecated in 16.0
- iPadOS 13.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- tvOS 13.0+ - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`supplementaryContentInsetsReference`](./supplementarycontentinsetsreference.md) instead.

## Declaration

```swift
var supplementariesFollowContentInsets: Bool { get set }
```

```objc
@property (nonatomic) BOOL supplementariesFollowContentInsets;
```

#### Discussion

The default value of this property is [`true`](../../Swift/true.md).

## See Also

### Configuring section spacing
- [var interGroupSpacing: CGFloat](./intergroupspacing.md)
  The amount of space between the groups in the section.
- [var contentInsets: NSDirectionalEdgeInsets](./contentinsets.md)
  The amount of space between the content of the section and its boundaries.
- [var contentInsetsReference: UIContentInsetsReference](./contentinsetsreference.md)
  The boundary to reference when defining content insets.
- [var supplementaryContentInsetsReference: UIContentInsetsReference](./supplementarycontentinsetsreference.md)
  The reference boundary for content insets on boundary supplementary items.
- [enum UIContentInsetsReference](../uicontentinsetsreference.md)
  Constants that describe the reference point of the content insets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutsection/supplementariesfollowcontentinsets)*