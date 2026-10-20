# fullScreenAuxiliary

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The window displays on the same space as the full screen window.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static var fullScreenAuxiliary: NSWindow.CollectionBehavior { get }
```

```c
NSWindowCollectionBehaviorFullScreenAuxiliary
```

## See Also

### Full screen
- [static var fullScreenPrimary: NSWindow.CollectionBehavior](./fullscreenprimary.md)
  The window can enter full-screen mode.
- [static var fullScreenNone: NSWindow.CollectionBehavior](./fullscreennone.md)
  The window doesn’t support full-screen mode.
- [static var fullScreenAllowsTiling: NSWindow.CollectionBehavior](./fullscreenallowstiling.md)
  The window can be a secondary full screen tile even if it can’t be a full screen window itself.
- [static var fullScreenDisallowsTiling: NSWindow.CollectionBehavior](./fullscreendisallowstiling.md)
  The window doesn’t support being a full-screen tile window, but may support being a full-screen window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior-swift.struct/fullscreenauxiliary)*