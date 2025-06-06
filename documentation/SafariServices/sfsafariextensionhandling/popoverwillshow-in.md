# popoverWillShow(in:)

**Framework**: Safari Services  
**Kind**: method

Tells the handler that the app extension’s popover is about to be opened.

**Availability**:
- macOS 10.12+

## Declaration

```swift
optional func popoverWillShow(in window: SFSafariWindow)
```

## Mentions

- [Adjusting settings for a toolbar item](adjusting-settings-for-a-toolbar-item.md)

#### Discussion

This method is called when a popover associated with the app extension is triggered.

## Parameters

- `window`: The window to display the popover in.

## See Also

- [func popoverViewController() -> SFSafariExtensionViewController](sfsafariextensionhandling/popoverviewcontroller.md)
  Asks the handler to provide a popover view controller for display.
- [func popoverDidClose(in: SFSafariWindow)](sfsafariextensionhandling/popoverdidclose(in:).md)
  Tells the handler that the app extension’s popover was closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/popoverwillshow(in:))*