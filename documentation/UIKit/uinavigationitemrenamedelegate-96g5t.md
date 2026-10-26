# UINavigationItemRenameDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

Methods an object implements to rename a navigation item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```objc
@protocol UINavigationItemRenameDelegate <NSObject>
```

#### Overview

A navigation item ([`UINavigationItem`](./uinavigationitem.md)) uses this delegate to determine whether a person can change the navigation item’s title and to handle the rename process.

> **Related Sessions from WWDC22**:  Session 10069: [Meet desktop-class iPad](https://developer.apple.com/wwdc22/10069)
>
> Session 10070: [Build a desktop-class iPad app](https://developer.apple.com/wwdc22/10070)

## Topics

### Determining rename support
- [- navigationItemShouldBeginRenaming:](./uinavigationitemrenamedelegate-96g5t/navigationitemshouldbeginrenaming_.md)
  Asks the delegate whether the navigation item supports renaming.
- [- navigationItem:shouldEndRenamingWithTitle:](./uinavigationitemrenamedelegate-96g5t/navigationitem_shouldendrenamingwithtitle_.md)
  Asks the delegate whether to continue or abandon the rename process.
### Handling the rename process
- [- navigationItem:willBeginRenamingWithSuggestedTitle:selectedRange:](./uinavigationitemrenamedelegate-96g5t/navigationitem_willbeginrenamingwithsuggestedtitle_selectedrange_.md)
  Tells the delegate when the rename process starts.
- [- navigationItem:didEndRenamingWithTitle:](./uinavigationitemrenamedelegate-96g5t/navigationitem_didendrenamingwithtitle_.md)
  Tells the delegate when the rename process ends.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [UIDocument](./uidocument.md)

## See Also

### Renaming documents
- [renameDelegate](./uinavigationitem/renamedelegate-o32h.md)
  The delegate for renaming the navigation item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitemrenamedelegate-96g5t)*