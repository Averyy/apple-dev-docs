# saveFrame(usingName:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Saves the window’s frame rectangle in the user defaults system under a given name.

**Availability**:
- macOS

## Declaration

```swift
func saveFrame(usingName name: NSWindow.FrameAutosaveName)
```

```objc
- (void) saveFrameUsingName:(NSWindowFrameAutosaveName) name;
```

## Discussion

With the companion method [`setFrameUsingName(_:)`](./setframeusingname%28_%29.md), you can save and reset an `NSWindow` object’s frame over various launches of an application. The default is owned by the application and stored under the name “`NSWindow Frame name`”. See [`UserDefaults`](../../Foundation/userdefaults.md) for more information.

## Parameters

- `name`: The name under which the frame is to be saved.

## See Also

### Managing Window Frames in User Defaults
- [class func removeFrame(usingName: NSWindow.FrameAutosaveName)](./removeframe%28usingname%29.md)
  Removes the frame data stored under a given name from the application’s user defaults.
- [func setFrameUsingName(NSWindow.FrameAutosaveName) -> Bool](./setframeusingname%28_%29.md)
  Sets the window’s frame rectangle by reading the rectangle data stored under a given name from the defaults system.
- [func setFrameUsingName(NSWindow.FrameAutosaveName, force: Bool) -> Bool](./setframeusingname%28_,force%29.md)
  Sets the window’s frame rectangle by reading the rectangle data stored under a given name from the defaults system. Can operate on non-resizable windows.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/saveframe(usingname:))*