# isVisible

**Framework**: AppKit  
**Kind**: property

A Boolean value that determines whether the Media Library Browser panel is visible.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var isVisible: Bool { get set }
```

#### Discussion

Set this value to [`true`](https://developer.apple.com/documentation/Swift/true) to show the Media Library Browser or [`false`](https://developer.apple.com/documentation/Swift/false) to hide it.

This value can be read to determine the current visibility status of the panel.

## See Also

- [var frame: NSRect](nsmedialibrarybrowsercontroller/frame.md)
  The frame, in global coordinates, used to display the Media Library Browser panel.
- [func togglePanel(Any?)](nsmedialibrarybrowsercontroller/togglepanel(_:).md)
  Toggles the visibility of the Media Library Browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmedialibrarybrowsercontroller/isvisible)*