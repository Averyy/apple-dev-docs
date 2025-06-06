# windowTitle(forDocumentDisplayName:)

**Framework**: AppKit  
**Kind**: method

Returns the window title to be used for a given document display name.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func windowTitle(forDocumentDisplayName displayName: String) -> String
```

#### Discussion

The default implementation returns `displayName`. Subclasses can override this method to customize the window title. For example, a CAD application could append “-Top” or “-Side,” depending on the view displayed by the window.

## Parameters

- `displayName`: The display name for the document. This is the last path component under which the document file is saved.

## See Also

- [var shouldCascadeWindows: Bool](nswindowcontroller/shouldcascadewindows.md)
  A Boolean value that indicates whether the window will cascade in relation to other document windows when it is displayed.
- [var windowFrameAutosaveName: NSWindow.FrameAutosaveName](nswindowcontroller/windowframeautosavename.md)
  The name under which the frame rectangle of the window owned by the receiver is stored in the defaults database.
- [func synchronizeWindowTitleWithDocumentName()](nswindowcontroller/synchronizewindowtitlewithdocumentname.md)
  Synchronizes the displayed window title and the represented filename with the information in the associated document.
- [var contentViewController: NSViewController?](nswindowcontroller/contentviewcontroller.md)
  The view controller for the window’s content view.
- [func dismissController(Any?)](nswindowcontroller/dismisscontroller(_:).md)
  Dismisses the window controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/windowtitle(fordocumentdisplayname:))*