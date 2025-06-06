# fullScreenDisallowsTiling

**Framework**: AppKit  
**Kind**: property

The window doesn’t support being a full-screen tile window, but may support being a full-screen window.

**Availability**:
- macOS 10.11+

## Declaration

```swift
static var fullScreenDisallowsTiling: NSWindow.CollectionBehavior { get }
```

#### Discussion

For more information about full-screen tile window support, see [`fullScreenAllowsTiling`](nswindow/collectionbehavior-swift.struct/fullscreenallowstiling.md).

## See Also

- [static var fullScreenPrimary: NSWindow.CollectionBehavior](nswindow/collectionbehavior-swift.struct/fullscreenprimary.md)
  The window can enter full-screen mode.
- [static var fullScreenAuxiliary: NSWindow.CollectionBehavior](nswindow/collectionbehavior-swift.struct/fullscreenauxiliary.md)
  The window displays on the same space as the full screen window.
- [static var fullScreenNone: NSWindow.CollectionBehavior](nswindow/collectionbehavior-swift.struct/fullscreennone.md)
  The window doesn’t support full-screen mode.
- [static var fullScreenAllowsTiling: NSWindow.CollectionBehavior](nswindow/collectionbehavior-swift.struct/fullscreenallowstiling.md)
  The window can be a secondary full screen tile even if it can’t be a full screen window itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior-swift.struct/fullscreendisallowstiling)*