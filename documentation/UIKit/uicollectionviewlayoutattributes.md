# UICollectionViewLayoutAttributes

**Framework**: UIKit  
**Kind**: class

A layout object that manages the layout-related attributes for a given item in a collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICollectionViewLayoutAttributes
```

#### Overview

Layout objects create instances of this class when asked to do so by the collection view. In turn, the collection view uses the layout information to position cells and supplementary views inside its bounds.

##### Subclassing Notes

In most cases, you use this class as-is. If you want to supplement the base layout attributes with custom layout attributes, you can subclass and define whatever properties you want to store the additional layout data. Because layout attribute objects may be copied by the collection view, make sure your subclass conforms to the [`NSCopying`](https://developer.apple.com/documentation/Foundation/NSCopying) protocol by implementing any methods appropriate for copying your custom attributes to new instances of your subclass. In addition to defining your subclass, your [`UICollectionReusableView`](uicollectionreusableview.md) objects need to implement the [`apply(_:)`](uicollectionreusableview/apply(_:).md) method so that they can apply any custom attributes at layout time.

If you subclass and implement any custom layout attributes, you must also override the inherited `isEqual:` method to compare the values of your properties. In iOS 7 and later, the collection view doesn’t apply layout attributes if those attributes have not changed. It determines whether the attributes have changed by comparing the old and new attribute objects using the `isEqual:` method. Because the default implementation of this method checks only the existing properties of this class, you must implement your own version of the method to compare any additional properties. If your custom properties are all equal, call `super` and return the resulting value at the end of your implementation.

## Topics

### Creating layout attributes
- [convenience init(forCellWith: IndexPath)](uicollectionviewlayoutattributes/init(forcellwith:).md)
  Creates and returns a layout attributes object that represents a cell with the specified index path.
- [convenience init(forSupplementaryViewOfKind: String, with: IndexPath)](uicollectionviewlayoutattributes/init(forsupplementaryviewofkind:with:).md)
  Creates and returns a layout attributes object that represents the specified supplementary view.
- [convenience init(forDecorationViewOfKind: String, with: IndexPath)](uicollectionviewlayoutattributes/init(fordecorationviewofkind:with:).md)
  Creates and returns a layout attributes object that represents the specified decoration view.
### Identifying the referenced item
- [var indexPath: IndexPath](uicollectionviewlayoutattributes/indexpath.md)
  The index path of the item in the collection view.
- [var representedElementKind: String?](uicollectionviewlayoutattributes/representedelementkind.md)
  The layout-specific identifier for the target view.
- [var representedElementCategory: UICollectionView.ElementCategory](uicollectionviewlayoutattributes/representedelementcategory.md)
  The type of the item.
- [UICollectionView.ElementCategory](uicollectionview/elementcategory.md)
  Constants specifying the type of view.
### Accessing the layout attributes
- [var frame: CGRect](uicollectionviewlayoutattributes/frame.md)
  The frame rectangle of the item.
- [var bounds: CGRect](uicollectionviewlayoutattributes/bounds.md)
  The bounds of the item.
- [var center: CGPoint](uicollectionviewlayoutattributes/center.md)
  The center point of the item.
- [var size: CGSize](uicollectionviewlayoutattributes/size.md)
  The size of the item.
- [var transform3D: CATransform3D](uicollectionviewlayoutattributes/transform3d.md)
  The 3D transform of the item.
- [var transform: CGAffineTransform](uicollectionviewlayoutattributes/transform.md)
  The affine transform of the item.
- [var alpha: CGFloat](uicollectionviewlayoutattributes/alpha.md)
  The transparency of the item.
- [var zIndex: Int](uicollectionviewlayoutattributes/zindex.md)
  Specifies the item’s position on the z axis.
- [var isHidden: Bool](uicollectionviewlayoutattributes/ishidden.md)
  Determines whether the item is currently displayed.

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
- [UIDynamicItem](uidynamicitem.md)

## See Also

- [Customizing collection view layouts](customizing-collection-view-layouts.md)
  Customize a view layout by changing the size of cells in the flow or implementing a mosaic style.
- [class UICollectionViewLayout](uicollectionviewlayout.md)
  An abstract base class for generating layout information for a collection view.
- [class UICollectionViewFlowLayout](uicollectionviewflowlayout.md)
  A layout object that organizes items into a grid with optional header and footer views for each section.
- [class UICollectionViewTransitionLayout](uicollectionviewtransitionlayout.md)
  A special type of layout object that lets you implement behaviors when changing from one layout to another in your collection view.
- [class UICollectionViewFlowLayoutInvalidationContext](uicollectionviewflowlayoutinvalidationcontext.md)
  A set of properties for determining whether to recompute the size of items or their position in the layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes)*