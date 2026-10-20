# windowWillBeginSheet(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate that the window is about to open a sheet.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowWillBeginSheet(_ notification: Notification)
```

```objc
- (void) windowWillBeginSheet:(NSNotification *) notification;
```

#### Discussion

You can retrieve the window object in question by sending [`object`](../../Foundation/nsnotification/object.md) to `notification`.

## Parameters

- `notification`: A notification named [`willBeginSheetNotification`](../nswindow/willbeginsheetnotification.md).

## See Also

### Managing Sheets
- [func window(NSWindow, willPositionSheet: NSWindow, using: NSRect) -> NSRect](./window%28_,willpositionsheet,using%29.md)
  Tells the delegate that the window is about to show a sheet at the specified location, giving it the opportunity to return a custom location for the attachment of the sheet to the window.
- [func windowDidEndSheet(Notification)](./windowdidendsheet%28_%29.md)
  Tells the delegate that the window has closed a sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowwillbeginsheet(_:))*