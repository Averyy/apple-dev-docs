# fullScreenAllowsTiling

**Framework**: Appkit  
**Kind**: property

The window can be a secondary full screen tile even if it can’t be a full screen window itself.

**Availability**:
- macOS 10.11+

## Declaration

```swift
static var fullScreenAllowsTiling: NSWindow.CollectionBehavior { get }
```

#### Discussion

The default behavior is to allow any window to participate in full-screen tiling, as long as it isn’t a panel or sheet and it meets certain requirements, such as being resizable. Windows that aren’t full screen capable can still become a secondary tile in full-screen.

A window can explicitly allow the system to place the window into a full-screen tile by including [`fullScreenAllowsTiling`](nswindow/collectionbehavior-swift.struct/fullscreenallowstiling.md). Even if a window allows full-screen tiling, the system may not put it in the tile if the window’s [`minFullScreenContentSize`](nswindow/minfullscreencontentsize.md) is too large.

A window can explicitly disallow the system from placing the window in a full-screen tile by including [`fullScreenDisallowsTiling`](nswindow/collectionbehavior-swift.struct/fullscreendisallowstiling.md). Windows that don’t support full-screen mode can use [`fullScreenDisallowsTiling`](nswindow/collectionbehavior-swift.struct/fullscreendisallowstiling.md) to prevent the system from putting the window into a full-screen tile. Full-screen windows can use [`fullScreenDisallowsTiling`](nswindow/collectionbehavior-swift.struct/fullscreendisallowstiling.md) to prevent the system from placing any other windows in its full-screen tile.

> **Note**:  The system raises an exception if you set both [`fullScreenAllowsTiling`](nswindow/collectionbehavior-swift.struct/fullscreenallowstiling.md) and [`fullScreenDisallowsTiling`](nswindow/collectionbehavior-swift.struct/fullscreendisallowstiling.md).

## See Also

- [static var fullScreenPrimary: NSWindow.CollectionBehavior](nswindow/collectionbehavior-swift.struct/fullscreenprimary.md)
  The window can enter full-screen mode.
- [static var fullScreenAuxiliary: NSWindow.CollectionBehavior](nswindow/collectionbehavior-swift.struct/fullscreenauxiliary.md)
  The window displays on the same space as the full screen window.
- [static var fullScreenNone: NSWindow.CollectionBehavior](nswindow/collectionbehavior-swift.struct/fullscreennone.md)
  The window doesn’t support full-screen mode.
- [static var fullScreenDisallowsTiling: NSWindow.CollectionBehavior](nswindow/collectionbehavior-swift.struct/fullscreendisallowstiling.md)
  The window doesn’t support being a full-screen tile window, but may support being a full-screen window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/nswindow/collectionbehavior-swift.struct/fullscreenallowstiling)*