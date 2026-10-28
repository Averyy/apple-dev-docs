# isWindowLoaded

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the nib file containing the receiver’s window has been loaded.

**Availability**:
- macOS

## Declaration

```swift
var isWindowLoaded: Bool { get }
```

```objc
@property (readonly, getter=isWindowLoaded) BOOL windowLoaded;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the nib file containing the receiver’s window has been loaded, [`false`](../../Swift/false.md) otherwise.

## See Also

### Loading and Displaying the Window
- [func loadWindow()](./loadwindow%28%29.md)
  Loads the receiver’s window from the nib file.
- [func showWindow(Any?)](./showwindow%28_%29.md)
  Displays the window associated with the receiver.
- [var window: NSWindow?](./window.md)
  The window owned by the receiver.
- [func windowDidLoad()](./windowdidload%28%29.md)
  Sent after the window owned by the receiver has been loaded.
- [func windowWillLoad()](./windowwillload%28%29.md)
  Sent before the window owned by the receiver is loaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowcontroller/iswindowloaded)*