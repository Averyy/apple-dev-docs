# init(window:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns a window controller initialized with a given window.

**Availability**:
- macOS

## Declaration

```swift
init(window: NSWindow?)
```

```objc
- (instancetype) initWithWindow:(NSWindow *) window;
```

## Return Value

A newly initialized window controller.

## Discussion

This method is the designated initializer for `NSWindowController`.

This initializer is useful when a window has been loaded but no window controller is assigned. The default initialization turns on cascading, sets the [`shouldCloseDocument`](./shouldclosedocument.md) property to [`false`](../../Swift/false.md), and sets the window frame autosave name to an empty string. As a side effect, the created window controller is added as an observer of the [`willCloseNotification`](../nswindow/willclosenotification.md) posted by that window object (which is handled by a private method). If you make the window controller a delegate of the window, you can implement the [`NSWindow`](../nswindow.md) delegate method `windowShouldClose(_:)`.

## Parameters

- `window`: The window object to manage; can be `nil`.

## See Also

### Initializing Window Controllers
- [convenience init(windowNibName: NSNib.Name)](./init%28windownibname%29.md)
  Returns a window controller initialized with a nib file.
- [convenience init(windowNibName: NSNib.Name, owner: Any)](./init%28windownibname,owner%29.md)
  Returns a window controller initialized with a nib file and a specified owner for that nib file.
- [convenience init(windowNibPath: String, owner: Any)](./init%28windownibpath,owner%29.md)
  Returns a window controller initialized with a nib file at an absolute path and a specified owner.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/init(window:))*