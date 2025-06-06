# dismissController(_:)

**Framework**: AppKit  
**Kind**: method

Dismisses the window controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@IBAction
@MainActor func dismissController(_ sender: Any?)
```

#### Discussion

This method does nothing if the receiver is not currently presented.

## Parameters

- `sender`: The sender of the message.

## See Also

- [var shouldCascadeWindows: Bool](nswindowcontroller/shouldcascadewindows.md)
  A Boolean value that indicates whether the window will cascade in relation to other document windows when it is displayed.
- [var windowFrameAutosaveName: NSWindow.FrameAutosaveName](nswindowcontroller/windowframeautosavename.md)
  The name under which the frame rectangle of the window owned by the receiver is stored in the defaults database.
- [func synchronizeWindowTitleWithDocumentName()](nswindowcontroller/synchronizewindowtitlewithdocumentname.md)
  Synchronizes the displayed window title and the represented filename with the information in the associated document.
- [func windowTitle(forDocumentDisplayName: String) -> String](nswindowcontroller/windowtitle(fordocumentdisplayname:).md)
  Returns the window title to be used for a given document display name.
- [var contentViewController: NSViewController?](nswindowcontroller/contentviewcontroller.md)
  The view controller for the window’s content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/dismisscontroller(_:))*