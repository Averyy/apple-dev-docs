# drawerWillResizeContents(_:to:)

**Framework**: AppKit  
**Kind**: method

Invoked when the user resizes the drawer or parent.

**Availability**:
- macOS 10.0+

## Declaration

```swift
optional func drawerWillResizeContents(_ sender: NSDrawer, to contentSize: NSSize) -> NSSize
```

#### Return Value

The size that the drawer should be resized to. To resize to a different size, simply return the desired size from this method; to avoid resizing, return the current size.

#### Discussion

The receiver’s minimum and maximum size constraints have already been applied when this method is invoked. While the user is resizing an `NSDrawer` or its parent, the delegate is sent a series of `windowWillResize` messages as the `NSDrawer` or parent window is dragged.

## Parameters

- `sender`: The drawer being resized.
- `contentSize`: The proposed new size of the drawer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawerdelegate/drawerwillresizecontents(_:to:))*