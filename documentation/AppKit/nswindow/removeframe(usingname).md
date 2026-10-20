# removeFrame(usingName:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Removes the frame data stored under a given name from the application’s user defaults.

**Availability**:
- macOS

## Declaration

```swift
class func removeFrame(usingName name: NSWindow.FrameAutosaveName)
```

```objc
+ (void) removeFrameUsingName:(NSWindowFrameAutosaveName) name;
```

## Parameters

- `name`: The name of the frame to remove.

## See Also

### Managing Window Frames in User Defaults
- [func setFrameUsingName(NSWindow.FrameAutosaveName) -> Bool](./setframeusingname%28_%29.md)
  Sets the window’s frame rectangle by reading the rectangle data stored under a given name from the defaults system.
- [func setFrameUsingName(NSWindow.FrameAutosaveName, force: Bool) -> Bool](./setframeusingname%28_,force%29.md)
  Sets the window’s frame rectangle by reading the rectangle data stored under a given name from the defaults system. Can operate on non-resizable windows.
- [func saveFrame(usingName: NSWindow.FrameAutosaveName)](./saveframe%28usingname%29.md)
  Saves the window’s frame rectangle in the user defaults system under a given name.
- [func setFrameAutosaveName(NSWindow.FrameAutosaveName) -> Bool](./setframeautosavename%28_%29.md)
  Sets the name AppKit uses to automatically save the window’s frame rectangle data in the defaults system.
- [var frameAutosaveName: NSWindow.FrameAutosaveName](./frameautosavename-swift.property.md)
  The name used to automatically save the window’s frame rectangle data in the defaults system.
- [typealias FrameAutosaveName](./frameautosavename-swift.typealias.md)
  The type of a window’s frame autosave name.
- [var frameDescriptor: NSWindow.PersistableFrameDescriptor](./framedescriptor.md)
  A string representation of the window’s frame rectangle.
- [func setFrame(from: NSWindow.PersistableFrameDescriptor)](./setframe%28from%29.md)
  Sets the window’s frame rectangle from a given string representation.
- [typealias PersistableFrameDescriptor](./persistableframedescriptor.md)
  The type of a window’s frame descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/removeframe(usingname:))*