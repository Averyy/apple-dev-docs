# TVCollectionViewFullScreenLayoutAttributes

**Framework**: TVUIKit  
**Kind**: class

Attributes to manage the appearance of the collection view’s layout.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
@MainActor
class TVCollectionViewFullScreenLayoutAttributes
```

## Topics

### Modifying Cell Appearance
- [var contentBleed: UIEdgeInsets](tvcollectionviewfullscreenlayoutattributes/contentbleed.md)
  The amount of content that bleeds into the masked portions of the cell.
- [var cornerRadius: CGFloat](tvcollectionviewfullscreenlayoutattributes/cornerradius.md)
  The radius to use when drawing rounded corners for the cell.
- [var maskAmount: CGFloat](tvcollectionviewfullscreenlayoutattributes/maskamount.md)
  The amount of masking to apply to the cell.
### Modifying the Parallax Effect
- [var parallaxOffset: CGFloat](tvcollectionviewfullscreenlayoutattributes/parallaxoffset.md)
  The number of points by which to shift the background from the center when moving focus.
### Managing Cell Position
- [var normalizedPosition: CGFloat](tvcollectionviewfullscreenlayoutattributes/normalizedposition.md)
  A value that indicates the distance of the current cell from the collection view’s center cell.

## Relationships

### Inherits From
- [UICollectionViewLayoutAttributes](../UIKit/UICollectionViewLayoutAttributes.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)

## See Also

- [Creating immersive experiences using a full-screen layout](creating-immersive-experiences-using-a-full-screen-layout.md)
  Display content with a collection view that maximizes the tvOS experience.
- [class TVCollectionViewFullScreenLayout](tvcollectionviewfullscreenlayout.md)
  A collection view layout that organizes items into a browsable, full-screen display format.
- [protocol TVCollectionViewDelegateFullScreenLayout](tvcollectionviewdelegatefullscreenlayout.md)
  Methods that send notifications of events during cell transitions.
- [class TVCollectionViewFullScreenCell](tvcollectionviewfullscreencell.md)
  A full-screen cell to use in full-screen display format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcollectionviewfullscreenlayoutattributes)*