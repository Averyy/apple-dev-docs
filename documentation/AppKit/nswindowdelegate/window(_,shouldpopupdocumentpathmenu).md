# window(_:shouldPopUpDocumentPathMenu:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the window displays the title pop-up menu in response to a Command-click or Control-click on its title.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
optional func window(_ window: NSWindow, shouldPopUpDocumentPathMenu menu: NSMenu) -> Bool
```

```objc
- (BOOL) window:(NSWindow *) window shouldPopUpDocumentPathMenu:(NSMenu *) menu;
```

## Return Value

[`true`](../../Swift/true.md) to allow the display of the title pop-up menu; [`false`](../../Swift/false.md) to prevent it.

## Parameters

- `window`: The window whose title the user Command-clicked or Control-clicked.
- `menu`: The menu the window will display, if allowed. By default, its items are the path components of the file represented by `window`.

## See Also

### Related Documentation
- [var representedURL: URL?](../nswindow/representedurl.md)
  The URL of the file the window represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/window(_:shouldpopupdocumentpathmenu:))*