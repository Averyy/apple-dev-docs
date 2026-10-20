# isVisible

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the Media Library Browser panel is visible.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var isVisible: Bool { get set }
```

```objc
@property (getter=isVisible) BOOL visible;
```

#### Discussion

Set this value to [`true`](../../Swift/true.md) to show the Media Library Browser or [`false`](../../Swift/false.md) to hide it.

This value can be read to determine the current visibility status of the panel.

## See Also

### Displaying the Media Library Browser Panel
- [var frame: NSRect](./frame.md)
  The frame, in global coordinates, used to display the Media Library Browser panel.
- [func togglePanel(Any?)](./togglepanel%28_%29.md)
  Toggles the visibility of the Media Library Browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmedialibrarybrowsercontroller/isvisible)*