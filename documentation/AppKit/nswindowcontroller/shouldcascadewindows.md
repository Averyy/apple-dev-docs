# shouldCascadeWindows

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window will cascade in relation to other document windows when it is displayed.

**Availability**:
- macOS

## Declaration

```swift
var shouldCascadeWindows: Bool { get set }
```

```objc
@property BOOL shouldCascadeWindows;
```

#### Discussion

Cascading in relation to other document windows means having a slightly offset location so that the title bars of previously displayed windows are still visible. The value of this property is [`true`](../../Swift/true.md) if the window will cascade in relation to other document windows, [`false`](../../Swift/false.md) otherwise. The default value is [`true`](../../Swift/true.md).

## See Also

### Accessing Window Attributes and Content
- [var windowFrameAutosaveName: NSWindow.FrameAutosaveName](./windowframeautosavename.md)
  The name under which the frame rectangle of the window owned by the receiver is stored in the defaults database.
- [func synchronizeWindowTitleWithDocumentName()](./synchronizewindowtitlewithdocumentname%28%29.md)
  Synchronizes the displayed window title and the represented filename with the information in the associated document.
- [func windowTitle(forDocumentDisplayName: String) -> String](./windowtitle%28fordocumentdisplayname%29.md)
  Returns the window title to be used for a given document display name.
- [var contentViewController: NSViewController?](./contentviewcontroller.md)
  The view controller for the window’s content view.
- [func dismissController(Any?)](./dismisscontroller%28_%29.md)
  Dismisses the window controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/shouldcascadewindows)*