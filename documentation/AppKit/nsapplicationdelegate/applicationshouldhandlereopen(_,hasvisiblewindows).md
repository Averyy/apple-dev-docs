# applicationShouldHandleReopen(_:hasVisibleWindows:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates if the app responds to reopen AppleEvents.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func applicationShouldHandleReopen(_ sender: NSApplication, hasVisibleWindows: Bool) -> Bool
```

```objc
- (BOOL) applicationShouldHandleReopen:(NSApplication *) sender hasVisibleWindows:(BOOL) hasVisibleWindows;
```

#### Return Value

[`true`](../../Swift/true.md) if you want the application to perform its normal tasks or [`false`](../../Swift/false.md) if you want the application to do nothing.

#### Discussion

These events are sent whenever the Finder reactivates an already running application because someone double-clicked it again or used the dock to activate it.

By default the Application Kit will handle this event by checking whether there are any visible `NSWindow` (not `NSPanel`) objects, and, if there are none, it goes through the standard untitled document creation (the same as it does if `theApplication` is launched without any document to open). For most document-based applications, an untitled document will be created.

The application delegate will also get a chance to respond to the normal untitled document delegate methods. If you implement this method in your application delegate, it will be called before any of the default behavior happens. If you return [`true`](../../Swift/true.md), then `NSApplication` will proceed as normal. If you return [`false`](../../Swift/false.md), then `NSApplication` will do nothing. So, you can either implement this method with a version that does nothing, and return [`false`](../../Swift/false.md) if you do not want anything to happen at all (not recommended), or you can implement this method, handle the event yourself in some custom way, and return [`false`](../../Swift/false.md).

Miniaturized windows, windows in the Dock, are considered visible by this method, and cause `flag` to return [`true`](../../Swift/true.md), despite the fact that miniaturized windows return [`false`](../../Swift/false.md) when sent an [`isVisible`](../nswindow/isvisible.md) message.

## Parameters

- `sender`: The application object.
- `hasVisibleWindows`: Indicates whether the `NSApplication` object found any visible windows in your application. You can use this value as an indication of whether the application would do anything if you return [`true`](../../Swift/true.md).

## See Also

### Managing Windows
- [func applicationWillUpdate(Notification)](./applicationwillupdate%28_%29.md)
  Tells the delegate that the app is about to update its windows.
- [func applicationDidUpdate(Notification)](./applicationdidupdate%28_%29.md)
  Tells the delegate that the app’s windows did update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/applicationshouldhandlereopen(_:hasvisiblewindows:))*