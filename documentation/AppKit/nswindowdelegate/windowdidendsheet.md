# windowDidEndSheet(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the window has closed a sheet.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func windowDidEndSheet(_ notification: Notification)
```

#### Discussion

You can retrieve the window object in question by sending [`object`](https://developer.apple.com/documentation/foundation/nsnotification/1414469-object) to `notification`.

## Parameters

- `notification`: A notification named  .

## See Also

- [func window(NSWindow, willPositionSheet: NSWindow, using: NSRect) -> NSRect](nswindowdelegate/window(_:willpositionsheet:using:).md)
  Tells the delegate that the window is about to show a sheet at the specified location, giving it the opportunity to return a custom location for the attachment of the sheet to the window.
- [func windowWillBeginSheet(Notification)](nswindowdelegate/windowwillbeginsheet(_:).md)
  Notifies the delegate that the window is about to open a sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowdelegate/windowdidendsheet(_:))*