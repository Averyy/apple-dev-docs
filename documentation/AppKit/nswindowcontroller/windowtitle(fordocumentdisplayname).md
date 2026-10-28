# windowTitle(forDocumentDisplayName:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the window title to be used for a given document display name.

**Availability**:
- macOS

## Declaration

```swift
func windowTitle(forDocumentDisplayName displayName: String) -> String
```

```objc
- (NSString *) windowTitleForDocumentDisplayName:(NSString *) displayName;
```

## Discussion

The default implementation returns `displayName`. Subclasses can override this method to customize the window title. For example, a CAD application could append “-Top” or “-Side,” depending on the view displayed by the window.

## Parameters

- `displayName`: The display name for the document. This is the last path component under which the document file is saved.

## See Also

### Accessing Window Attributes and Content
- [var shouldCascadeWindows: Bool](./shouldcascadewindows.md)
  A Boolean value that indicates whether the window will cascade in relation to other document windows when it is displayed.
- [var windowFrameAutosaveName: NSWindow.FrameAutosaveName](./windowframeautosavename.md)
  The name under which the frame rectangle of the window owned by the receiver is stored in the defaults database.
- [func synchronizeWindowTitleWithDocumentName()](./synchronizewindowtitlewithdocumentname%28%29.md)
  Synchronizes the displayed window title and the represented filename with the information in the associated document.
- [var contentViewController: NSViewController?](./contentviewcontroller.md)
  The view controller for the window’s content view.
- [func dismissController(Any?)](./dismisscontroller%28_%29.md)
  Dismisses the window controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/windowtitle(fordocumentdisplayname:))*