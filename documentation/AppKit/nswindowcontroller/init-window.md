# init(window:)

**Framework**: AppKit  
**Kind**: init

Returns a window controller initialized with a given window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
init(window: NSWindow?)
```

#### Return Value

A newly initialized window controller.

#### Discussion

This method is the designated initializer for `NSWindowController`.

This initializer is useful when a window has been loaded but no window controller is assigned. The default initialization turns on cascading, sets the [`shouldCloseDocument`](nswindowcontroller/shouldclosedocument.md) property to [`false`](https://developer.apple.com/documentation/swift/false), and sets the window frame autosave name to an empty string. As a side effect, the created window controller is added as an observer of the [`willCloseNotification`](nswindow/willclosenotification.md)s posted by that window object (which is handled by a private method). If you make the window controller a delegate of the window, you can implement NSWindow’s windowShouldClose: delegate method.

## Parameters

- `window`: The window object to manage; can be  .

## See Also

- [Document-Based App Programming Guide for Mac](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/DocBasedAppProgrammingGuideForOSX/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011179)
- [convenience init(windowNibName: NSNib.Name)](nswindowcontroller/init(windownibname:).md)
  Returns a window controller initialized with a nib file.
- [convenience init(windowNibName: NSNib.Name, owner: Any)](nswindowcontroller/init(windownibname:owner:).md)
  Returns a window controller initialized with a nib file and a specified owner for that nib file.
- [convenience init(windowNibPath: String, owner: Any)](nswindowcontroller/init(windownibpath:owner:).md)
  Returns a window controller initialized with a nib file at an absolute path and a specified owner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/init(window:))*