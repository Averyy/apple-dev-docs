# init(contentViewController:)

**Framework**: AppKit  
**Kind**: init

Creates a titled window that contains the specified content view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
convenience init(contentViewController: NSViewController)
```

#### Return Value

A window with the content view controller set to the passed-in view controller object.

#### Discussion

This method creates a basic window object that is titled, closable, resizable, and miniaturizable. By default, the window’s title is automatically bound to the title of `contentViewController`. You can control the size of the window by using Auto Layout and applying size constraints to the view or its subviews. The initial size of the window is set to the initial size of [`contentView`](nswindow/contentview.md) (that is, the size of `contentViewController``.view`). The newly created window has [`isReleasedWhenClosed`](nswindow/isreleasedwhenclosed.md) set to [`false`](https://developer.apple.com/documentation/swift/false), and it must be explicitly retained to keep the window instance alive.

## Parameters

- `contentViewController`: The view controller that provides the main content view for the window. The window’s   property is set to  .

## See Also

- [Window Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Introduction.html#//apple_ref/doc/uid/10000031i)
- [var contentViewController: NSViewController?](nswindow/contentviewcontroller.md)
  The main content view controller for the window.
- [init(contentRect: NSRect, styleMask: NSWindow.StyleMask, backing: NSWindow.BackingStoreType, defer: Bool)](nswindow/init(contentrect:stylemask:backing:defer:).md)
  Initializes the window with the specified values.
- [convenience init(contentRect: NSRect, styleMask: NSWindow.StyleMask, backing: NSWindow.BackingStoreType, defer: Bool, screen: NSScreen?)](nswindow/init(contentrect:stylemask:backing:defer:screen:).md)
  Initializes an allocated window with the specified values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/init(contentviewcontroller:))*