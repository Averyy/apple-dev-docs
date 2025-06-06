# toolbarItemClicked(in:)

**Framework**: Safari Services  
**Kind**: method

A method the system calls when a user clicks a toolbar item associated with the app extension.

**Availability**:
- macOS 10.12+

## Declaration

```swift
optional func toolbarItemClicked(in window: SFSafariWindow)
```

## Mentions

- [Adjusting settings for a toolbar item](adjusting-settings-for-a-toolbar-item.md)

#### Discussion

The toolbar item can either execute a command or display a popover.

## Parameters

- `window`: The window containing the clicked toolbar item.

## See Also

- [func validateToolbarItem(in: SFSafariWindow, validationHandler: (Bool, String) -> Void)](sfsafariextensionhandling/validatetoolbaritem(in:validationhandler:).md)
  Determines if a toolbar menu item should be enabled or have badge text when browser state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/toolbaritemclicked(in:))*