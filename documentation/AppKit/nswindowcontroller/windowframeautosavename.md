# windowFrameAutosaveName

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The name under which the frame rectangle of the window owned by the receiver is stored in the defaults database.

**Availability**:
- macOS

## Declaration

```swift
var windowFrameAutosaveName: NSWindow.FrameAutosaveName { get set }
```

```objc
@property (copy) NSWindowFrameAutosaveName windowFrameAutosaveName;
```

#### Discussion

By default, `name` is an empty string, which means that no information is stored in the defaults database.

## See Also

### Related Documentation
- [func setFrameAutosaveName(NSWindow.FrameAutosaveName) -> Bool](../nswindow/setframeautosavename%28_%29.md)
  Sets the name AppKit uses to automatically save the window’s frame rectangle data in the defaults system.
### Accessing Window Attributes and Content
- [var shouldCascadeWindows: Bool](./shouldcascadewindows.md)
  A Boolean value that indicates whether the window will cascade in relation to other document windows when it is displayed.
- [func synchronizeWindowTitleWithDocumentName()](./synchronizewindowtitlewithdocumentname%28%29.md)
  Synchronizes the displayed window title and the represented filename with the information in the associated document.
- [func windowTitle(forDocumentDisplayName: String) -> String](./windowtitle%28fordocumentdisplayname%29.md)
  Returns the window title to be used for a given document display name.
- [var contentViewController: NSViewController?](./contentviewcontroller.md)
  The view controller for the window’s content view.
- [func dismissController(Any?)](./dismisscontroller%28_%29.md)
  Dismisses the window controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/windowframeautosavename)*