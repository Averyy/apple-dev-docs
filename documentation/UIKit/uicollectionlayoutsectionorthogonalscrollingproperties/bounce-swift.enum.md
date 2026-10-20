# UICollectionLayoutSectionOrthogonalScrollingProperties.Bounce

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UICollectionLayoutSectionOrthogonalScrollingBounce : NSInteger;
```

## Topics

### Selecting bounce options
- [UICollectionLayoutSectionOrthogonalScrollingProperties.Bounce.always](./bounce-swift.enum/always.md)
  The orthogonal scroll view bounces even if the content is smaller than its bounds.
- [UICollectionLayoutSectionOrthogonalScrollingProperties.Bounce.automatic](./bounce-swift.enum/automatic.md)
  The orthogonal scroll view bounces when it encounters a content boundary.
- [UICollectionLayoutSectionOrthogonalScrollingProperties.Bounce.never](./bounce-swift.enum/never.md)
  The orthogonal scroll view stops scrolling immediately when it encounters a content boundary without bouncing.
### Initializers
- [init?(rawValue: Int)](./bounce-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying the bounce behavior
- [var bounce: UICollectionLayoutSectionOrthogonalScrollingProperties.Bounce](./bounce-swift.property.md)
  A value that specifies whether the orthogonal scrolling section bounces past the edge of content and back again.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionlayoutsectionorthogonalscrollingproperties/bounce-swift.enum)*