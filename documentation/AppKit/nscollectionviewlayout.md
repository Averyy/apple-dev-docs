# NSCollectionViewLayout

**Framework**: AppKit  
**Kind**: class

An abstract base class that you subclass and use to generate layout information for a collection view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
class NSCollectionViewLayout
```

#### Overview

The job of a layout object is to perform the calculations needed to determine the placement and appearance of items, supplementary views, and other content in the collection view. The layout object does not apply the layout attributes it generates to the views in your interface. Instead, it passes those layout attributes to the collection view, which then creates the needed views and applies the layout attributes to them.

You do not create instances of this class directly. Instead, you create instances of one of its subclasses and associate that object with your collection view either programmatically (using the [`collectionViewLayout`](nscollectionview/collectionviewlayout.md) property) or at design time in Interface Builder. Changing the layout object of a collection view forces an immediate update of the layout information.

Collection views support many different types of elements, most of which are visual and all of which require layout attributes:

-  are the main elements managed by the layout. Each item represents a single piece of data in the collection view. A collection view can have a single group of items or it can divide the items into multiple sections.
-  are optional views associated with a specific section. The layout object defines the placement and use of supplementary views. For example, grid and flow layouts use supplementary views to implement headers and footers for each section. Supplementary views cannot be selected by the user.
-  are visual adornments used to implement themes or to present visual content that is unrelated to the data being managed by the collection view. Decoration views are optional and the layout object defines their use and placement.
-  supply a drop target for dragged content. Gaps do not have a direct visual representation, but they do have layout attributes, which the collection view uses for hit testing. The layout object provides attributes for inter-item gaps only when asked to do so.

Each concrete layout object defines a specific organization for the contained elements and provides the appropriate layout attributes. The placement and appearance of items is determined entirely by the layout object. The [`NSCollectionViewFlowLayout`](nscollectionviewflowlayout.md) and [`NSCollectionViewGridLayout`](nscollectionviewgridlayout.md) subclasses define variants of a grid-based layout, but you can create custom layouts that arrange elements in different ways. For example, you might define a layout class that arranges items in a circle or define a class that groups items into stacks that resemble a pile of photos on a table.

##### Subclassing Notes

Layout objects provide information about the position and visual state of elements in the collection view. When defining an `NSCollectionViewLayout` subclass, first have an idea for how items in your layout will appear onscreen. Layouts should provide a well-defined organization for their elements and should not morph between different organizations. If you want your collection view to change how it organizes elements, define separate layout objects for each organization and switch between them at runtime.

Remember that a layout object does not directly create the views for which it provides layout information. Creation of the views is handled by the collection view, which creates them with the help of its data source object. The layout object only assists the collection view by providing information about the position and appearance of the views that the collection view creates.

Your `NSCollectionViewLayout` subclass should be mostly self contained and should not rely on the collection view. Layout objects can retrieve the number of sections and items from the collection view, but you should not design layout objects that require knowledge of the data being displayed. The separation of the layout information from the displayed data offers flexibility and makes it easier to reuse layout objects.

###### Methods to Override

When defining a custom layout class, always override the following methods and properties:

- [`prepare()`](nscollectionviewlayout/prepare().md)
- [`collectionViewContentSize`](nscollectionviewlayout/collectionviewcontentsize.md)
- [`layoutAttributesForElements(in:)`](nscollectionviewlayout/layoutattributesforelements(in:).md)
- [`layoutAttributesForItem(at:)`](nscollectionviewlayout/layoutattributesforitem(at:).md)
- [`layoutAttributesForSupplementaryView(ofKind:at:)`](nscollectionviewlayout/layoutattributesforsupplementaryview(ofkind:at:).md) (if your layout supports supplementary views)
- [`layoutAttributesForDecorationView(ofKind:at:)`](nscollectionviewlayout/layoutattributesfordecorationview(ofkind:at:).md) (if your layout supports decoration views)
- [`shouldInvalidateLayout(forBoundsChange:)`](nscollectionviewlayout/shouldinvalidatelayout(forboundschange:).md)

These methods provide the fundamental layout information that the collection view needs to configure the items and other views that it displays. Layout objects need to implement only the methods associated with the types of elements they support. So if your layout object does not include decoration views, you do not need to implement the [`layoutAttributesForDecorationView(ofKind:at:)`](nscollectionviewlayout/layoutattributesfordecorationview(ofkind:at:).md) method or any other methods relating to decoration views.

In addition to the preceding methods, it is recommended that you implement several other methods in your custom layout objects. The insertion or deletion of items usually involves animations to move those items into position. Providing initial or final layout attributes makes your layout more engaging by improving the animations associated with the insertion or deletion of items. Other methods provide additional support for layout-related behaviors.

- [`initialLayoutAttributesForAppearingItem(at:)`](nscollectionviewlayout/initiallayoutattributesforappearingitem(at:).md)
- [`initialLayoutAttributesForAppearingSupplementaryElement(ofKind:at:)`](nscollectionviewlayout/initiallayoutattributesforappearingsupplementaryelement(ofkind:at:).md)
- [`initialLayoutAttributesForAppearingDecorationElement(ofKind:at:)`](nscollectionviewlayout/initiallayoutattributesforappearingdecorationelement(ofkind:at:).md)
- [`finalLayoutAttributesForDisappearingItem(at:)`](nscollectionviewlayout/finallayoutattributesfordisappearingitem(at:).md)
- [`finalLayoutAttributesForDisappearingSupplementaryElement(ofKind:at:)`](nscollectionviewlayout/finallayoutattributesfordisappearingsupplementaryelement(ofkind:at:).md)
- [`finalLayoutAttributesForDisappearingDecorationElement(ofKind:at:)`](nscollectionviewlayout/finallayoutattributesfordisappearingdecorationelement(ofkind:at:).md)
- [`layoutAttributesForDropTarget(at:)`](nscollectionviewlayout/layoutattributesfordroptarget(at:).md) (if your layout supports dropping content between items
- [`layoutAttributesForInterItemGap(before:)`](nscollectionviewlayout/layoutattributesforinteritemgap(before:).md) (if your layout supports dropping content in gaps between elements)

###### Understanding the Layout Process

Although the collection view drives the layout process, layout objects do all the work of calculating the layout information used during that process. The layout object acts as a semi-passive utility object, computing the location of elements and returning layout attributes only when asked to do so. Layout occurs when the collection view is first displayed and reoccurs whenever all or part of the layout is marked as invalid.

During the layout process, the collection view calls several methods of your layout object to gather information. In particular, it calls three very important methods, whose implementations drive the core layout behavior.

- Use the [`prepare()`](nscollectionviewlayout/prepare().md) method to perform your initial layout calculations. These calculations provide the basis for everything the layout object does later.
- Use the [`collectionViewContentSize`](nscollectionviewlayout/collectionviewcontentsize.md) method to return the smallest rectangle that completely encloses all of the elements in the collection view. Use the calculations from your [`prepare()`](nscollectionviewlayout/prepare().md) method to specify this rectangle.
- Use the [`layoutAttributesForElements(in:)`](nscollectionviewlayout/layoutattributesforelements(in:).md) method to return the layout attributes for all elements in the specified rectangle. The collection view typically requests only the subset of visible elements, but may include elements that are just offscreen.

The [`prepare()`](nscollectionviewlayout/prepare().md) method is your chance to perform the main calculations associated with the layout process. Use this method to generate an initial list of layout attributes for your content. For example, use this method to calculate the frame rectangles of all elements in the collection view. Performing all of these calculations up front and caching the resulting data is often simpler than trying to compute attributes for individual items later.

In addition to the [`layoutAttributesForElements(in:)`](nscollectionviewlayout/layoutattributesforelements(in:).md) method, the collection view may call other methods to retrieve layout attributes for specific items. By performing your calculations in advance, your implementations of those methods should be able to return cached information without having to recompute that information first. The only time your layout object needs to recompute its layout information is when your app invalidates the layout. For example, you might invalidate the layout when the user inserts or deletes items.

###### Adding Decoration Views to Your Layout

Layouts can use decoration views to create a specific visual appearance for the collection view’s content. Decoration views are fully configured visual elements that the layout object provides. When defining your own custom layout objects, you might use decoration views to provide a dynamic background or add visual styling in and around the items of the collection view. The layout object defines what decoration views are needed and registers an appropriate class or nib file for each view using the [`register(_:forDecorationViewOfKind:)`](nscollectionviewlayout/register(_:fordecorationviewofkind:)-44qmc.md) or [`register(_:forDecorationViewOfKind:)`](nscollectionviewlayout/register(_:fordecorationviewofkind:)-7z7uf.md) method.

To create a decoration view, return an appropriate layout attributes object from your layout object’s  [`layoutAttributesForElements(in:)`](nscollectionviewlayout/layoutattributesforelements(in:).md) method. When the collection view receives attributes for a decoration view, it creates that view using the class or nib file that your layout object registered. Because the collection view creates them, decoration views must be fully configured at registration time. You cannot add content to a decoration view or change its configuration later.

###### Optimizing Layout Performance Using Invalidation Contexts

When designing custom layouts, you can improve performance by updating only the portions of your layout that actually changed. The [`invalidateLayout()`](nscollectionviewlayout/invalidatelayout().md) method forces the collection view to throw away all of its layout information and recompute it, which is inefficient if most of the layout has not changed. A better way to update your layout is using the [`invalidateLayout(with:)`](nscollectionviewlayout/invalidatelayout(with:).md) method, which uses the provided context object to invalidate only the parts of the layout that changed.

Support for invalidation contexts must be built into the implementation of your layout object. At a minimum, you must override the [`invalidateLayout(with:)`](nscollectionviewlayout/invalidatelayout(with:).md) method and use it to mark the parts of your layout that changed. You might do this by setting flags or throwing away cached layout attributes for the changed elements. Your [`invalidateLayout(with:)`](nscollectionviewlayout/invalidatelayout(with:).md) method should also call `super` so that the collection view can initiate the layout update process at a future time.

If your layout object supports more fine-grained invalidation than the [`NSCollectionViewLayoutInvalidationContext`](nscollectionviewlayoutinvalidationcontext.md) class provides, you can subclass and add your invalidation information there. If you define a custom context class, override the [`invalidationContextClass`](nscollectionviewlayout/invalidationcontextclass.md) property in your layout object so that the collection view knows which class to instantiate. Similarly, other parts of your app should create instances of your custom context class and use them to invalidate the layout.

## Topics

### Getting the Collection View
- [var collectionView: NSCollectionView?](nscollectionviewlayout/collectionview.md)
  The collection view object currently using this layout.
### Providing Layout Information
- [class var layoutAttributesClass: AnyClass](nscollectionviewlayout/layoutattributesclass.md)
  Returns the class to use for layout attribute objects
- [func prepare()](nscollectionviewlayout/prepare.md)
  Prepares the layout object to begin laying out content.
- [var collectionViewContentSize: NSSize](nscollectionviewlayout/collectionviewcontentsize.md)
  The width and height of the collection view’s contents.
- [func layoutAttributesForElements(in: NSRect) -> [NSCollectionViewLayoutAttributes]](nscollectionviewlayout/layoutattributesforelements(in:).md)
  Returns the layout attribute objects for all items and views in the specified rectangle.
- [func layoutAttributesForItem(at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/layoutattributesforitem(at:).md)
  Returns the layout attributes for the item at the specified index path.
- [func layoutAttributesForSupplementaryView(ofKind: NSCollectionView.SupplementaryElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/layoutattributesforsupplementaryview(ofkind:at:).md)
  Returns the layout attributes of the supplementary view at the specified location in your layout.
- [func layoutAttributesForDecorationView(ofKind: NSCollectionView.DecorationElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/layoutattributesfordecorationview(ofkind:at:).md)
  Returns the layout attributes of the decoration view at the specified location in your layout.
- [func layoutAttributesForDropTarget(at: NSPoint) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/layoutattributesfordroptarget(at:).md)
  Returns layout attributes for the drop target at the specified point.
- [func layoutAttributesForInterItemGap(before: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/layoutattributesforinteritemgap(before:).md)
  Returns layout attributes for the inter-item gap at the specified location in your layout.
- [func targetContentOffset(forProposedContentOffset: NSPoint) -> NSPoint](nscollectionviewlayout/targetcontentoffset(forproposedcontentoffset:).md)
  Returns the offset value to use after an animated layout update or change.
- [func targetContentOffset(forProposedContentOffset: NSPoint, withScrollingVelocity: NSPoint) -> NSPoint](nscollectionviewlayout/targetcontentoffset(forproposedcontentoffset:withscrollingvelocity:).md)
  Returns the offset value to use for the collection view’s content at the end of scrolling.
### Responding to Collection View Updates
- [func prepare(forCollectionViewUpdates: [NSCollectionViewUpdateItem])](nscollectionviewlayout/prepare(forcollectionviewupdates:).md)
  Performs needed tasks before items are inserted, deleted, or moved within the collection view.
- [func finalizeCollectionViewUpdates()](nscollectionviewlayout/finalizecollectionviewupdates.md)
  Performs needed steps after items are inserted, deleted, or moved within a collection view.
- [func indexPathsToInsertForSupplementaryView(ofKind: NSCollectionView.SupplementaryElementKind) -> Set<IndexPath>](nscollectionviewlayout/indexpathstoinsertforsupplementaryview(ofkind:).md)
  Returns the index paths for any supplementary views that the layout object wants to add to the collection view.
- [func indexPathsToInsertForDecorationView(ofKind: NSCollectionView.DecorationElementKind) -> Set<IndexPath>](nscollectionviewlayout/indexpathstoinsertfordecorationview(ofkind:).md)
  Returns the index paths for any decoration views that the layout object wants to add to the collection view.
- [func initialLayoutAttributesForAppearingItem(at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/initiallayoutattributesforappearingitem(at:).md)
  Returns the starting layout information for an item being inserted into the collection view.
- [func initialLayoutAttributesForAppearingSupplementaryElement(ofKind: NSCollectionView.SupplementaryElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/initiallayoutattributesforappearingsupplementaryelement(ofkind:at:).md)
  Returns the starting layout information for a supplementary view being added to the collection view.
- [func initialLayoutAttributesForAppearingDecorationElement(ofKind: NSCollectionView.DecorationElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/initiallayoutattributesforappearingdecorationelement(ofkind:at:).md)
  Returns the starting layout information for a decoration view being added to the collection view.
- [func indexPathsToDeleteForSupplementaryView(ofKind: NSCollectionView.SupplementaryElementKind) -> Set<IndexPath>](nscollectionviewlayout/indexpathstodeleteforsupplementaryview(ofkind:).md)
  Returns the index paths for any supplementary views that the layout object wants to remove from the collection view.
- [func indexPathsToDeleteForDecorationView(ofKind: NSCollectionView.DecorationElementKind) -> Set<IndexPath>](nscollectionviewlayout/indexpathstodeletefordecorationview(ofkind:).md)
  Returns index paths for any decoration views that the layout object wants to remove from the collection view.
- [func finalLayoutAttributesForDisappearingItem(at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/finallayoutattributesfordisappearingitem(at:).md)
  Returns the ending layout information for an item being removed from the collection view.
- [func finalLayoutAttributesForDisappearingSupplementaryElement(ofKind: NSCollectionView.SupplementaryElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/finallayoutattributesfordisappearingsupplementaryelement(ofkind:at:).md)
  Returns the ending layout information for a supplementary view being removed from the collection view.
- [func finalLayoutAttributesForDisappearingDecorationElement(ofKind: NSCollectionView.DecorationElementKind, at: IndexPath) -> NSCollectionViewLayoutAttributes?](nscollectionviewlayout/finallayoutattributesfordisappearingdecorationelement(ofkind:at:).md)
  Returns the ending layout information for a decoration view being removed from the collection view.
### Invalidating the Layout
- [func invalidateLayout()](nscollectionviewlayout/invalidatelayout.md)
  Invalidates all layout information and triggers a layout update.
- [func invalidateLayout(with: NSCollectionViewLayoutInvalidationContext)](nscollectionviewlayout/invalidatelayout(with:).md)
  Invalidates specific parts of the layout using the specified context object.
- [class var invalidationContextClass: AnyClass](nscollectionviewlayout/invalidationcontextclass.md)
  Returns the class to use when creating an invalidation context object for the layout.
- [func shouldInvalidateLayout(forBoundsChange: NSRect) -> Bool](nscollectionviewlayout/shouldinvalidatelayout(forboundschange:).md)
  Returns a Boolean indicating whether a bounds change triggers a layout update.
- [func shouldInvalidateLayout(forPreferredLayoutAttributes: NSCollectionViewLayoutAttributes, withOriginalAttributes: NSCollectionViewLayoutAttributes) -> Bool](nscollectionviewlayout/shouldinvalidatelayout(forpreferredlayoutattributes:withoriginalattributes:).md)
  Returns a Boolean indicating whether changes to a cell’s layout attributes trigger a larger layout update.
- [func invalidationContext(forBoundsChange: NSRect) -> NSCollectionViewLayoutInvalidationContext](nscollectionviewlayout/invalidationcontext(forboundschange:).md)
  Returns an invalidation context object that defines the portions of the layout that need to be updated.
- [func invalidationContext(forPreferredLayoutAttributes: NSCollectionViewLayoutAttributes, withOriginalAttributes: NSCollectionViewLayoutAttributes) -> NSCollectionViewLayoutInvalidationContext](nscollectionviewlayout/invalidationcontext(forpreferredlayoutattributes:withoriginalattributes:).md)
  Returns an invalidation context object that defines the portions of the layout that need to be updated.
### Coordinating Animated Changes
- [func prepare(forAnimatedBoundsChange: NSRect)](nscollectionviewlayout/prepare(foranimatedboundschange:).md)
  Prepares the layout object for animated changes to the collection view’s bounds or for the insertion or deletion of items.
- [func finalizeAnimatedBoundsChange()](nscollectionviewlayout/finalizeanimatedboundschange.md)
  Cleans up after any animated changes to the collection view’s bounds or after the insertion or deletion of items.
### Registering Decoration Views
- [func register(AnyClass?, forDecorationViewOfKind: NSCollectionView.DecorationElementKind)](nscollectionviewlayout/register(_:fordecorationviewofkind:)-44qmc.md)
  Registers a class to use when creating the layout’s decoration views.
- [func register(NSNib?, forDecorationViewOfKind: NSCollectionView.DecorationElementKind)](nscollectionviewlayout/register(_:fordecorationviewofkind:)-7z7uf.md)
  Registers a nib file to use when creating the layout’s decoration views.
### Transitioning Between Layouts
- [func prepareForTransition(from: NSCollectionViewLayout)](nscollectionviewlayout/preparefortransition(from:).md)
  Prepares the layout object to be installed in the collection view.
- [func prepareForTransition(to: NSCollectionViewLayout)](nscollectionviewlayout/preparefortransition(to:).md)
  Prepares the layout object to be uninstalled from the collection view.
- [func finalizeLayoutTransition()](nscollectionviewlayout/finalizelayouttransition.md)
  Performs any final steps related to a layout transition before the transition animations actually occur.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSCollectionViewCompositionalLayout](nscollectionviewcompositionallayout.md)
- [NSCollectionViewFlowLayout](nscollectionviewflowlayout.md)
- [NSCollectionViewGridLayout](nscollectionviewgridlayout.md)
- [NSCollectionViewTransitionLayout](nscollectionviewtransitionlayout.md)
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

- [Implementing modern collection views](../UIKit/implementing-modern-collection-views.md)
  Bring compositional layouts to your app and simplify updating your user interface with diffable data sources.
- [class NSCollectionViewFlowLayout](nscollectionviewflowlayout.md)
  A layout that organizes items into a flexible and configurable arrangement.
- [protocol NSCollectionViewDelegateFlowLayout](nscollectionviewdelegateflowlayout.md)
  A set of methods that a delegate implements to provide layout information to a flow layout object in a collection view.
- [class NSCollectionViewGridLayout](nscollectionviewgridlayout.md)
  A layout that displays a single section of items in a row and column grid.
- [class NSCollectionViewTransitionLayout](nscollectionviewtransitionlayout.md)
  An object that implements custom behaviors when changing from one layout to another in a collection view.
- [class NSCollectionViewLayoutAttributes](nscollectionviewlayoutattributes.md)
  An object that contains layout-related attributes for an element in a collection view.
- [class NSCollectionViewCompositionalLayout](nscollectionviewcompositionallayout.md)
  A layout object that lets you combine items in highly adaptive and flexible visual arrangements.
- [class NSCollectionViewCompositionalLayoutConfiguration](nscollectionviewcompositionallayoutconfiguration.md)
  An object that defines scroll direction, section spacing, and headers or footers for the layout.
- [typealias NSCollectionViewCompositionalLayoutSectionProvider](nscollectionviewcompositionallayoutsectionprovider.md)
  A closure that creates and returns each of the layout’s sections.
- [enum NSCollectionLayoutSectionOrthogonalScrollingBehavior](nscollectionlayoutsectionorthogonalscrollingbehavior.md)
  The scrolling behavior of the layout’s sections in relation to the main layout axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayout)*