# UICollectionLayoutSectionOrthogonalScrollingProperties.DecelerationRate

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants that specify the rate of deceleration in the orthogonal scrolling section after the scrolling pan gesture ends.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
struct DecelerationRate
```

```c
typedef CGFloat UICollectionLayoutSectionOrthogonalScrollingDecelerationRate;
```

## Topics

### Selecting deceleration rates
- [static let automatic: UICollectionLayoutSectionOrthogonalScrollingProperties.DecelerationRate](./decelerationrate-swift.struct/automatic.md)
  A deceleration rate that matches the parent scroll view’s deceleration rate for the orthogonal scrolling section.
- [static let fast: UICollectionLayoutSectionOrthogonalScrollingProperties.DecelerationRate](./decelerationrate-swift.struct/fast.md)
  A rapid deceleration rate for the orthogonal scrolling section.
- [static let normal: UICollectionLayoutSectionOrthogonalScrollingProperties.DecelerationRate](./decelerationrate-swift.struct/normal.md)
  The default deceleration rate for the orthogonal scrolling section.
### Creating a deceleration rate
- [init(rawValue: CGFloat)](./decelerationrate-swift.struct/init%28rawvalue%29.md)
  Creates a deceleration rate.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying the rate of deceleration
- [var decelerationRate: UICollectionLayoutSectionOrthogonalScrollingProperties.DecelerationRate](./decelerationrate-swift.property.md)
  A value that specifies the rate of deceleration in the orthogonal scrolling section after the scrolling pan gesture ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionlayoutsectionorthogonalscrollingproperties/decelerationrate-swift.struct)*