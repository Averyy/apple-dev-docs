# isMiniaturized

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window is minimized.

**Availability**:
- macOS

## Declaration

```swift
var isMiniaturized: Bool { get }
```

```objc
@property (readonly, getter=isMiniaturized) BOOL miniaturized;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the window is minimized; otherwise, [`false`](../../Swift/false.md). A minimized window is removed from the screen and replaced by a image, icon, or button that represents it, called the counterpart.

## See Also

### Minimizing Windows
- [func performMiniaturize(Any?)](./performminiaturize%28_%29.md)
  Simulates the user clicking the minimize button by momentarily highlighting the button, then minimizing the window.
- [func miniaturize(Any?)](./miniaturize%28_%29.md)
  Removes the window from the screen list and displays the minimized window in the Dock.
- [func deminiaturize(Any?)](./deminiaturize%28_%29.md)
  De-minimizes the window.
- [var miniwindowImage: NSImage?](./miniwindowimage.md)
  The custom miniaturized window image of the window.
- [var miniwindowTitle: String!](./miniwindowtitle.md)
  The title displayed in the window’s minimized window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/isminiaturized)*