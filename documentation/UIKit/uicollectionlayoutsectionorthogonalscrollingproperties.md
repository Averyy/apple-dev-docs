# UICollectionLayoutSectionOrthogonalScrollingProperties

**Framework**: UIKit  
**Kind**: class

An object that specifies properties for a layout section that scrolls orthogonally in relation to the main layout axis.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICollectionLayoutSectionOrthogonalScrollingProperties
```

## Topics

### Specifying the bounce behavior
- [var bounce: UICollectionLayoutSectionOrthogonalScrollingProperties.Bounce](uicollectionlayoutsectionorthogonalscrollingproperties/bounce-swift.property.md)
  A value that specifies whether the orthogonal scrolling section bounces past the edge of content and back again.
- [UICollectionLayoutSectionOrthogonalScrollingProperties.Bounce](uicollectionlayoutsectionorthogonalscrollingproperties/bounce-swift.enum.md)
  Constants that specify whether the orthogonal scrolling section bounces past the edge of content and back again.
### Specifying the rate of deceleration
- [var decelerationRate: UICollectionLayoutSectionOrthogonalScrollingProperties.DecelerationRate](uicollectionlayoutsectionorthogonalscrollingproperties/decelerationrate-swift.property.md)
  A value that specifies the rate of deceleration in the orthogonal scrolling section after the scrolling pan gesture ends.
- [UICollectionLayoutSectionOrthogonalScrollingProperties.DecelerationRate](uicollectionlayoutsectionorthogonalscrollingproperties/decelerationrate-swift.struct.md)
  Constants that specify the rate of deceleration in the orthogonal scrolling section after the scrolling pan gesture ends.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var orthogonalScrollingBehavior: UICollectionLayoutSectionOrthogonalScrollingBehavior](nscollectionlayoutsection/orthogonalscrollingbehavior.md)
  The section’s scrolling behavior in relation to the main layout axis.
- [var orthogonalScrollingProperties: UICollectionLayoutSectionOrthogonalScrollingProperties](nscollectionlayoutsection/orthogonalscrollingproperties.md)
  The section’s orthogonal scrolling properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionlayoutsectionorthogonalscrollingproperties)*