# shouldCascadeWindows

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window will cascade in relation to other document windows when it is displayed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var shouldCascadeWindows: Bool { get set }
```

#### Discussion

Cascading in relation to other document windows means having a slightly offset location so that the title bars of previously displayed windows are still visible. The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the window will cascade in relation to other document windows, [`false`](https://developer.apple.com/documentation/swift/false) otherwise. The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var windowFrameAutosaveName: NSWindow.FrameAutosaveName](nswindowcontroller/windowframeautosavename.md)
  The name under which the frame rectangle of the window owned by the receiver is stored in the defaults database.
- [func synchronizeWindowTitleWithDocumentName()](nswindowcontroller/synchronizewindowtitlewithdocumentname.md)
  Synchronizes the displayed window title and the represented filename with the information in the associated document.
- [func windowTitle(forDocumentDisplayName: String) -> String](nswindowcontroller/windowtitle(fordocumentdisplayname:).md)
  Returns the window title to be used for a given document display name.
- [var contentViewController: NSViewController?](nswindowcontroller/contentviewcontroller.md)
  The view controller for the window’s content view.
- [func dismissController(Any?)](nswindowcontroller/dismisscontroller(_:).md)
  Dismisses the window controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/shouldcascadewindows)*