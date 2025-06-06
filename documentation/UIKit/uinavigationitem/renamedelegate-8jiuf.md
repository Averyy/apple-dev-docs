# renameDelegate

**Framework**: UIKit  
**Kind**: property

The delegate for renaming the navigation item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency weak var renameDelegate: (any UINavigationItemRenameDelegate)? { get set }
```

#### Discussion

If you assign a non-`nil` value to this property, UIKit shows an inline text field UI for changing the navigation item’s title. This UI appears when either you or the system calls [`rename(_:)`](uiresponderstandardeditactions/rename(_:).md) on the navigation controller, which occurs when a person taps Rename in the title menu or when you call [`rename(_:)`](uiresponderstandardeditactions/rename(_:).md) explicitly.

To show Rename in the navigation item’s title menu, include the Rename menu element in the menu you return from [`titleMenuProvider`](uinavigationitem/titlemenuprovider.md). UIKit includes Rename in the set of menu element suggestions it passes in to this closure.

If you only want to show Rename in the title menu, assign a [`renameDelegate`](uinavigationitem/renamedelegate-8jiuf.md) without setting a [`titleMenuProvider`](uinavigationitem/titlemenuprovider.md). In this case, UIKit automatically generates a title menu containing the Rename menu element only.

If you set this property to `nil` while a rename operation is in progress, the operation cancels immediately.

## See Also

- [protocol UINavigationItemRenameDelegate](uinavigationitemrenamedelegate-5j4ws.md)
  Methods an object implements to rename a navigation item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/renamedelegate-8jiuf)*