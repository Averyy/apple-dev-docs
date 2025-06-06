# validateToolbarItem(in:validationHandler:)

**Framework**: Safari Services  
**Kind**: method

Determines if a toolbar menu item should be enabled or have badge text when browser state changes.

**Availability**:
- macOS 10.12+

## Declaration

```swift
optional func validateToolbarItem(in window: SFSafariWindow, validationHandler: @escaping (Bool, String) -> Void)
```

## Mentions

- [Adjusting settings for a toolbar item](adjusting-settings-for-a-toolbar-item.md)

#### Discussion

This method is called by the [`setToolbarItemsNeedUpdate()`](sfsafariapplication/settoolbaritemsneedupdate().md) method or when Safari’s state changes in a way that may affect the toolbar item’s enabled or badge state. Your handler should decide whether the toolbar menu should be enabled and whether it should have any badge text, and then call the `validationHandler` block to update the toolbar item state.

## Parameters

- `window`: The window containing the clicked toolbar item.
- `validationHandler`: A code block used to set the state of the toolbar item.

## See Also

- [func toolbarItemClicked(in: SFSafariWindow)](sfsafariextensionhandling/toolbaritemclicked(in:).md)
  A method the system calls when a user clicks a toolbar item associated with the app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/validatetoolbaritem(in:validationhandler:))*