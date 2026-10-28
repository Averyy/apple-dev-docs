# popoverViewController()

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

Asks the handler to provide a popover view controller for display.

**Availability**:
- macOS 10.12+

## Declaration

```swift
optional func popoverViewController() -> SFSafariExtensionViewController
```

```objc
- (SFSafariExtensionViewController *) popoverViewController;
```

## Mentions

- [Adjusting settings for a toolbar item](../adjusting-settings-for-a-toolbar-item.md)

## Return Value

The app extension’s popover view controller.

## See Also

### Working with Popovers
- [func popoverWillShow(in: SFSafariWindow)](./popoverwillshow%28in%29.md)
  Tells the handler that the app extension’s popover is about to be opened.
- [func popoverDidClose(in: SFSafariWindow)](./popoverdidclose%28in%29.md)
  Tells the handler that the app extension’s popover was closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/popoverviewcontroller())*