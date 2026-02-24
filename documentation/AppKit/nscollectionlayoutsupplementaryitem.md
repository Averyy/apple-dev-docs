# NSCollectionLayoutSupplementaryItem

**Framework**: AppKit  
**Kind**: class

An object used to add an extra visual decoration to an item in a collection view.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class NSCollectionLayoutSupplementaryItem
```

#### Overview

You use supplementary items to attach additional views to your content. For example, you might attach a badge to an item or a frame around a group. A supplementary item follows the index path of the item it’s attached to.

If you want to create a header or footer for your layout or its sections, use a boundary supplementary item (<````NSCollectionLayoutBoundarySupplementaryItem``>) instead.

Each type of supplementary item must have a unique element kind. Consider tracking these strings together in a way that makes it straightforward to identify each element, for example:

**Swift**:

```swift
struct ElementKind {
    static let badge = "badge-element-kind"
    static let background = "background-element-kind"
    static let sectionHeader = "section-header-element-kind"
    static let sectionFooter = "section-footer-element-kind"
    static let layoutHeader = "layout-header-element-kind"
    static let layoutFooter = "layout-footer-element-kind"
}
```

**Objective-C**:

```objc
NSString* const ELEMENT_KIND_BADGE = @"badge-element-kind";
NSString* const ELEMENT_KIND_BACKGROUND = @"background-element-kind";
NSString* const ELEMENT_KIND_SECTION_HEADER = @"section-header-element-kind";
NSString* const ELEMENT_KIND_SECTION_FOOTER = @"section-footer-element-kind";
NSString* const ELEMENT_KIND_LAYOUT_HEADER = @"layout-header-element-kind";
NSString* const ELEMENT_KIND_LAYOUT_FOOTER = @"layout-footer-element-kind";
```

Add supplementary items to an item by passing in an array of supplementary items when you construct the item:

**Swift**:

```swift
let itemSize = NSCollectionLayoutSize(widthDimension: .absolute(44),
                                     heightDimension: .absolute(44))
    
let badgeAnchor = NSCollectionLayoutAnchor(edges: [.top, .trailing],
                                fractionalOffset: CGPoint(x: 0.3, y: -0.3))
   
let badgeSize = NSCollectionLayoutSize(widthDimension: .absolute(20),
                                      heightDimension: .absolute(20))
    
let badge = NSCollectionLayoutSupplementaryItem(layoutSize: badgeSize,
                                               elementKind: ElementKind.badge,
                                           containerAnchor: badgeAnchor)
    
let item = NSCollectionLayoutItem(layoutSize: itemSize,
                          supplementaryItems: [badge])
```

**Objective-C**:

```objc
NSCollectionLayoutSize *itemSize = [NSCollectionLayoutSize sizeWithWidthDimension:[NSCollectionLayoutDimension absoluteDimension:44.0] heightDimension:[NSCollectionLayoutDimension absoluteDimension:44.0]];

NSCollectionLayoutAnchor *badgeAnchor = [NSCollectionLayoutAnchor layoutAnchorWithEdges: NSDirectionalRectEdgeTop|NSDirectionalRectEdgeTrailing fractionalOffset:CGPointMake(0.3, -0.3)];

NSCollectionLayoutSize *badgeSize = [NSCollectionLayoutSize sizeWithWidthDimension:[NSCollectionLayoutDimension absoluteDimension:20.0] heightDimension:[NSCollectionLayoutDimension absoluteDimension:20.0]];

NSCollectionLayoutSupplementaryItem *badge = [NSCollectionLayoutSupplementaryItem supplementaryItemWithLayoutSize:badgeSize elementKind:ELEMENT_KIND_BADGE containerAnchor:badgeAnchor];

NSCollectionLayoutItem *item = [NSCollectionLayoutItem itemWithLayoutSize:itemSize supplementaryItems:@[badge]];

```

## Topics

### Creating a supplementary item
- [convenience init(layoutSize: NSCollectionLayoutSize, elementKind: String, containerAnchor: NSCollectionLayoutAnchor)](nscollectionlayoutsupplementaryitem/init(layoutsize:elementkind:containeranchor:).md)
  Creates a supplementary item of the specified size and element kind, with an anchor relative to a container.
- [convenience init(layoutSize: NSCollectionLayoutSize, elementKind: String, containerAnchor: NSCollectionLayoutAnchor, itemAnchor: NSCollectionLayoutAnchor)](nscollectionlayoutsupplementaryitem/init(layoutsize:elementkind:containeranchor:itemanchor:).md)
  Creates a supplementary item of the specified size and element kind, an anchor relative to a container, and an anchor relative to an item.
### Getting the anchors
- [var itemAnchor: NSCollectionLayoutAnchor?](nscollectionlayoutsupplementaryitem/itemanchor.md)
  The anchor between the supplementary item and the item it’s attached to.
- [var containerAnchor: NSCollectionLayoutAnchor](nscollectionlayoutsupplementaryitem/containeranchor.md)
  The anchor between the supplementary item and the container it’s attached to.
### Getting the element kind
- [var elementKind: String](nscollectionlayoutsupplementaryitem/elementkind.md)
  A string that identifies the type of supplementary item.
### Specifying stacking order
- [var zIndex: Int](nscollectionlayoutsupplementaryitem/zindex.md)
  The vertical stacking order of the supplementary item in relation to other items in the section.

## Relationships

### Inherits From
- [NSCollectionLayoutItem](nscollectionlayoutitem.md)
### Inherited By
- [NSCollectionLayoutBoundarySupplementaryItem](nscollectionlayoutboundarysupplementaryitem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSCollectionLayoutBoundarySupplementaryItem](nscollectionlayoutboundarysupplementaryitem.md)
  An object used to add headers or footers to a collection view.
- [class NSCollectionLayoutDecorationItem](nscollectionlayoutdecorationitem.md)
  An object used to add a background to a section of a collection view.
- [class NSCollectionLayoutAnchor](nscollectionlayoutanchor.md)
  An object that defines how to attach a supplementary item to an item in a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutsupplementaryitem)*