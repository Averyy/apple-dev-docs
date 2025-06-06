# saveFrame(usingName:)

**Framework**: AppKit  
**Kind**: method

Saves the window’s frame rectangle in the user defaults system under a given name.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func saveFrame(usingName name: NSWindow.FrameAutosaveName)
```

#### Discussion

With the companion method [`setFrameUsingName(_:)`](nswindow/setframeusingname(_:).md), you can save and reset an `NSWindow` object’s frame over various launches of an application. The default is owned by the application and stored under the name “`NSWindow Frame name`”. See [`UserDefaults`](https://developer.apple.com/documentation/Foundation/UserDefaults) for more information.

## Parameters

- `name`: The name under which the frame is to be saved.

## See Also

- [class func removeFrame(usingName: NSWindow.FrameAutosaveName)](nswindow/removeframe(usingname:).md)
  Removes the frame data stored under a given name from the application’s user defaults.
- [func setFrameUsingName(NSWindow.FrameAutosaveName) -> Bool](nswindow/setframeusingname(_:).md)
  Sets the window’s frame rectangle by reading the rectangle data stored under a given name from the defaults system.
- [func setFrameUsingName(NSWindow.FrameAutosaveName, force: Bool) -> Bool](nswindow/setframeusingname(_:force:).md)
  Sets the window’s frame rectangle by reading the rectangle data stored under a given name from the defaults system. Can operate on non-resizable windows.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/saveframe(usingname:))*