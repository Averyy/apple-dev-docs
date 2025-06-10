# windowWillBeginSheet(_:)

**Framework**: AppKit  
**Kind**: method

Notifies the delegate that the window is about to open a sheet.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowWillBeginSheet(_ notification: Notification)
```

#### Discussion

You can retrieve the window object in question by sending [`object`](https://developer.apple.com/documentation/Foundation/NSNotification/object) to `notification`.

## Parameters

- `notification`: A notification named  .

## See Also

- [func window(NSWindow, willPositionSheet: NSWindow, using: NSRect) -> NSRect](nswindowdelegate/window(_:willpositionsheet:using:).md)
  Tells the delegate that the window is about to show a sheet at the specified location, giving it the opportunity to return a custom location for the attachment of the sheet to the window.
- [func windowDidEndSheet(Notification)](nswindowdelegate/windowdidendsheet(_:).md)
  Tells the delegate that the window has closed a sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowwillbeginsheet(_:))*