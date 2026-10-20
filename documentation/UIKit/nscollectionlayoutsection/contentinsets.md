# contentInsets

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The amount of space between the content of the section and its boundaries.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var contentInsets: NSDirectionalEdgeInsets { get set }
```

```objc
@property (nonatomic) NSDirectionalEdgeInsets contentInsets;
```

## See Also

### Configuring section spacing
- [var interGroupSpacing: CGFloat](./intergroupspacing.md)
  The amount of space between the groups in the section.
- [var contentInsetsReference: UIContentInsetsReference](./contentinsetsreference.md)
  The boundary to reference when defining content insets.
- [var supplementaryContentInsetsReference: UIContentInsetsReference](./supplementarycontentinsetsreference.md)
  The reference boundary for content insets on boundary supplementary items.
- [enum UIContentInsetsReference](../uicontentinsetsreference.md)
  Constants that describe the reference point of the content insets.
- [var supplementariesFollowContentInsets: Bool](./supplementariesfollowcontentinsets.md)
  A Boolean value that indicates whether the section’s supplementary items follow the specified content insets for the section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutsection/contentinsets)*