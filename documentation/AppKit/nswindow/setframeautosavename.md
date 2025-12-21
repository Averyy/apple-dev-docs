# setFrameAutosaveName(_:)

**Framework**: AppKit  
**Kind**: method

Sets the name AppKit uses to automatically save the window’s frame rectangle data in the defaults system.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setFrameAutosaveName(_ name: NSWindow.FrameAutosaveName) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the specified name is acceptable and another window isn’t already using it; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `name`: The name to use for the window’s frame rectangle.

## See Also

- [class func removeFrame(usingName: NSWindow.FrameAutosaveName)](nswindow/removeframe(usingname:).md)
  Removes the frame data stored under a given name from the application’s user defaults.
- [func setFrameUsingName(NSWindow.FrameAutosaveName) -> Bool](nswindow/setframeusingname(_:).md)
  Sets the window’s frame rectangle by reading the rectangle data stored under a given name from the defaults system.
- [func setFrameUsingName(NSWindow.FrameAutosaveName, force: Bool) -> Bool](nswindow/setframeusingname(_:force:).md)
  Sets the window’s frame rectangle by reading the rectangle data stored under a given name from the defaults system. Can operate on non-resizable windows.
- [func saveFrame(usingName: NSWindow.FrameAutosaveName)](nswindow/saveframe(usingname:).md)
  Saves the window’s frame rectangle in the user defaults system under a given name.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/setframeautosavename(_:))*