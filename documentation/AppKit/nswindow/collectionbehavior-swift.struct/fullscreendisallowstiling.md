# fullScreenDisallowsTiling

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The window doesn’t support being a full-screen tile window, but may support being a full-screen window.

**Availability**:
- macOS 10.11+

## Declaration

```swift
static var fullScreenDisallowsTiling: NSWindow.CollectionBehavior { get }
```

```c
NSWindowCollectionBehaviorFullScreenDisallowsTiling
```

#### Discussion

For more information about full-screen tile window support, see [`fullScreenAllowsTiling`](./fullscreenallowstiling.md).

## See Also

### Full screen
- [static var fullScreenPrimary: NSWindow.CollectionBehavior](./fullscreenprimary.md)
  The window can enter full-screen mode.
- [static var fullScreenAuxiliary: NSWindow.CollectionBehavior](./fullscreenauxiliary.md)
  The window displays on the same space as the full screen window.
- [static var fullScreenNone: NSWindow.CollectionBehavior](./fullscreennone.md)
  The window doesn’t support full-screen mode.
- [static var fullScreenAllowsTiling: NSWindow.CollectionBehavior](./fullscreenallowstiling.md)
  The window can be a secondary full screen tile even if it can’t be a full screen window itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior-swift.struct/fullscreendisallowstiling)*