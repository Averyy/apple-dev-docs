# NSCollectionViewUpdateItem

**Framework**: AppKit  
**Kind**: class

A description of a single change to make to an item in a collection view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
class NSCollectionViewUpdateItem
```

#### Overview

You do not create instances of this class directly. When updating its content, the collection view object creates them and passes them to the layout object’s [`prepare(forCollectionViewUpdates:)`](nscollectionviewlayout/prepare(forcollectionviewupdates:).md) method, which can use them to prepare for the upcoming changes.

## Topics

### Accessing the Item Changes
- [var indexPathBeforeUpdate: IndexPath?](nscollectionviewupdateitem/indexpathbeforeupdate.md)
  The index path of the item before the update.
- [var indexPathAfterUpdate: IndexPath?](nscollectionviewupdateitem/indexpathafterupdate.md)
  The index path of the item after the update.
- [var updateAction: NSCollectionView.UpdateAction](nscollectionviewupdateitem/updateaction.md)
  The action being performed on the item.
- [NSCollectionView.UpdateAction](nscollectionview/updateaction.md)
  Constants indicating the type of action being performed on an item.
- [NSCollectionView.ScrollDirection](nscollectionview/scrolldirection.md)
  Constants indicating the scrolling direction for the layout.
### Constants
- [NSCollectionView.UpdateAction](nscollectionview/updateaction.md)
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

- [class NSCollectionViewLayoutInvalidationContext](nscollectionviewlayoutinvalidationcontext.md)
  An object that identifies the portions of your layout that need to be updated.
- [class NSCollectionViewFlowLayoutInvalidationContext](nscollectionviewflowlayoutinvalidationcontext.md)
  An object that identifies the portions of a flow layout object that need to be updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewupdateitem)*