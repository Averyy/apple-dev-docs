# contentViewController

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The view controller for the window’s content view.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var contentViewController: NSViewController? { get set }
```

```objc
@property (strong, nullable) NSViewController * contentViewController;
```

#### Discussion

The value of this property tracks the window’s [`contentView`](../nswindow/contentview.md) property.

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
- [func dismissController(Any?)](./dismisscontroller%28_%29.md)
  Dismisses the window controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/contentviewcontroller)*