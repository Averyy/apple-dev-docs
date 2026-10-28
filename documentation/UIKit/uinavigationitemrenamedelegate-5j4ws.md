# UINavigationItemRenameDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

Methods an object implements to rename a navigation item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency protocol UINavigationItemRenameDelegate : AnyObject
```

## Overview

A navigation item ([`UINavigationItem`](./uinavigationitem.md)) uses this delegate to determine whether a person can change the navigation item’s title and to handle the rename process.

> **Related Sessions from WWDC22**:  Session 10069: [Meet desktop-class iPad](https://developer.apple.com/wwdc22/10069)
>
> Session 10070: [Build a desktop-class iPad app](https://developer.apple.com/wwdc22/10070)

## Topics

### Determining rename support
- [func navigationItemShouldBeginRenaming(UINavigationItem) -> Bool](./uinavigationitemrenamedelegate-5j4ws/navigationitemshouldbeginrenaming%28_%29.md)
  Asks the delegate whether the navigation item supports renaming.
- [func navigationItem(UINavigationItem, shouldEndRenamingWith: String) -> Bool](./uinavigationitemrenamedelegate-5j4ws/navigationitem%28_,shouldendrenamingwith%29.md)
  Asks the delegate whether to continue or abandon the rename process.
### Handling the rename process
- [func navigationItem(UINavigationItem, willBeginRenamingWith: String, selectedRange: Range<String.Index>) -> (String, Range<String.Index>)](./uinavigationitemrenamedelegate-5j4ws/navigationitem%28_,willbeginrenamingwith,selectedrange%29.md)
  Tells the delegate when the rename process starts.
- [func navigationItem(UINavigationItem, didEndRenamingWith: String)](./uinavigationitemrenamedelegate-5j4ws/navigationitem%28_,didendrenamingwith%29.md)
  Tells the delegate when the rename process ends.

## See Also

### Renaming documents
- [var renameDelegate: (any UINavigationItemRenameDelegate)?](./uinavigationitem/renamedelegate-8jiuf.md)
  The delegate for renaming the navigation item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitemrenamedelegate-5j4ws)*