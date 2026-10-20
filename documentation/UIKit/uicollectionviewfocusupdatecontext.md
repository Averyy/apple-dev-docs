# UICollectionViewFocusUpdateContext

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A context object that stores information specific to a focus update in a collection view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICollectionViewFocusUpdateContext
```

```objc
@interface UICollectionViewFocusUpdateContext : UIFocusUpdateContext
```

#### Overview

When focus changes, the collection view delegate receives a context object with the relevant information. Your delegate methods use the information in this object to create animations or to perform other tasks related to the change in focus.

## Topics

### Locating focusable items in the collection view
- [var previouslyFocusedIndexPath: IndexPath?](./uicollectionviewfocusupdatecontext/previouslyfocusedindexpath.md)
  The index path of the collection view cell that previously had the focus.
- [var nextFocusedIndexPath: IndexPath?](./uicollectionviewfocusupdatecontext/nextfocusedindexpath.md)
  The index path of the collection view cell that’s receiving the focus.

## Relationships

### Inherits From
- [UIFocusUpdateContext](./uifocusupdatecontext.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Layout updates
- [protocol NSCollectionLayoutVisibleItem](./nscollectionlayoutvisibleitem.md)
  An item that’s currently visible within the bounds of a section.
- [typealias NSCollectionLayoutSectionVisibleItemsInvalidationHandler](./nscollectionlayoutsectionvisibleitemsinvalidationhandler.md)
  A closure called before each layout cycle to allow modification of items in a section immediately before they’re displayed.
- [class UICollectionViewUpdateItem](./uicollectionviewupdateitem.md)
  An object that describes a single change to make to an item in a collection view.
- [class UICollectionViewLayoutInvalidationContext](./uicollectionviewlayoutinvalidationcontext.md)
  A context object that declares which parts of your layout need to be updated when the layout is invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewfocusupdatecontext)*