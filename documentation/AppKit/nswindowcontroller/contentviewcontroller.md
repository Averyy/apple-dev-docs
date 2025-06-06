# contentViewController

**Framework**: AppKit  
**Kind**: property

The view controller for the window’s content view.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var contentViewController: NSViewController? { get set }
```

#### Discussion

The value of this property tracks the window’s [`contentView`](nswindow/contentview.md) property.

## See Also

- [var shouldCascadeWindows: Bool](nswindowcontroller/shouldcascadewindows.md)
  A Boolean value that indicates whether the window will cascade in relation to other document windows when it is displayed.
- [var windowFrameAutosaveName: NSWindow.FrameAutosaveName](nswindowcontroller/windowframeautosavename.md)
  The name under which the frame rectangle of the window owned by the receiver is stored in the defaults database.
- [func synchronizeWindowTitleWithDocumentName()](nswindowcontroller/synchronizewindowtitlewithdocumentname.md)
  Synchronizes the displayed window title and the represented filename with the information in the associated document.
- [func windowTitle(forDocumentDisplayName: String) -> String](nswindowcontroller/windowtitle(fordocumentdisplayname:).md)
  Returns the window title to be used for a given document display name.
- [func dismissController(Any?)](nswindowcontroller/dismisscontroller(_:).md)
  Dismisses the window controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/contentviewcontroller)*