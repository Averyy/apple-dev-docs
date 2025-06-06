# popoverViewController()

**Framework**: Safari Services  
**Kind**: method

Asks the handler to provide a popover view controller for display.

**Availability**:
- macOS 10.12+

## Declaration

```swift
optional func popoverViewController() -> SFSafariExtensionViewController
```

## Mentions

- [Adjusting settings for a toolbar item](adjusting-settings-for-a-toolbar-item.md)

#### Return Value

The app extension’s popover view controller.

## See Also

- [func popoverWillShow(in: SFSafariWindow)](sfsafariextensionhandling/popoverwillshow(in:).md)
  Tells the handler that the app extension’s popover is about to be opened.
- [func popoverDidClose(in: SFSafariWindow)](sfsafariextensionhandling/popoverdidclose(in:).md)
  Tells the handler that the app extension’s popover was closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/popoverviewcontroller())*