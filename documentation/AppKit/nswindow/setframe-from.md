# setFrame(from:)

**Framework**: AppKit  
**Kind**: method

Sets the window’s frame rectangle from a given string representation.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setFrame(from string: NSWindow.PersistableFrameDescriptor)
```

#### Discussion

If the window is not resizable, this method will not resize the window. The frame is constrained according to the window’s minimum and maximum size settings. This method causes a [`windowWillResize(_:to:)`](nswindowdelegate/windowwillresize(_:to:).md) message to be sent to the delegate.

## Parameters

- `string`: A string representation of a frame rectangle, previously accessed using  .

## See Also

- [class func removeFrame(usingName: NSWindow.FrameAutosaveName)](nswindow/removeframe(usingname:).md)
  Removes the frame data stored under a given name from the application’s user defaults.
- [func setFrameUsingName(NSWindow.FrameAutosaveName) -> Bool](nswindow/setframeusingname(_:).md)
  Sets the window’s frame rectangle by reading the rectangle data stored under a given name from the defaults system.
- [func setFrameUsingName(NSWindow.FrameAutosaveName, force: Bool) -> Bool](nswindow/setframeusingname(_:force:).md)
  Sets the window’s frame rectangle by reading the rectangle data stored under a given name from the defaults system. Can operate on non-resizable windows.
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
- [typealias PersistableFrameDescriptor](nswindow/persistableframedescriptor.md)
  The type of a window’s frame descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/setframe(from:))*