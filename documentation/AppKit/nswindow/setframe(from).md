# setFrame(from:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the window’s frame rectangle from a given string representation.

**Availability**:
- macOS

## Declaration

```swift
func setFrame(from string: NSWindow.PersistableFrameDescriptor)
```

```objc
- (void) setFrameFromString:(NSWindowPersistableFrameDescriptor) string;
```

#### Discussion

If the window is not resizable, this method will not resize the window. The frame is constrained according to the window’s minimum and maximum size settings. This method causes a [`windowWillResize(_:to:)`](../nswindowdelegate/windowwillresize%28_,to%29.md) message to be sent to the delegate.

## Parameters

- `string`: A string representation of a frame rectangle, previously accessed using [`frameDescriptor`](./framedescriptor.md).

## See Also

### Managing Window Frames in User Defaults
- [class func removeFrame(usingName: NSWindow.FrameAutosaveName)](./removeframe%28usingname%29.md)
  Removes the frame data stored under a given name from the application’s user defaults.
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
- [typealias PersistableFrameDescriptor](./persistableframedescriptor.md)
  The type of a window’s frame descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/setframe(from:))*