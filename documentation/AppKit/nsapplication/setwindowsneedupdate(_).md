# setWindowsNeedUpdate(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets whether the receiver’s windows need updating when the receiver has finished processing the current event.

**Availability**:
- macOS

## Declaration

```swift
func setWindowsNeedUpdate(_ needUpdate: Bool)
```

```objc
- (void) setWindowsNeedUpdate:(BOOL) needUpdate;
```

## Discussion

This method is especially useful for making sure menus are updated to reflect changes not initiated by user actions, such as messages received from remote objects.

## Parameters

- `needUpdate`: If [`true`](../../Swift/true.md), the receiver’s windows are updated after an event is processed.

## See Also

### Updating Windows
- [func updateWindows()](./updatewindows%28%29.md)
  Sends an [`update()`](../nswindow/update%28%29.md) message to each onscreen window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/setwindowsneedupdate(_:))*