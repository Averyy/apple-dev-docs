# NSCollectionViewLayoutAttributes

**Framework**: AppKit  
**Kind**: class

An object that contains layout-related attributes for an element in a collection view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
class NSCollectionViewLayoutAttributes
```

#### Overview

During the layout, the layout object creates instances of [`NSCollectionViewLayoutAttributes`](nscollectionviewlayoutattributes.md) for each element displayed in the collection view. The layout attributes describe the position of an element and other information such as its alpha and position on the z axis. The collection view later applies the layout attributes to the onscreen elements.

The only time you interact with layout attribute objects is when you implement a custom layout, and the interactions are straightforward. When asked for layout attributes for a specific element, your layout object uses the methods of this class to create an appropriate instance of the class based on the type of the requested element. It then configures the properties of the object and returns it to the requester.

##### Subclassing Notes

If you implement a custom layout object and your layout object requires additional attributes, you can subclass `NSCollectionViewLayoutAttributes` and add custom properties to your subclass. In your subclass, be sure to do the following:

- Provide an [`init()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/init()) method with no parameters to initialize your subclass.
- Implement support for the [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying) protocol. The collection view caches layout attribute objects for later use.
- Override the inherited [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:)) method to perform any relevant equality checks.

Supporting equality checks is important because of how the collection view manages layout attributes. As an optimization, the collection view applies layout attributes only when they change. When the layout object returns a layout attributes object, the collection view checks to see if the new attributes are equal to any cached attributes. Therefore, if you want to include any new properties in the equality check, you must override the [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:)) method.

In addition to defining your `NSCollectionViewLayoutAttributes` subclass, override the [`layoutAttributesClass`](nscollectionviewlayout/layoutattributesclass.md) method of your layout object. That method is a funnel point for creating new layout attribute objects. Returning your custom class from that method ensures that the correct class is instantiated.

## Topics

### Creating Layout Attributes
- [convenience init(forItemWith: IndexPath)](nscollectionviewlayoutattributes/init(foritemwith:).md)
  Creates and returns a layout attributes object for the item at the specified index path.
- [convenience init(forSupplementaryViewOfKind: NSCollectionView.SupplementaryElementKind, with: IndexPath)](nscollectionviewlayoutattributes/init(forsupplementaryviewofkind:with:).md)
  Creates and returns a layout attributes object for a supplementary view based on the specified information.
- [convenience init(forDecorationViewOfKind: NSCollectionView.DecorationElementKind, with: IndexPath)](nscollectionviewlayoutattributes/init(fordecorationviewofkind:with:).md)
  Creates and returns a layout attributes object for a decoration view based on the specified information.
- [convenience init(forInterItemGapBefore: IndexPath)](nscollectionviewlayoutattributes/init(forinteritemgapbefore:).md)
  Creates and returns a layout attributes object for an inter-item gap view at the specified index path.
- [NSCollectionView.DecorationElementKind](nscollectionview/decorationelementkind.md)
### Identifying the Element
- [var representedElementCategory: NSCollectionElementCategory](nscollectionviewlayoutattributes/representedelementcategory.md)
  The type of the element.
- [var indexPath: IndexPath?](nscollectionviewlayoutattributes/indexpath.md)
  The index path of the element.
- [var representedElementKind: String?](nscollectionviewlayoutattributes/representedelementkind.md)
  The identifier for specific elements of your collection view interface.
- [class let elementKindInterItemGapIndicator: String](nscollectionview/elementkindinteritemgapindicator.md)
  The element kind string assigned to the attributes object when it represents an inter-item gap.
- [class let elementKindSectionFooter: String](nscollectionview/elementkindsectionfooter.md)
  A supplementary view that acts as a footer for a given section.
- [class let elementKindSectionHeader: String](nscollectionview/elementkindsectionheader.md)
  A supplementary view that acts as a header for a given section.
### Accessing the Layout Attributes
- [var frame: NSRect](nscollectionviewlayoutattributes/frame.md)
  The frame rectangle of the element.
- [var size: NSSize](nscollectionviewlayoutattributes/size.md)
  The size of the element.
- [var alpha: CGFloat](nscollectionviewlayoutattributes/alpha.md)
  The transparency of the element.
- [var isHidden: Bool](nscollectionviewlayoutattributes/ishidden.md)
  A Boolean value indicating whether the element is hidden.
- [var zIndex: Int](nscollectionviewlayoutattributes/zindex.md)
  The element’s position on the z axis.
### Constants
- [enum NSCollectionElementCategory](nscollectionelementcategory.md)
  Constants specifying the type of element in the collection view.
- [Inter-Item Gap Support](inter-item-gap-support.md)
  Constant for supporting inter-item gaps.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewlayoutattributes)*