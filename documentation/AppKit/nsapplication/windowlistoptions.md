# NSApplication.WindowListOptions

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

This constant indicates a window ordering.

**Availability**:
- macOS 10.12+

## Declaration

```swift
struct WindowListOptions
```

```c
enum NSWindowListOptions : NSInteger;
```

## Topics

### Options
- [static var orderedFrontToBack: NSApplication.WindowListOptions](./windowlistoptions/orderedfronttoback.md)
  The app’s onscreen windows in front-to-back order. By default, [`windows`](./windows.md) is used.
### Initializers
- [init(rawValue: Int)](./windowlistoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Managing App Windows
- [var keyWindow: NSWindow?](./keywindow.md)
  The window that currently receives keyboard events.
- [var mainWindow: NSWindow?](./mainwindow.md)
  The app’s main window.
- [func window(withWindowNumber: Int) -> NSWindow?](./window%28withwindownumber%29.md)
  Returns the window corresponding to the specified window number.
- [var windows: [NSWindow]](./windows.md)
  An array of the app’s window objects.
- [func enumerateWindows(options: NSApplication.WindowListOptions, using: (NSWindow, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratewindows%28options,using%29.md)
  Executes a block for each of the app’s windows.
- [func makeWindowsPerform(Selector, inOrder: Bool) -> NSWindow?](./makewindowsperform%28_,inorder%29.md)
  Sends the specified message to each of the app’s window objects until one returns a non-`nil` value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/windowlistoptions)*