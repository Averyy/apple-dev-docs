# init(contentViewController:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a titled window that contains the specified content view controller.

**Availability**:
- macOS 10.10+

## Declaration

```swift
convenience init(contentViewController: NSViewController)
```

```objc
+ (instancetype) windowWithContentViewController:(NSViewController *) contentViewController;
```

#### Return Value

A window with the content view controller set to the passed-in view controller object.

#### Discussion

This method creates a basic window object that is titled, closable, resizable, and miniaturizable. By default, the window’s title is automatically bound to the title of `contentViewController`. You can control the size of the window by using Auto Layout and applying size constraints to the view or its subviews. The initial size of the window is set to the initial size of [`contentView`](./contentview.md) (that is, the size of `contentViewController``.view`). The newly created window has [`isReleasedWhenClosed`](./isreleasedwhenclosed.md) set to [`false`](../../Swift/false.md), and it must be explicitly retained to keep the window instance alive.

## Parameters

- `contentViewController`: The view controller that provides the main content view for the window. The window’s [`contentView`](./contentview.md) property is set to `contentViewController``.view`.

## See Also

### Related Documentation
- [Window Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Introduction.html#//apple_ref/doc/uid/10000031i)
- [var contentViewController: NSViewController?](./contentviewcontroller.md)
  The main content view controller for the window.
### Creating a Window
- [init(contentRect: NSRect, styleMask: NSWindow.StyleMask, backing: NSWindow.BackingStoreType, defer: Bool)](./init%28contentrect,stylemask,backing,defer%29.md)
  Initializes the window with the specified values.
- [convenience init(contentRect: NSRect, styleMask: NSWindow.StyleMask, backing: NSWindow.BackingStoreType, defer: Bool, screen: NSScreen?)](./init%28contentrect,stylemask,backing,defer,screen%29.md)
  Initializes an allocated window with the specified values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/init(contentviewcontroller:))*