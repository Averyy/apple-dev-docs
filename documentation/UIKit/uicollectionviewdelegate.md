# UICollectionViewDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

The methods adopted by the object you use to manage user interactions with items in a collection view.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
@MainActor
protocol UICollectionViewDelegate : UIScrollViewDelegate
```

```objc
@protocol UICollectionViewDelegate <UIScrollViewDelegate>
```

## Overview

A collection view delegate manages user interactions with the collection view’s contents, including item selection, highlighting, and performing actions on those items. The methods of this protocol are all optional.

When configuring the collection view object, assign your delegate object to its [`delegate`](./uicollectionview/delegate.md) property. For more information, see [`UICollectionView`](./uicollectionview.md).

## Topics

### Managing the selected cells
- [Changing the appearance of selected and highlighted cells](./changing-the-appearance-of-selected-and-highlighted-cells.md)
  Provide visual feedback to the user about the state of a cell and the transition between states.
- [Selecting multiple items with a two-finger pan gesture](./selecting-multiple-items-with-a-two-finger-pan-gesture.md)
  Accelerate user selection of multiple items using the multiselect gesture on table and collection views.
- [func collectionView(UICollectionView, shouldSelectItemAt: IndexPath) -> Bool](./uicollectionviewdelegate/collectionview%28_,shouldselectitemat%29.md)
  Asks the delegate if the specified item should be selected.
- [func collectionView(UICollectionView, didSelectItemAt: IndexPath)](./uicollectionviewdelegate/collectionview%28_,didselectitemat%29.md)
  Tells the delegate that the item at the specified index path was selected.
- [func collectionView(UICollectionView, shouldDeselectItemAt: IndexPath) -> Bool](./uicollectionviewdelegate/collectionview%28_,shoulddeselectitemat%29.md)
  Asks the delegate if the specified item should be deselected.
- [func collectionView(UICollectionView, didDeselectItemAt: IndexPath)](./uicollectionviewdelegate/collectionview%28_,diddeselectitemat%29.md)
  Tells the delegate that the item at the specified path was deselected.
- [func collectionView(UICollectionView, shouldBeginMultipleSelectionInteractionAt: IndexPath) -> Bool](./uicollectionviewdelegate/collectionview%28_,shouldbeginmultipleselectioninteractionat%29.md)
  Asks the delegate whether the user can select multiple items using a two-finger pan gesture in a collection view.
- [func collectionView(UICollectionView, didBeginMultipleSelectionInteractionAt: IndexPath)](./uicollectionviewdelegate/collectionview%28_,didbeginmultipleselectioninteractionat%29.md)
  Tells the delegate when the user starts using a two-finger pan gesture to select multiple items in a collection view.
- [func collectionViewDidEndMultipleSelectionInteraction(UICollectionView)](./uicollectionviewdelegate/collectionviewdidendmultipleselectioninteraction%28_%29.md)
  Tells the delegate when the user stops using a two-finger pan gesture to select multiple items in a collection view.
### Managing cell highlighting
- [func collectionView(UICollectionView, shouldHighlightItemAt: IndexPath) -> Bool](./uicollectionviewdelegate/collectionview%28_,shouldhighlightitemat%29.md)
  Asks the delegate if the item should be highlighted during tracking.
- [func collectionView(UICollectionView, didHighlightItemAt: IndexPath)](./uicollectionviewdelegate/collectionview%28_,didhighlightitemat%29.md)
  Tells the delegate that the item at the specified index path was highlighted.
- [func collectionView(UICollectionView, didUnhighlightItemAt: IndexPath)](./uicollectionviewdelegate/collectionview%28_,didunhighlightitemat%29.md)
  Tells the delegate that the highlight was removed from the item at the specified index path.
### Tracking the addition and removal of views
- [func collectionView(UICollectionView, willDisplay: UICollectionViewCell, forItemAt: IndexPath)](./uicollectionviewdelegate/collectionview%28_,willdisplay,foritemat%29.md)
  Tells the delegate that the specified cell is about to be displayed in the collection view.
- [func collectionView(UICollectionView, willDisplaySupplementaryView: UICollectionReusableView, forElementKind: String, at: IndexPath)](./uicollectionviewdelegate/collectionview%28_,willdisplaysupplementaryview,forelementkind,at%29.md)
  Tells the delegate that the specified supplementary view is about to be displayed in the collection view.
- [func collectionView(UICollectionView, didEndDisplaying: UICollectionViewCell, forItemAt: IndexPath)](./uicollectionviewdelegate/collectionview%28_,didenddisplaying,foritemat%29.md)
  Tells the delegate that the specified cell was removed from the collection view.
- [func collectionView(UICollectionView, didEndDisplayingSupplementaryView: UICollectionReusableView, forElementOfKind: String, at: IndexPath)](./uicollectionviewdelegate/collectionview%28_,didenddisplayingsupplementaryview,forelementofkind,at%29.md)
  Tells the delegate that the specified supplementary view was removed from the collection view.
### Handling layout changes
- [func collectionView(UICollectionView, transitionLayoutForOldLayout: UICollectionViewLayout, newLayout: UICollectionViewLayout) -> UICollectionViewTransitionLayout](./uicollectionviewdelegate/collectionview%28_,transitionlayoutforoldlayout,newlayout%29.md)
  Asks for the custom transition layout to use when moving between the specified layouts.
- [func collectionView(UICollectionView, targetContentOffsetForProposedContentOffset: CGPoint) -> CGPoint](./uicollectionviewdelegate/collectionview%28_,targetcontentoffsetforproposedcontentoffset%29.md)
  Gives the delegate an opportunity to customize the content offset for layout changes and animated updates.
- [func collectionView(UICollectionView, targetIndexPathForMoveOfItemFromOriginalIndexPath: IndexPath, atCurrentIndexPath: IndexPath, toProposedIndexPath: IndexPath) -> IndexPath](./uicollectionviewdelegate/collectionview%28_,targetindexpathformoveofitemfromoriginalindexpath,atcurrentindexpath,toproposedindexpath%29.md)
  Asks the delegate for the index path to use when moving an item.
### Managing context menus
- [Adding context menus in your app](./adding-context-menus-in-your-app.md)
  Provide quick access to useful actions by adding context menus to your iOS app.
- [func collectionView(UICollectionView, willDisplayContextMenu: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](./uicollectionviewdelegate/collectionview%28_,willdisplaycontextmenu,animator%29.md)
  Informs the delegate when a context menu will appear.
- [func collectionView(UICollectionView, willEndContextMenuInteraction: UIContextMenuConfiguration, animator: (any UIContextMenuInteractionAnimating)?)](./uicollectionviewdelegate/collectionview%28_,willendcontextmenuinteraction,animator%29.md)
  Informs the delegate when a context menu will disappear.
- [func collectionView(UICollectionView, willPerformPreviewActionForMenuWith: UIContextMenuConfiguration, animator: any UIContextMenuInteractionCommitAnimating)](./uicollectionviewdelegate/collectionview%28_,willperformpreviewactionformenuwith,animator%29.md)
  Informs the delegate when a user triggers a commit by tapping the preview.
- [func collectionView(UICollectionView, contextMenuConfigurationForItemsAt: [IndexPath], point: CGPoint) -> UIContextMenuConfiguration?](./uicollectionviewdelegate/collectionview%28_,contextmenuconfigurationforitemsat,point%29.md)
  Asks the delegate for a context-menu configuration for the items at the specified index paths.
- [func collectionView(UICollectionView, contextMenuConfiguration: UIContextMenuConfiguration, highlightPreviewForItemAt: IndexPath) -> UITargetedPreview?](./uicollectionviewdelegate/collectionview%28_,contextmenuconfiguration,highlightpreviewforitemat%29.md)
  Asks the delegate for a preview of the item at the specified index path when a context-menu interaction begins.
- [func collectionView(UICollectionView, contextMenuConfiguration: UIContextMenuConfiguration, dismissalPreviewForItemAt: IndexPath) -> UITargetedPreview?](./uicollectionviewdelegate/collectionview%28_,contextmenuconfiguration,dismissalpreviewforitemat%29.md)
  Asks the delegate for a preview of the item at the specified index path when a context-menu interaction ends.
### Working with focus
- [func collectionView(UICollectionView, canFocusItemAt: IndexPath) -> Bool](./uicollectionviewdelegate/collectionview%28_,canfocusitemat%29.md)
  Asks the delegate whether the item at the specified index path can be focused.
- [func indexPathForPreferredFocusedView(in: UICollectionView) -> IndexPath?](./uicollectionviewdelegate/indexpathforpreferredfocusedview%28in%29.md)
  Asks the delegate for the index path of the cell that should be focused.
- [func collectionView(UICollectionView, shouldUpdateFocusIn: UICollectionViewFocusUpdateContext) -> Bool](./uicollectionviewdelegate/collectionview%28_,shouldupdatefocusin%29.md)
  Asks the delegate whether a change in focus should occur.
- [func collectionView(UICollectionView, didUpdateFocusIn: UICollectionViewFocusUpdateContext, with: UIFocusAnimationCoordinator)](./uicollectionviewdelegate/collectionview%28_,didupdatefocusin,with%29.md)
  Tells the delegate that a focus update occurred.
- [func collectionView(UICollectionView, selectionFollowsFocusForItemAt: IndexPath) -> Bool](./uicollectionviewdelegate/collectionview%28_,selectionfollowsfocusforitemat%29.md)
  Asks the delegate whether to relate selection and focus behavior for the cell at the corresponding index path.
### Editing items
- [func collectionView(UICollectionView, canEditItemAt: IndexPath) -> Bool](./uicollectionviewdelegate/collectionview%28_,canedititemat%29.md)
  Determines whether the specified item is editable.
### Managing actions for cells
- [func collectionView(UICollectionView, canPerformPrimaryActionForItemAt: IndexPath) -> Bool](./uicollectionviewdelegate/collectionview%28_,canperformprimaryactionforitemat%29.md)
  Asks the delegate whether to perform a primary action for the cell at the specified index path.
- [func collectionView(UICollectionView, performPrimaryActionForItemAt: IndexPath)](./uicollectionviewdelegate/collectionview%28_,performprimaryactionforitemat%29.md)
  Tells the delegate to perform the primary action for the cell at the specified index path.
### Handling scene transitions
- [func collectionView(UICollectionView, sceneActivationConfigurationForItemAt: IndexPath, point: CGPoint) -> UIWindowScene.ActivationConfiguration?](./uicollectionviewdelegate/collectionview%28_,sceneactivationconfigurationforitemat,point%29.md)
  Returns a scene activation configuration that allows the cell to expand into a new scene.
### Controlling the spring-loading behavior
- [func collectionView(UICollectionView, shouldSpringLoadItemAt: IndexPath, with: any UISpringLoadedInteractionContext) -> Bool](./uicollectionviewdelegate/collectionview%28_,shouldspringloaditemat,with%29.md)
  Determines whether the spring-loading interaction effect is displayed for the specified item.
### Deprecated
- [Deprecated symbols](./uicollectionviewdelegate-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [UIScrollViewDelegate](./uiscrollviewdelegate.md)
### Inherited By
- [UICollectionViewDelegateFlowLayout](./uicollectionviewdelegateflowlayout.md)
### Conforming Types
- [UICollectionViewController](./uicollectionviewcontroller.md)

## See Also

### Managing collection view interactions
- [var delegate: (any UICollectionViewDelegate)?](./uicollectionview/delegate.md)
  The object that acts as the delegate of the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdelegate)*