# applicationWillUpdate(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the app is about to update its windows.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func applicationWillUpdate(_ notification: Notification)
```

```objc
- (void) applicationWillUpdate:(NSNotification *) notification;
```

## Parameters

- `notification`: A notification named [`willUpdateNotification`](../nsapplication/willupdatenotification.md). Calling the [`object`](../../Foundation/nsnotification/object.md) method of this notification returns the `NSApplication` object itself.

## See Also

### Related Documentation
- [func updateWindows()](../nsapplication/updatewindows%28%29.md)
  Sends an [`update()`](../nswindow/update%28%29.md) message to each onscreen window.
### Managing Windows
- [func applicationDidUpdate(Notification)](./applicationdidupdate%28_%29.md)
  Tells the delegate that the app’s windows did update.
- [func applicationShouldHandleReopen(NSApplication, hasVisibleWindows: Bool) -> Bool](./applicationshouldhandlereopen%28_,hasvisiblewindows%29.md)
  Returns a Boolean value that indicates if the app responds to reopen AppleEvents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationwillupdate(_:))*