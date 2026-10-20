# init(contentRect:styleMask:backing:defer:screen:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes an allocated window with the specified values.

**Availability**:
- macOS

## Declaration

```swift
convenience init(contentRect: NSRect, styleMask style: NSWindow.StyleMask, backing backingStoreType: NSWindow.BackingStoreType, defer flag: Bool, screen: NSScreen?)
```

```objc
- (instancetype) initWithContentRect:(NSRect) contentRect styleMask:(NSWindowStyleMask) style backing:(NSBackingStoreType) backingStoreType defer:(BOOL) flag screen:(NSScreen *) screen;
```

#### Return Value

The initialized window.

#### Discussion

The primary screen is the one that contains the current key window or, if there is no key window, the one that contains the main menu. If there’s neither a key window nor a main menu (if there’s no active application), the primary screen is the one where the origin of the screen coordinate system is located.

> ⚠️ **Warning**: Swift and Automatic Reference Counting (ARC) clients need to set the [`isReleasedWhenClosed`](./isreleasedwhenclosed.md) property to [`false`](../../Swift/false.md) to avoid releasing the window too many times.

## Parameters

- `contentRect`: Origin and size of the window’s content area in screen coordinates. The origin is relative to the origin of the provided screen. Note that the window server limits window position coordinates to ±16,000 and sizes to 10,000.
- `style`: The window’s style. It can be `NSBorderlessWindowMask`, or it can contain any of the options described in [`NSWindow.StyleMask`](./stylemask-swift.struct.md), combined using the C bitwise OR operator. Borderless windows display none of the usual peripheral elements and are generally useful only for display or caching purposes; you should not usually need to create them. Also, note that a window’s style mask should include `NSTitledWindowMask` if it includes any of the others.
- `backingStoreType`: Specifies how the drawing done in the window is buffered by the window device; possible values are described in [`NSWindow.BackingStoreType`](./backingstoretype.md).
- `flag`: Specifies whether the window server creates a window device for the window immediately. When [`true`](../../Swift/true.md), the window server defers creating the window device until the window is moved onscreen. All display messages sent to the window or its views are postponed until the window is created, just before it’s moved onscreen.
- `screen`: Specifies the screen on which the window is positioned. The content rectangle is positioned relative to the bottom-left corner of `screen`. When `nil`, the content rectangle is positioned relative to (0, 0), which is the origin of the primary screen.

## See Also

### Related Documentation
- [var title: String](./title.md)
  The string that appears in the title bar of the window or the path to the represented file.
- [func orderFront(Any?)](./orderfront%28_%29.md)
  Moves the window to the front of its level in the screen list, without changing either the key window or the main window.
- [var isOneShot: Bool](./isoneshot.md)
  A Boolean value that indicates whether the window device the window manages is freed when it’s removed from the screen list.
### Creating a Window
- [convenience init(contentViewController: NSViewController)](./init%28contentviewcontroller%29.md)
  Creates a titled window that contains the specified content view controller.
- [init(contentRect: NSRect, styleMask: NSWindow.StyleMask, backing: NSWindow.BackingStoreType, defer: Bool)](./init%28contentrect,stylemask,backing,defer%29.md)
  Initializes the window with the specified values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/init(contentrect:stylemask:backing:defer:screen:))*