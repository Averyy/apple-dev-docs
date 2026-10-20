# transferWindowSharing(to:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Attempts to move window sharing (within a SharePlay session) from this window to another window.

**Availability**:
- macOS 13.3+

## Declaration

```swift
func transferWindowSharing(to window: NSWindow) async throws
```

#### Discussion

In response to this request, the user may choose to transfer sharing to the new window, or simply stop sharing the content.

## Parameters

- `window`: Another window to replace this window in representing the user’s current activity.
- `completionHandler`: A completion block that is called after the request finishes.

## See Also

- [var hasActiveWindowSharingSession: Bool](nswindow/hasactivewindowsharingsession.md)
  Indicates whether the receiver is the subject of an active SharePlay sharing session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/transferwindowsharing(to:completionhandler:))*