# TVCollectionViewDelegateFullScreenLayout

**Framework**: TVUIKit  
**Kind**: protocol  
**Role**: Protocol

Methods that send notifications of events during cell transitions.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
protocol TVCollectionViewDelegateFullScreenLayout : UICollectionViewDelegate
```

```objc
@protocol TVCollectionViewDelegateFullScreenLayout <UICollectionViewDelegate>
```

## Overview

The methods contained in this protocol help you manage and control cell transitions.

## Topics

### Managing Cell Transitions
- [func collectionView(UICollectionView, layout: UICollectionViewLayout, willCenterCellAt: IndexPath)](./tvcollectionviewdelegatefullscreenlayout/collectionview%28_,layout,willcentercellat%29.md)
  Tells the delegate when a cell is to be the center cell.
- [func collectionView(UICollectionView, layout: UICollectionViewLayout, didCenterCellAt: IndexPath)](./tvcollectionviewdelegatefullscreenlayout/collectionview%28_,layout,didcentercellat%29.md)
  Tells the delegate when a cell has completed the transition and has become the center cell.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [UICollectionViewDelegate](../UIKit/uicollectionviewdelegate.md)
- [UIScrollViewDelegate](../UIKit/uiscrollviewdelegate.md)

## See Also

### Collections of content
- [Creating immersive experiences using a full-screen layout](./creating-immersive-experiences-using-a-full-screen-layout.md)
  Display content with a collection view that maximizes the tvOS experience.
- [class TVCollectionViewFullScreenLayout](./tvcollectionviewfullscreenlayout.md)
  A collection view layout that organizes items into a browsable, full-screen display format.
- [class TVCollectionViewFullScreenCell](./tvcollectionviewfullscreencell.md)
  A full-screen cell to use in full-screen display format.
- [class TVCollectionViewFullScreenLayoutAttributes](./tvcollectionviewfullscreenlayoutattributes.md)
  Attributes to manage the appearance of the collection view’s layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcollectionviewdelegatefullscreenlayout)*