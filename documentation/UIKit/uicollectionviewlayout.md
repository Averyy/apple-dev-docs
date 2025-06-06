# UICollectionViewLayout

**Framework**: UIKit  
**Kind**: class

An abstract base class for generating layout information for a collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICollectionViewLayout
```

#### Overview

A layout object determines the placement of cells, supplementary views, and decoration views inside the collection view’s bounds and reports that information to the collection view. The collection view then applies the provided layout information to the corresponding views so that they can be presented onscreen.

You must subclass [`UICollectionViewLayout`](uicollectionviewlayout.md) in order to use it. Before you consider subclassing, however, consider whether you can adapt [`UICollectionViewCompositionalLayout`](uicollectionviewcompositionallayout.md) to your layout needs.

##### Subclassing Notes

The layout object defines the position, size, and visual state of items in the collection view, based on the design of the layout. The views for the layout are created by the collection view’s data source.

You lay out three types of visual elements in a collection view:

-  are the main elements positioned by the layout. Each cell represents a single data item in the collection. You can make cells interactive so that a user can perform actions like selecting, dragging, and reordering the cells. A collection view can have a single group of cells, or you can divide those cells into multiple sections. The layout object arranges the cells in the collection view’s content area.
-  present data but can’t be selected by the user. You use supplementary views to implement things like header and footer views for a given section or for the entire collection view. Supplementary views are optional and their use and placement is defined by the layout object.
-  are visual adornments, like badges, that can’t be selected and aren’t inherently tied to the data of the collection view. Decoration views are another type of supplementary view. Like supplementary views, they’re optional and their use and placement is defined by the layout object.

The collection view asks its layout object to provide layout information for these elements at many different times. Every cell and view that appears on screen is positioned using information from the layout object. Similarly, every time items are inserted into or deleted from the collection view, an additional layout pass occurs for the items being added or removed. However, the collection view always limits layout to the objects that are visible onscreen.

###### Methods to Override

Every layout object should implement the following methods:

- [`collectionViewContentSize`](uicollectionviewlayout/collectionviewcontentsize.md)
- [`layoutAttributesForElements(in:)`](uicollectionviewlayout/layoutattributesforelements(in:).md)
- [`layoutAttributesForItem(at:)`](uicollectionviewlayout/layoutattributesforitem(at:).md)
- [`layoutAttributesForSupplementaryView(ofKind:at:)`](uicollectionviewlayout/layoutattributesforsupplementaryview(ofkind:at:).md) (if your layout supports supplementary views)
- [`layoutAttributesForDecorationView(ofKind:at:)`](uicollectionviewlayout/layoutattributesfordecorationview(ofkind:at:).md) (if your layout supports decoration views)
- [`shouldInvalidateLayout(forBoundsChange:)`](uicollectionviewlayout/shouldinvalidatelayout(forboundschange:).md)

These methods provide the fundamental layout information that the collection view needs to place contents on the screen. If your layout doesn’t support supplementary or decoration views, don’t implement the corresponding methods.

When the data in the collection view changes and items are to be inserted or deleted, the collection view asks its layout object to update the layout information. Specifically, any item that’s moved, added, or deleted must have its layout information updated to reflect its new location. For moved items, the collection view uses the standard methods to retrieve the item’s updated layout attributes. For items being inserted or deleted, the collection view calls some different methods, which you should override to provide the appropriate layout information:

- [`initialLayoutAttributesForAppearingItem(at:)`](uicollectionviewlayout/initiallayoutattributesforappearingitem(at:).md)
- [`initialLayoutAttributesForAppearingSupplementaryElement(ofKind:at:)`](uicollectionviewlayout/initiallayoutattributesforappearingsupplementaryelement(ofkind:at:).md)
- [`initialLayoutAttributesForAppearingDecorationElement(ofKind:at:)`](uicollectionviewlayout/initiallayoutattributesforappearingdecorationelement(ofkind:at:).md)
- [`finalLayoutAttributesForDisappearingItem(at:)`](uicollectionviewlayout/finallayoutattributesfordisappearingitem(at:).md)
- [`finalLayoutAttributesForDisappearingSupplementaryElement(ofKind:at:)`](uicollectionviewlayout/finallayoutattributesfordisappearingsupplementaryelement(ofkind:at:).md)
- [`finalLayoutAttributesForDisappearingDecorationElement(ofKind:at:)`](uicollectionviewlayout/finallayoutattributesfordisappearingdecorationelement(ofkind:at:).md)

In addition to these methods, you can also override the [`prepare(forCollectionViewUpdates:)`](uicollectionviewlayout/prepare(forcollectionviewupdates:).md) to handle any layout-related preparation. You can also override the [`finalizeCollectionViewUpdates()`](uicollectionviewlayout/finalizecollectionviewupdates().md) method and use it to add animations to the overall animation block or to implement any final layout-related tasks.

###### Optimizing Layout Performance Using Invalidation Contexts

When designing your custom layouts, you can improve performance by invalidating only those parts of your layout that actually changed. When you change items, calling the [`invalidateLayout()`](uicollectionviewlayout/invalidatelayout().md) method forces the collection view to recompute all of its layout information and reapply it. A better solution is to recompute only the layout information that changed, which is exactly what invalidation contexts allow you to do. An invalidation context lets you specify which parts of the layout changed. The layout object can then use that information to minimize the amount of data it recomputes.

To define a custom invalidation context for your layout, subclass the [`UICollectionViewLayoutInvalidationContext`](uicollectionviewlayoutinvalidationcontext.md) class. In your subclass, define custom properties that represent the parts of your layout data that can be recomputed independently. When you need to invalidate your layout at runtime, create an instance of your invalidation context subclass, configure the custom properties based on what layout information changed, and pass that object to your layout’s [`invalidateLayout(with:)`](uicollectionviewlayout/invalidatelayout(with:).md) method. Your custom implementation of that method can use the information in the invalidation context to recompute only the portions of your layout that changed.

If you define a custom invalidation context class for your layout object, you should also override the [`invalidationContextClass`](uicollectionviewlayout/invalidationcontextclass.md) method and return your custom class. The collection view always creates an instance of the class you specify when it needs an invalidation context. Returning your custom subclass from this method ensures that your layout object always has the invalidation context it expects.

## Topics

### Creating the collection view layout
- [init()](uicollectionviewlayout/init.md)
  Creates a collection view layout object.
- [init?(coder: NSCoder)](uicollectionviewlayout/init(coder:).md)
  Creates a collection view layout object from data in a given unarchiver.
### Getting the collection view information
- [var collectionView: UICollectionView?](uicollectionviewlayout/collectionview.md)
  The collection view object currently using this layout object.
- [var collectionViewContentSize: CGSize](uicollectionviewlayout/collectionviewcontentsize.md)
  The width and height of the collection view’s contents.
### Providing layout attributes
- [class var layoutAttributesClass: AnyClass](uicollectionviewlayout/layoutattributesclass.md)
  The class to use when creating layout attributes objects.
- [func prepare()](uicollectionviewlayout/prepare.md)
  Tells the layout object to update the current layout.
- [func layoutAttributesForElements(in: CGRect) -> [UICollectionViewLayoutAttributes]?](uicollectionviewlayout/layoutattributesforelements(in:).md)
  Retrieves the layout attributes for all of the cells and views in the specified rectangle.
- [func layoutAttributesForItem(at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionviewlayout/layoutattributesforitem(at:).md)
  Retrieves layout information for an item at the specified index path with a corresponding cell.
- [func layoutAttributesForInteractivelyMovingItem(at: IndexPath, withTargetPosition: CGPoint) -> UICollectionViewLayoutAttributes](uicollectionviewlayout/layoutattributesforinteractivelymovingitem(at:withtargetposition:).md)
  Retrieves the layout attributes of an item when it is being moved interactively by the user.
- [func layoutAttributesForSupplementaryView(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionviewlayout/layoutattributesforsupplementaryview(ofkind:at:).md)
  Retrieves the layout attributes for the specified supplementary view.
- [func layoutAttributesForDecorationView(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionviewlayout/layoutattributesfordecorationview(ofkind:at:).md)
  Retrieves the layout attributes for the specified decoration view.
- [func targetContentOffset(forProposedContentOffset: CGPoint) -> CGPoint](uicollectionviewlayout/targetcontentoffset(forproposedcontentoffset:).md)
  Retrieves the content offset to use after an animated layout update or change.
- [func targetContentOffset(forProposedContentOffset: CGPoint, withScrollingVelocity: CGPoint) -> CGPoint](uicollectionviewlayout/targetcontentoffset(forproposedcontentoffset:withscrollingvelocity:).md)
  Retrieves the point at which to stop scrolling.
### Responding to collection view updates
- [func prepare(forCollectionViewUpdates: [UICollectionViewUpdateItem])](uicollectionviewlayout/prepare(forcollectionviewupdates:).md)
  Notifies the layout object that the contents of the collection view are about to change.
- [func finalizeCollectionViewUpdates()](uicollectionviewlayout/finalizecollectionviewupdates.md)
  Performs any additional animations or clean up needed during a collection view update.
- [func indexPathsToInsertForSupplementaryView(ofKind: String) -> [IndexPath]](uicollectionviewlayout/indexpathstoinsertforsupplementaryview(ofkind:).md)
  Retrieves an array of index paths for the supplementary views you want to add to the layout.
- [func indexPathsToInsertForDecorationView(ofKind: String) -> [IndexPath]](uicollectionviewlayout/indexpathstoinsertfordecorationview(ofkind:).md)
  Retrieves an array of index paths representing the decoration views to add.
- [func initialLayoutAttributesForAppearingItem(at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionviewlayout/initiallayoutattributesforappearingitem(at:).md)
  Retrieves the starting layout information for an item being inserted into the collection view.
- [func initialLayoutAttributesForAppearingSupplementaryElement(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionviewlayout/initiallayoutattributesforappearingsupplementaryelement(ofkind:at:).md)
  Retrieves the starting layout information for a supplementary view being inserted into the collection view.
- [func initialLayoutAttributesForAppearingDecorationElement(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionviewlayout/initiallayoutattributesforappearingdecorationelement(ofkind:at:).md)
  Retrieves the starting layout information for a decoration view being inserted into the collection view.
- [func indexPathsToDeleteForSupplementaryView(ofKind: String) -> [IndexPath]](uicollectionviewlayout/indexpathstodeleteforsupplementaryview(ofkind:).md)
  Retrieves an array of index paths representing the supplementary views to remove.
- [func indexPathsToDeleteForDecorationView(ofKind: String) -> [IndexPath]](uicollectionviewlayout/indexpathstodeletefordecorationview(ofkind:).md)
  Retrieves an array of index paths representing the decoration views to remove.
- [func finalLayoutAttributesForDisappearingItem(at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionviewlayout/finallayoutattributesfordisappearingitem(at:).md)
  Retrieves the final layout information for an item that is about to be removed from the collection view.
- [func finalLayoutAttributesForDisappearingSupplementaryElement(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionviewlayout/finallayoutattributesfordisappearingsupplementaryelement(ofkind:at:).md)
  Retrieves the final layout information for a supplementary view that is about to be removed from the collection view.
- [func finalLayoutAttributesForDisappearingDecorationElement(ofKind: String, at: IndexPath) -> UICollectionViewLayoutAttributes?](uicollectionviewlayout/finallayoutattributesfordisappearingdecorationelement(ofkind:at:).md)
  Retrieves the final layout information for a decoration view that is about to be removed from the collection view.
- [func targetIndexPath(forInteractivelyMovingItem: IndexPath, withPosition: CGPoint) -> IndexPath](uicollectionviewlayout/targetindexpath(forinteractivelymovingitem:withposition:).md)
  Retrieves the index path to for an item when it is at the specified location in the collection view’s bounds.
### Invalidating the layout
- [func invalidateLayout()](uicollectionviewlayout/invalidatelayout.md)
  Invalidates the current layout and triggers a layout update.
- [func invalidateLayout(with: UICollectionViewLayoutInvalidationContext)](uicollectionviewlayout/invalidatelayout(with:).md)
  Invalidates the current layout using the information in the provided context object.
- [class var invalidationContextClass: AnyClass](uicollectionviewlayout/invalidationcontextclass.md)
  Returns the class to use when creating an invalidation context for the layout.
- [func shouldInvalidateLayout(forBoundsChange: CGRect) -> Bool](uicollectionviewlayout/shouldinvalidatelayout(forboundschange:).md)
  Asks the layout object if the new bounds require a layout update.
- [func invalidationContext(forBoundsChange: CGRect) -> UICollectionViewLayoutInvalidationContext](uicollectionviewlayout/invalidationcontext(forboundschange:).md)
  Retrieves a context object that defines the portions of the layout that should change when a bounds change occurs.
- [func shouldInvalidateLayout(forPreferredLayoutAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes: UICollectionViewLayoutAttributes) -> Bool](uicollectionviewlayout/shouldinvalidatelayout(forpreferredlayoutattributes:withoriginalattributes:).md)
  Asks the layout object if changes to a self-sizing cell require a layout update.
- [func invalidationContext(forPreferredLayoutAttributes: UICollectionViewLayoutAttributes, withOriginalAttributes: UICollectionViewLayoutAttributes) -> UICollectionViewLayoutInvalidationContext](uicollectionviewlayout/invalidationcontext(forpreferredlayoutattributes:withoriginalattributes:).md)
  Retrieves a context object that identifies the portions of the layout that should change in response to dynamic cell changes.
- [func invalidationContext(forInteractivelyMovingItems: [IndexPath], withTargetPosition: CGPoint, previousIndexPaths: [IndexPath], previousPosition: CGPoint) -> UICollectionViewLayoutInvalidationContext](uicollectionviewlayout/invalidationcontext(forinteractivelymovingitems:withtargetposition:previousindexpaths:previousposition:).md)
  Retrieves a context object that identifies the items that are being interactively moved in the layout.
- [func invalidationContextForEndingInteractiveMovementOfItems(toFinalIndexPaths: [IndexPath], previousIndexPaths: [IndexPath], movementCancelled: Bool) -> UICollectionViewLayoutInvalidationContext](uicollectionviewlayout/invalidationcontextforendinginteractivemovementofitems(tofinalindexpaths:previousindexpaths:movementcancelled:).md)
  Retrieves a context object that identifies the items that were moved
### Coordinating animated changes
- [func prepare(forAnimatedBoundsChange: CGRect)](uicollectionviewlayout/prepare(foranimatedboundschange:).md)
  Prepares the layout object for animated changes to the view’s bounds or the insertion or deletion of items.
- [func finalizeAnimatedBoundsChange()](uicollectionviewlayout/finalizeanimatedboundschange.md)
  Cleans up after any animated changes to the view’s bounds or after the insertion or deletion of items.
### Transitioning between layouts
- [func prepareForTransition(from: UICollectionViewLayout)](uicollectionviewlayout/preparefortransition(from:).md)
  Tells the layout object to prepare to be installed as the layout for the collection view.
- [func prepareForTransition(to: UICollectionViewLayout)](uicollectionviewlayout/preparefortransition(to:).md)
  Tells the layout object that it is about to be removed as the layout for the collection view.
- [func finalizeLayoutTransition()](uicollectionviewlayout/finalizelayouttransition.md)
  Tells the layout object to perform any final steps before the transition animations occur.
### Registering decoration views
- [func register(AnyClass?, forDecorationViewOfKind: String)](uicollectionviewlayout/register(_:fordecorationviewofkind:)-361k6.md)
  Registers a class for use in creating decoration views for a collection view.
- [func register(UINib?, forDecorationViewOfKind: String)](uicollectionviewlayout/register(_:fordecorationviewofkind:)-35jf9.md)
  Registers a nib file for use in creating decoration views for a collection view.
### Supporting right-to-left layouts
- [var developmentLayoutDirection: UIUserInterfaceLayoutDirection](uicollectionviewlayout/developmentlayoutdirection.md)
  The direction of the language you used when designing your custom layout.
- [var flipsHorizontallyInOppositeLayoutDirection: Bool](uicollectionviewlayout/flipshorizontallyinoppositelayoutdirection.md)
  A Boolean value that indicates whether the horizontal coordinate system is automatically flipped at appropriate times.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UICollectionViewCompositionalLayout](uicollectionviewcompositionallayout.md)
- [UICollectionViewFlowLayout](uicollectionviewflowlayout.md)
- [UICollectionViewTransitionLayout](uicollectionviewtransitionlayout.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Customizing collection view layouts](customizing-collection-view-layouts.md)
  Customize a view layout by changing the size of cells in the flow or implementing a mosaic style.
- [class UICollectionViewFlowLayout](uicollectionviewflowlayout.md)
  A layout object that organizes items into a grid with optional header and footer views for each section.
- [class UICollectionViewTransitionLayout](uicollectionviewtransitionlayout.md)
  A special type of layout object that lets you implement behaviors when changing from one layout to another in your collection view.
- [class UICollectionViewLayoutAttributes](uicollectionviewlayoutattributes.md)
  A layout object that manages the layout-related attributes for a given item in a collection view.
- [class UICollectionViewFlowLayoutInvalidationContext](uicollectionviewflowlayoutinvalidationcontext.md)
  A set of properties for determining whether to recompute the size of items or their position in the layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout)*