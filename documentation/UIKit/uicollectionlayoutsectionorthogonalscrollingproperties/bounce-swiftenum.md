# UICollectionLayoutSectionOrthogonalScrollingProperties.Bounce

**Framework**: UIKit  
**Kind**: enum

Constants that specify whether the orthogonal scrolling section bounces past the edge of content and back again.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
enum Bounce
```

## Topics

### Selecting bounce options
- [UICollectionLayoutSectionOrthogonalScrollingProperties.Bounce.always](uicollectionlayoutsectionorthogonalscrollingproperties/bounce-swift.enum/always.md)
  The orthogonal scroll view bounces even if the content is smaller than its bounds.
- [UICollectionLayoutSectionOrthogonalScrollingProperties.Bounce.automatic](uicollectionlayoutsectionorthogonalscrollingproperties/bounce-swift.enum/automatic.md)
  The orthogonal scroll view bounces when it encounters a content boundary.
- [UICollectionLayoutSectionOrthogonalScrollingProperties.Bounce.never](uicollectionlayoutsectionorthogonalscrollingproperties/bounce-swift.enum/never.md)
  The orthogonal scroll view stops scrolling immediately when it encounters a content boundary without bouncing.
### Initializers
- [init?(rawValue: Int)](uicollectionlayoutsectionorthogonalscrollingproperties/bounce-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var bounce: UICollectionLayoutSectionOrthogonalScrollingProperties.Bounce](uicollectionlayoutsectionorthogonalscrollingproperties/bounce-swift.property.md)
  A value that specifies whether the orthogonal scrolling section bounces past the edge of content and back again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionlayoutsectionorthogonalscrollingproperties/bounce-swift.enum)*