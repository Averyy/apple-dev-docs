# setFrameUsingName(_:force:)

**Framework**: AppKit  
**Kind**: method

Sets the window’s frame rectangle by reading the rectangle data stored under a given name from the defaults system. Can operate on non-resizable windows.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setFrameUsingName(_ name: NSWindow.FrameAutosaveName, force: Bool) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) when `name` is read and the frame is set successfully; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `name`: The name of the frame to read.
- `force`:   to use   on a non-resizable window;   to fail on a non-resizable window.

## See Also

- [class func removeFrame(usingName: NSWindow.FrameAutosaveName)](nswindow/removeframe(usingname:).md)
  Removes the frame data stored under a given name from the application’s user defaults.
- [func setFrameUsingName(NSWindow.FrameAutosaveName) -> Bool](nswindow/setframeusingname(_:).md)
  Sets the window’s frame rectangle by reading the rectangle data stored under a given name from the defaults system.
- [func saveFrame(usingName: NSWindow.FrameAutosaveName)](nswindow/saveframe(usingname:).md)
  Saves the window’s frame rectangle in the user defaults system under a given name.
- [func setFrameAutosaveName(NSWindow.FrameAutosaveName) -> Bool](nswindow/setframeautosavename(_:).md)
  Sets the name AppKit uses to automatically save the window’s frame rectangle data in the defaults system.
- [var frameAutosaveName: NSWindow.FrameAutosaveName](nswindow/frameautosavename-swift.property.md)
  The name used to automatically save the window’s frame rectangle data in the defaults system.
- [typealias FrameAutosaveName](nswindow/frameautosavename-swift.typealias.md)
  The type of a window’s frame autosave name.
- [var frameDescriptor: NSWindow.PersistableFrameDescriptor](nswindow/framedescriptor.md)
  A string representation of the window’s frame rectangle.
- [func setFrame(from: NSWindow.PersistableFrameDescriptor)](nswindow/setframe(from:).md)
  Sets the window’s frame rectangle from a given string representation.
- [typealias PersistableFrameDescriptor](nswindow/persistableframedescriptor.md)
  The type of a window’s frame descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/setframeusingname(_:force:))*