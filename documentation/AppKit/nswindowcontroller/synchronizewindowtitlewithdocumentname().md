# synchronizeWindowTitleWithDocumentName()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Synchronizes the displayed window title and the represented filename with the information in the associated document.

**Availability**:
- macOS

## Declaration

```swift
func synchronizeWindowTitleWithDocumentName()
```

```objc
- (void) synchronizeWindowTitleWithDocumentName;
```

## Discussion

Does nothing if the window controller has no associated document or loaded window. This method queries the window controller’s document to get the document’s display name and full filename path, then calls [`windowTitle(forDocumentDisplayName:)`](./windowtitle%28fordocumentdisplayname%29.md) to get the display name to show in the window title.

## See Also

### Accessing Window Attributes and Content
- [var shouldCascadeWindows: Bool](./shouldcascadewindows.md)
  A Boolean value that indicates whether the window will cascade in relation to other document windows when it is displayed.
- [var windowFrameAutosaveName: NSWindow.FrameAutosaveName](./windowframeautosavename.md)
  The name under which the frame rectangle of the window owned by the receiver is stored in the defaults database.
- [func windowTitle(forDocumentDisplayName: String) -> String](./windowtitle%28fordocumentdisplayname%29.md)
  Returns the window title to be used for a given document display name.
- [var contentViewController: NSViewController?](./contentviewcontroller.md)
  The view controller for the window’s content view.
- [func dismissController(Any?)](./dismisscontroller%28_%29.md)
  Dismisses the window controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/synchronizewindowtitlewithdocumentname())*