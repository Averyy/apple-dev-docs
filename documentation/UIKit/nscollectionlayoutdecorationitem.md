# NSCollectionLayoutDecorationItem

**Framework**: UIKit  
**Kind**: class

An object used to add a background to a section of a collection view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class NSCollectionLayoutDecorationItem
```

#### Overview

Each type of decoration item must have a unique element kind. Consider tracking these strings together in a way that makes it straightforward to identify each element, for example:

Add a background to a section by setting that section’s [`decorationItems`](nscollectionlayoutsection/decorationitems.md) property:

## Topics

### Creating a background
- [class func background(elementKind: String) -> Self](nscollectionlayoutdecorationitem/background(elementkind:).md)
  Creates a section background with a string to identify the element kind.
### Getting the element kind
- [var elementKind: String](nscollectionlayoutdecorationitem/elementkind.md)
  A string that identifies the type of decoration item.
### Specifying stacking order
- [var zIndex: Int](nscollectionlayoutdecorationitem/zindex.md)
  The vertical stacking order of the decoration item in relation to other items in the section.

## Relationships

### Inherits From
- [NSCollectionLayoutItem](nscollectionlayoutitem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSCollectionLayoutAnchor](nscollectionlayoutanchor.md)
  An object that defines how to attach a supplementary item to an item in a collection view.
- [class NSCollectionLayoutSupplementaryItem](nscollectionlayoutsupplementaryitem.md)
  An object used to add an extra visual decoration to an item in a collection view.
- [class NSCollectionLayoutBoundarySupplementaryItem](nscollectionlayoutboundarysupplementaryitem.md)
  An object used to add headers or footers to a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutdecorationitem)*