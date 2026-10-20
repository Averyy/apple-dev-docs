# popoverDidClose(in:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

Tells the handler that the app extension’s popover was closed.

**Availability**:
- macOS 10.12+

## Declaration

```swift
optional func popoverDidClose(in window: SFSafariWindow)
```

```objc
- (void) popoverDidCloseInWindow:(SFSafariWindow *) window;
```

## Mentions

- [Adjusting settings for a toolbar item](../adjusting-settings-for-a-toolbar-item.md)

## Parameters

- `window`: The window that displayed the popover.

## See Also

### Working with Popovers
- [func popoverViewController() -> SFSafariExtensionViewController](./popoverviewcontroller%28%29.md)
  Asks the handler to provide a popover view controller for display.
- [func popoverWillShow(in: SFSafariWindow)](./popoverwillshow%28in%29.md)
  Tells the handler that the app extension’s popover is about to be opened.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/popoverdidclose(in:))*