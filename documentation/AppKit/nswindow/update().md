# update()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Updates the window.

**Availability**:
- macOS

## Declaration

```swift
func update()
```

```objc
- (void) update;
```

## Discussion

The `NSWindow` implementation of this method does nothing more than post an [`didUpdateNotification`](./didupdatenotification.md) notification to the default notification center. A subclass can override this method to perform specialized operations, but it should send an update message to `super` just before returning. For example, the `NSMenu` class implements this method to disable and enable menu commands.

An `NSWindow` object is automatically sent an `update` message on every pass through the event loop and before it’s displayed onscreen. You can manually cause an `update` message to be sent to all visible `NSWindow` objects through the `NSApplication` [`updateWindows()`](../nsapplication/updatewindows%28%29.md) method.

## See Also

### Related Documentation
- [func setWindowsNeedUpdate(Bool)](../nsapplication/setwindowsneedupdate%28_%29.md)
  Sets whether the receiver’s windows need updating when the receiver has finished processing the current event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/update())*