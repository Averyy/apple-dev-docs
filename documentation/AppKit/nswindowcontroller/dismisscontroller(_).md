# dismissController(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Dismisses the window controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@IBAction
func dismissController(_ sender: Any?)
```

```objc
- (void) dismissController:(id) sender;
```

#### Discussion

This method does nothing if the receiver is not currently presented.

## Parameters

- `sender`: The sender of the message.

## See Also

### Accessing Window Attributes and Content
- [var shouldCascadeWindows: Bool](./shouldcascadewindows.md)
  A Boolean value that indicates whether the window will cascade in relation to other document windows when it is displayed.
- [var windowFrameAutosaveName: NSWindow.FrameAutosaveName](./windowframeautosavename.md)
  The name under which the frame rectangle of the window owned by the receiver is stored in the defaults database.
- [func synchronizeWindowTitleWithDocumentName()](./synchronizewindowtitlewithdocumentname%28%29.md)
  Synchronizes the displayed window title and the represented filename with the information in the associated document.
- [func windowTitle(forDocumentDisplayName: String) -> String](./windowtitle%28fordocumentdisplayname%29.md)
  Returns the window title to be used for a given document display name.
- [var contentViewController: NSViewController?](./contentviewcontroller.md)
  The view controller for the window’s content view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/dismisscontroller(_:))*