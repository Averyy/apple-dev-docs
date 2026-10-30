# hasActiveWindowSharingSession

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Indicates whether the receiver is the subject of an active SharePlay sharing session.

**Availability**:
- macOS 13.3+

## Declaration

```swift
var hasActiveWindowSharingSession: Bool { get }
```

```objc
@property (readonly) BOOL hasActiveWindowSharingSession;
```

## See Also

### Managing Window Sharing
- [func transferWindowSharing(to: NSWindow, completionHandler: ((any Error)?) -> Void)](./transferwindowsharing%28to,completionhandler%29.md)
  Attempts to move window sharing (within a SharePlay session) from this window to another window.
- [func requestSharingOfWindow(NSWindow, completionHandler: ((any Error)?) -> Void)](./requestsharingofwindow%28_,completionhandler%29.md)
- [func requestSharingOfWindow(usingPreview: NSImage, title: String, completionHandler: ((any Error)?) -> Void)](./requestsharingofwindow%28usingpreview,title,completionhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/hasactivewindowsharingsession)*