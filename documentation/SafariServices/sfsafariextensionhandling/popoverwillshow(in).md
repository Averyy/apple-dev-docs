# popoverWillShow(in:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

Tells the handler that the app extension’s popover is about to be opened.

**Availability**:
- macOS 10.12+

## Declaration

```swift
optional func popoverWillShow(in window: SFSafariWindow)
```

```objc
- (void) popoverWillShowInWindow:(SFSafariWindow *) window;
```

## Mentions

- [Adjusting settings for a toolbar item](../adjusting-settings-for-a-toolbar-item.md)

#### Discussion

This method is called when a popover associated with the app extension is triggered.

## Parameters

- `window`: The window to display the popover in.

## See Also

### Working with Popovers
- [func popoverViewController() -> SFSafariExtensionViewController](./popoverviewcontroller%28%29.md)
  Asks the handler to provide a popover view controller for display.
- [func popoverDidClose(in: SFSafariWindow)](./popoverdidclose%28in%29.md)
  Tells the handler that the app extension’s popover was closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/popoverwillshow(in:))*