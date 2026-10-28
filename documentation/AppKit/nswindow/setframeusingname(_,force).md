# setFrameUsingName(_:force:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the window’s frame rectangle by reading the rectangle data stored under a given name from the defaults system. Can operate on non-resizable windows.

**Availability**:
- macOS

## Declaration

```swift
func setFrameUsingName(_ name: NSWindow.FrameAutosaveName, force: Bool) -> Bool
```

```objc
- (BOOL) setFrameUsingName:(NSWindowFrameAutosaveName) name force:(BOOL) force;
```

## Return Value

[`true`](../../Swift/true.md) when `name` is read and the frame is set successfully; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `name`: The name of the frame to read.
- `force`: [`true`](../../Swift/true.md) to use [`setFrameUsingName(_:)`](./setframeusingname%28_%29.md) on a non-resizable window; [`false`](../../Swift/false.md) to fail on a non-resizable window.

## See Also

### Managing Window Frames in User Defaults
- [class func removeFrame(usingName: NSWindow.FrameAutosaveName)](./removeframe%28usingname%29.md)
  Removes the frame data stored under a given name from the application’s user defaults.
- [func setFrameUsingName(NSWindow.FrameAutosaveName) -> Bool](./setframeusingname%28_%29.md)
  Sets the window’s frame rectangle by reading the rectangle data stored under a given name from the defaults system.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/setframeusingname(_:force:))*