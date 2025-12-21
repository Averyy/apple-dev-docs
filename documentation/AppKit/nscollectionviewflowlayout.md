# NSCollectionViewFlowLayout

**Framework**: AppKit  
**Kind**: class

A layout that organizes items into a flexible and configurable arrangement.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
class NSCollectionViewFlowLayout
```

#### Overview

In a flow layout, the first item is positioned in the top-left corner and other items are laid out either horizontally or vertically based on the scroll direction, which is configurable. Items may be the same size or different sizes, and you may use the flow layout object or the collection view’s delegate object to specify the size of items and the spacing around them. The flow layout also lets you specify custom header and footer views for each section.

You can use an [`NSCollectionViewFlowLayout`](nscollectionviewflowlayout.md) object as-is or subclass it to modify more aspects of the layout behavior. There are several ways to customize the basic layout behavior that do not require subclassing. For example, you can use a delegate object to change the size and spacing of items dynamically. Subclassing is appropriate for more advanced layout changes, such as adding supplementary views or decoration views, supporting custom layout attributes, or customizing the layout animations when inserting or deleting items.

##### Configuring a Collection View to Use a Flow Layout

You can configure a collection view to use a flow layout object programmatically or at design time:

- At design time, set the Layout attribute of your collection view to Flow.
- Create an `NSCollectionViewFlowLayout` object programmatically and assign it to the collection view’s [`collectionViewLayout`](nscollectionview/collectionviewlayout.md) property.

Normally, you specify the size of items and their spacing using the properties of this class. If you want to customize the values for your items, implement the methods of the [`NSCollectionViewDelegateFlowLayout`](nscollectionviewdelegateflowlayout.md) protocol in the object assigned as the collection view’s [`delegate`](nscollectionview/delegate.md). The delegate methods let you adjust layout information dynamically and change the values later as needed. If you do not provide a delegate, the flow layout object uses the same values for all items.

For more information about customizing the layout dynamically using a delegate, see [`NSCollectionViewDelegateFlowLayout`](nscollectionviewdelegateflowlayout.md).

##### Adding Header and Footer Views to Sections

The flow layout supports custom header and footer views for each section, displaying them as supplementary views in the layout. [`Figure 1`](nscollectionviewflowlayout#1965629.md) shows how header and footer views are presented in your layout. The header view appears above the items in a section and the footer view appears below those items.

![None](https://docs-assets.developer.apple.com/published/a62776fd8038549a225bc69c1df45a04/media-1965629%402x.png)

The size of the header and footer views is configurable using the [`headerReferenceSize`](nscollectionviewflowlayout/headerreferencesize.md) and [`footerReferenceSize`](nscollectionviewflowlayout/footerreferencesize.md) properties of this class or using the delegate object. For a vertically scrolling flow layout, the header and footer views span the width of the collection view and the height is based on the values you specify. For a horizontal layout, the footers span the height of the collection view and the width is configurable.

To add header or footer views to your flow layout, you must do the following:

1. Register your header and footer views using the [`register(_:forSupplementaryViewOfKind:withIdentifier:)`](nscollectionview/register(_:forsupplementaryviewofkind:withidentifier:)-3dqa.md) or [`register(_:forSupplementaryViewOfKind:withIdentifier:)`](nscollectionview/register(_:forsupplementaryviewofkind:withidentifier:)-7gvf2.md) method.
2. Implement the [`collectionView(_:viewForSupplementaryElementOfKind:at:)`](nscollectionviewdatasource/collectionview(_:viewforsupplementaryelementofkind:at:).md) method in your collection view’s data source object.

When registering your header view, specify [`elementKindSectionHeader`](nscollectionview/elementkindsectionheader.md) for the kind string. When registering your footer view, specify the [`elementKindSectionFooter`](nscollectionview/elementkindsectionfooter.md) string. You also pass those strings to the [`makeSupplementaryView(ofKind:withIdentifier:for:)`](nscollectionview/makesupplementaryview(ofkind:withidentifier:for:).md) method when creating new views in your data source object.

You configure the contents of your header and footer views in the same way you configure items. Use your app data to configure the content of the supplementary view and its subviews. When you want to update the content in a header or footer, call the [`reloadSections(_:)`](nscollectionview/reloadsections(_:).md) method and force the collection view to update the section, including its headers and footers. Reloading the section is safer than maintaining references to the views themselves because of how the collection view recycles views. If you do want to update views directly, use the methods of the [`NSCollectionViewDelegate`](nscollectionviewdelegate.md) protocol to track when your views are added and removed from the collection view.

##### Understanding How the Flow Layout Is Generated

The flow layout builds its grid dynamically, using the item size and spacing information to place items sequentially into rows (for a vertically scrolling layout) or columns (for a horizontally scrolling layout). The number of items displayed in each row or column is determined by the collection view’s size and the size of the items in that row. When items have a uniform size, the number of items in each row is the same, but when items are different sizes, some rows may contain more or fewer items. [`Figure 2`](nscollectionviewflowlayout#1965630.md) illustrates how the flow layout places items in a row until there is no more space and then begins a new row and continues the layout process.

![None](https://docs-assets.developer.apple.com/published/58a0ee07f5b8a63d901639753d08e975/media-1965630%402x.png)

The flow layout follows a specific set of steps to determine the size of each item. Whenever possible, the flow layout uses previously calculated information. When that information is not available, it falls back on other techniques to retrieve the size of the item. Specifically, the flow layout takes the following steps, stopping when it acquires a valid item size:

1. Get the size of the item from the already computed layout attributes.
2. Call the [`collectionView(_:layout:sizeForItemAt:)`](nscollectionviewdelegateflowlayout/collectionview(_:layout:sizeforitemat:).md) method of the delegate to get the item size.
3. Use the [`estimatedItemSize`](nscollectionviewflowlayout/estimateditemsize.md) property, if it is not set to [`NSZeroSize`](https://developer.apple.com/documentation/Foundation/NSZeroSize).
4. Use the [`itemSize`](nscollectionviewflowlayout/itemsize.md) property to get the size.

Individual spacing between items and between different lines of items is controlled by the properties of this class and the delegate. For line spacing, the largest item in the line defines the line’s height and thereby controls the spacing between that line and other lines. The minimum inter-item spacing controls only how many items are placed on the line, and does not set the spacing between items.

##### Subclassing Notes

When you want to do more than specify the size or spacing of items, subclass `NSCollectionViewFlowLayout` and override the appropriate methods. When subclassing, the best approach is to take advantage of the built-in flow layout behavior and then make tweaks as needed.

###### Adding New Supplementary or Decoration Views to the Layout

The standard flow layout object supports only header and footer supplementary views for each section. To support additional supplementary views, or to add decoration views, you must override the following methods:

- [`layoutAttributesForElements(in:)`](nscollectionviewlayout/layoutattributesforelements(in:).md) (Required)
- [`layoutAttributesForItem(at:)`](nscollectionviewlayout/layoutattributesforitem(at:).md) (Required)
- [`layoutAttributesForSupplementaryView(ofKind:at:)`](nscollectionviewlayout/layoutattributesforsupplementaryview(ofkind:at:).md) (Required only if you are adding supplementary views)
- [`layoutAttributesForDecorationView(ofKind:at:)`](nscollectionviewlayout/layoutattributesfordecorationview(ofkind:at:).md) (Required only if you are adding decoration views)

Your implementations of these methods should adjust the position of items and views to accommodate your custom content. For each of your implementations, call `super` first so that you can modify the attributes returned by the default flow layout behavior before adding any custom layout attributes.

###### Tweaking the Layout Attributes

To tweak the flow layout algorithm, override the [`layoutAttributesForElements(in:)`](nscollectionviewlayout/layoutattributesforelements(in:).md) method and any other methods that return layout attributes that you need to modify. In each method, call `super` first and then modify the attributes returned by the default flow layout behavior.

###### Changing the Initial or Final Attributes of Elements

To customize the insertion or deletion animations performed by the layout, override some or all of the following methods:

- [`initialLayoutAttributesForAppearingItem(at:)`](nscollectionviewlayout/initiallayoutattributesforappearingitem(at:).md)
- [`initialLayoutAttributesForAppearingSupplementaryElement(ofKind:at:)`](nscollectionviewlayout/initiallayoutattributesforappearingsupplementaryelement(ofkind:at:).md)
- [`initialLayoutAttributesForAppearingDecorationElement(ofKind:at:)`](nscollectionviewlayout/initiallayoutattributesforappearingdecorationelement(ofkind:at:).md)
- [`finalLayoutAttributesForDisappearingItem(at:)`](nscollectionviewlayout/finallayoutattributesfordisappearingitem(at:).md)
- [`finalLayoutAttributesForDisappearingSupplementaryElement(ofKind:at:)`](nscollectionviewlayout/finallayoutattributesfordisappearingsupplementaryelement(ofkind:at:).md)
- [`finalLayoutAttributesForDisappearingDecorationElement(ofKind:at:)`](nscollectionviewlayout/finallayoutattributesfordisappearingdecorationelement(ofkind:at:).md)

In your custom implementations, specify the layout attributes for each item or view being inserted or deleted. The flow layout handles the creation of the appropriate animations, using the initial or final attributes that you provide. It is also recommended that you override the [`prepare(forCollectionViewUpdates:)`](nscollectionviewlayout/prepare(forcollectionviewupdates:).md) and [`finalizeCollectionViewUpdates()`](nscollectionviewlayout/finalizecollectionviewupdates().md) methods to track the insertions and deletions.

###### Supporting Custom Layout Attributes

Subclassing is required if you want the flow layout to manage attributes other than the size and visibility of items and views. If you subclass [`NSCollectionViewLayoutAttributes`](nscollectionviewlayoutattributes.md) and define additional layout attributes, you must also subclass `NSCollectionViewFlowLayout` to provide values for those attributes . In your flow layout subclass, override the following:

- [`layoutAttributesClass`](nscollectionviewlayout/layoutattributesclass.md)
- [`layoutAttributesForElements(in:)`](nscollectionviewlayout/layoutattributesforelements(in:).md)
- [`layoutAttributesForItem(at:)`](nscollectionviewlayout/layoutattributesforitem(at:).md)
- All other methods that return layout attributes

The implementations of your custom methods should set the values of any layout attributes that you define. Call `super` first to retrieve the default layout attributes objects and then modify the returned objects by adding your custom data.

For more information about defining custom layout attributes, see [`NSCollectionViewLayoutAttributes`](nscollectionviewlayoutattributes.md).

## Topics

### Configuring the Scroll Direction
- [var scrollDirection: NSCollectionView.ScrollDirection](nscollectionviewflowlayout/scrolldirection.md)
  The scroll direction of the layout.
### Configuring the Item Spacing
- [var minimumLineSpacing: CGFloat](nscollectionviewflowlayout/minimumlinespacing.md)
  The minimum spacing (in points) to use between rows or columns.
- [var minimumInteritemSpacing: CGFloat](nscollectionviewflowlayout/minimuminteritemspacing.md)
  The minimum spacing (in points) to use between items in the same row or column.
- [var estimatedItemSize: NSSize](nscollectionviewflowlayout/estimateditemsize.md)
  The estimated size of items in the collection view.
- [var itemSize: NSSize](nscollectionviewflowlayout/itemsize.md)
  The default size to use for items.
- [var sectionInset: NSEdgeInsets](nscollectionviewflowlayout/sectioninset.md)
  The margins used to lay out content in a section.
### Configuring the Supplementary Views
- [var headerReferenceSize: NSSize](nscollectionviewflowlayout/headerreferencesize.md)
  The default size to use for section headers.
- [var footerReferenceSize: NSSize](nscollectionviewflowlayout/footerreferencesize.md)
  The default size to use for section footers.
### Constants
- [NSCollectionView.ScrollDirection](nscollectionview/scrolldirection.md)
  Constants indicating the scrolling direction for the layout.
- [Flow Layout Elements](flow-layout-elements.md)
  Constants for specifying the types of supplementary views that can be displayed by a flow layout.
### Instance Properties
- [var sectionFootersPinToVisibleBounds: Bool](nscollectionviewflowlayout/sectionfooterspintovisiblebounds.md)
- [var sectionHeadersPinToVisibleBounds: Bool](nscollectionviewflowlayout/sectionheaderspintovisiblebounds.md)
### Instance Methods
- [func collapseSection(at: Int)](nscollectionviewflowlayout/collapsesection(at:).md)
- [func expandSection(at: Int)](nscollectionviewflowlayout/expandsection(at:).md)
- [func section(atIndexIsCollapsed: Int) -> Bool](nscollectionviewflowlayout/section(atindexiscollapsed:).md)

## Relationships

### Inherits From
- [NSCollectionViewLayout](nscollectionviewlayout.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Implementing modern collection views](../UIKit/implementing-modern-collection-views.md)
  Bring compositional layouts to your app and simplify updating your user interface with diffable data sources.
- [protocol NSCollectionViewDelegateFlowLayout](nscollectionviewdelegateflowlayout.md)
  A set of methods that a delegate implements to provide layout information to a flow layout object in a collection view.
- [class NSCollectionViewGridLayout](nscollectionviewgridlayout.md)
  A layout that displays a single section of items in a row and column grid.
- [class NSCollectionViewTransitionLayout](nscollectionviewtransitionlayout.md)
  An object that implements custom behaviors when changing from one layout to another in a collection view.
- [class NSCollectionViewLayoutAttributes](nscollectionviewlayoutattributes.md)
  An object that contains layout-related attributes for an element in a collection view.
- [class NSCollectionViewLayout](nscollectionviewlayout.md)
  An abstract base class that you subclass and use to generate layout information for a collection view.
- [class NSCollectionViewCompositionalLayout](nscollectionviewcompositionallayout.md)
  A layout object that lets you combine items in highly adaptive and flexible visual arrangements.
- [class NSCollectionViewCompositionalLayoutConfiguration](nscollectionviewcompositionallayoutconfiguration.md)
  An object that defines scroll direction, section spacing, and headers or footers for the layout.
- [typealias NSCollectionViewCompositionalLayoutSectionProvider](nscollectionviewcompositionallayoutsectionprovider.md)
  A closure that creates and returns each of the layout’s sections.
- [enum NSCollectionLayoutSectionOrthogonalScrollingBehavior](nscollectionlayoutsectionorthogonalscrollingbehavior.md)
  The scrolling behavior of the layout’s sections in relation to the main layout axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewflowlayout)*