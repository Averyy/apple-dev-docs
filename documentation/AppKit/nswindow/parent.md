# parent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The parent window to which the window is attached as a child.

**Availability**:
- macOS

## Declaration

```swift
weak var parent: NSWindow? { get set }
```

```objc
@property (weak, nullable) NSWindow * parentWindow;
```

#### Discussion

This property should be set from a subclass when it is overridden by a subclass’s implementation. It should not be set otherwise.

Note that calling [`orderOut(_:)`](./orderout%28_%29.md) on a child window causes the window to be removed from its parent window before it is itself removed.

## See Also

### Managing Attached Windows
- [var childWindows: [NSWindow]?](./childwindows.md)
  An array of the window’s attached child windows.
- [func addChildWindow(NSWindow, ordered: NSWindow.OrderingMode)](./addchildwindow%28_,ordered%29.md)
  Adds a given window as a child window of the window.
- [func removeChildWindow(NSWindow)](./removechildwindow%28_%29.md)
  Detaches a given child window from the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/parent)*