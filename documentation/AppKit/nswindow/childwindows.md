# childWindows

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of the window’s attached child windows.

**Availability**:
- macOS

## Declaration

```swift
var childWindows: [NSWindow]? { get }
```

```objc
@property (copy, readonly, nullable) NSArray<__kindof NSWindow *> * childWindows;
```

## See Also

### Managing Attached Windows
- [func addChildWindow(NSWindow, ordered: NSWindow.OrderingMode)](./addchildwindow%28_,ordered%29.md)
  Adds a given window as a child window of the window.
- [func removeChildWindow(NSWindow)](./removechildwindow%28_%29.md)
  Detaches a given child window from the window.
- [var parent: NSWindow?](./parent.md)
  The parent window to which the window is attached as a child.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/childwindows)*