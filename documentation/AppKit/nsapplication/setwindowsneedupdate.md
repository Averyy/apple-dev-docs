# setWindowsNeedUpdate(_:)

**Framework**: AppKit  
**Kind**: method

Sets whether the receiver’s windows need updating when the receiver has finished processing the current event.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setWindowsNeedUpdate(_ needUpdate: Bool)
```

#### Discussion

This method is especially useful for making sure menus are updated to reflect changes not initiated by user actions, such as messages received from remote objects.

## Parameters

- `needUpdate`: If  , the receiver’s windows are updated after an event is processed.

## See Also

- [func updateWindows()](nsapplication/updatewindows.md)
  Sends an [`update()`](nswindow/update().md) message to each onscreen window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/setwindowsneedupdate(_:))*