# windowFrameAutosaveName

**Framework**: AppKit  
**Kind**: property

The name under which the frame rectangle of the window owned by the receiver is stored in the defaults database.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var windowFrameAutosaveName: NSWindow.FrameAutosaveName { get set }
```

#### Discussion

By default, `name` is an empty string, which means that no information is stored in the defaults database.

## See Also

- [func setFrameAutosaveName(NSWindow.FrameAutosaveName) -> Bool](nswindow/setframeautosavename(_:).md)
  Sets the name AppKit uses to automatically save the window’s frame rectangle data in the defaults system.
- [var shouldCascadeWindows: Bool](nswindowcontroller/shouldcascadewindows.md)
  A Boolean value that indicates whether the window will cascade in relation to other document windows when it is displayed.
- [func synchronizeWindowTitleWithDocumentName()](nswindowcontroller/synchronizewindowtitlewithdocumentname.md)
  Synchronizes the displayed window title and the represented filename with the information in the associated document.
- [func windowTitle(forDocumentDisplayName: String) -> String](nswindowcontroller/windowtitle(fordocumentdisplayname:).md)
  Returns the window title to be used for a given document display name.
- [var contentViewController: NSViewController?](nswindowcontroller/contentviewcontroller.md)
  The view controller for the window’s content view.
- [func dismissController(Any?)](nswindowcontroller/dismisscontroller(_:).md)
  Dismisses the window controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/windowframeautosavename)*