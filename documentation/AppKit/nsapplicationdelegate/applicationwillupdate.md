# applicationWillUpdate(_:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the app is about to update its windows.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func applicationWillUpdate(_ notification: Notification)
```

## Parameters

- `notification`: A notification named  . Calling the   method of this notification returns the   object itself.

## See Also

- [func updateWindows()](nsapplication/updatewindows.md)
  Sends an [`update()`](nswindow/update().md) message to each onscreen window.
- [func applicationDidUpdate(Notification)](nsapplicationdelegate/applicationdidupdate(_:).md)
  Tells the delegate that the app’s windows did update.
- [func applicationShouldHandleReopen(NSApplication, hasVisibleWindows: Bool) -> Bool](nsapplicationdelegate/applicationshouldhandlereopen(_:hasvisiblewindows:).md)
  Returns a Boolean value that indicates if the app responds to reopen AppleEvents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationwillupdate(_:))*