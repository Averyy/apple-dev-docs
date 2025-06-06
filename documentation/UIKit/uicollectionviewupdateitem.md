# UICollectionViewUpdateItem

**Framework**: UIKit  
**Kind**: class

An object that describes a single change to make to an item in a collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICollectionViewUpdateItem
```

#### Overview

You don’t create instances of this class directly. When updating its content, the collection view object creates them and passes them to the layout object’s [`prepare(forCollectionViewUpdates:)`](uicollectionviewlayout/prepare(forcollectionviewupdates:).md) method, which can use them to prepare the layout object for the upcoming changes.

## Topics

### Accessing the item changes
- [var indexPathBeforeUpdate: IndexPath?](uicollectionviewupdateitem/indexpathbeforeupdate.md)
  The index path of the item before the update.
- [var indexPathAfterUpdate: IndexPath?](uicollectionviewupdateitem/indexpathafterupdate.md)
  The index path of the item after the update.
- [var updateAction: UICollectionViewUpdateItem.Action](uicollectionviewupdateitem/updateaction.md)
  The action being performed on the item.
- [UICollectionViewUpdateItem.Action](uicollectionviewupdateitem/action.md)
  Constants indicating the type of action being performed on an item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol NSCollectionLayoutVisibleItem](nscollectionlayoutvisibleitem.md)
  An item that’s currently visible within the bounds of a section.
- [typealias NSCollectionLayoutSectionVisibleItemsInvalidationHandler](nscollectionlayoutsectionvisibleitemsinvalidationhandler.md)
  A closure called before each layout cycle to allow modification of items in a section immediately before they’re displayed.
- [class UICollectionViewFocusUpdateContext](uicollectionviewfocusupdatecontext.md)
  A context object that stores information specific to a focus update in a collection view.
- [class UICollectionViewLayoutInvalidationContext](uicollectionviewlayoutinvalidationcontext.md)
  A context object that declares which parts of your layout need to be updated when the layout is invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewupdateitem)*