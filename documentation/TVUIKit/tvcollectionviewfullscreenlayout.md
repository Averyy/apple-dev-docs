# TVCollectionViewFullScreenLayout

**Framework**: TVUIKit  
**Kind**: class

A collection view layout that organizes items into a browsable, full-screen display format.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
@MainActor
class TVCollectionViewFullScreenLayout
```

#### Overview

Use this class to create a full-screen browsing experience. Full-screen layouts are an immersive way to present and navigate through content.

![A diagram showing the TVCollectionViewFullScreenLayout. One cell is centered, and two cells are peeking from the left and right sides.](https://docs-assets.developer.apple.com/published/dc256aae53b2cb0d0bc0e88c31ab8fa5/media-3332103%402x.png)

## Topics

### Managing a collection view’s appearance
- [var interitemSpacing: CGFloat](tvcollectionviewfullscreenlayout/interitemspacing.md)
  The spacing between each cell in a collection view.
### Accessing collection view items
- [var centerIndexPath: IndexPath?](tvcollectionviewfullscreenlayout/centerindexpath.md)
  The index path of the currently centered item.
### Configuring cell masks
- [var maskAmount: CGFloat](tvcollectionviewfullscreenlayout/maskamount.md)
  The amount by which to mask the cells in a collection view.
- [var maskInset: UIEdgeInsets](tvcollectionviewfullscreenlayout/maskinset.md)
  The edge insets of the cell mask.
### Managing cell appearance
- [var cornerRadius: CGFloat](tvcollectionviewfullscreenlayout/cornerradius.md)
  The radius to use when drawing rounded corners for the cell.
### Managing transitions
- [var parallaxFactor: CGFloat](tvcollectionviewfullscreenlayout/parallaxfactor.md)
  A value that specifies how slowly the background should move relative to the foreground.
- [var isTransitioningToCenterIndexPath: Bool](tvcollectionviewfullscreenlayout/istransitioningtocenterindexpath.md)
  A Boolean value that indicates whether the cell is changing index paths.

## Relationships

### Inherits From
- [UICollectionViewLayout](../UIKit/UICollectionViewLayout.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Creating immersive experiences using a full-screen layout](creating-immersive-experiences-using-a-full-screen-layout.md)
  Display content with a collection view that maximizes the tvOS experience.
- [protocol TVCollectionViewDelegateFullScreenLayout](tvcollectionviewdelegatefullscreenlayout.md)
  Methods that send notifications of events during cell transitions.
- [class TVCollectionViewFullScreenCell](tvcollectionviewfullscreencell.md)
  A full-screen cell to use in full-screen display format.
- [class TVCollectionViewFullScreenLayoutAttributes](tvcollectionviewfullscreenlayoutattributes.md)
  Attributes to manage the appearance of the collection view’s layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcollectionviewfullscreenlayout)*