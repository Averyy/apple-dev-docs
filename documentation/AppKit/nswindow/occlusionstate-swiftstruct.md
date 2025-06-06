# NSWindow.OcclusionState

**Framework**: AppKit  
**Kind**: struct

Specifies whether the window is occluded.

**Availability**:
- macOS 10.9+

## Declaration

```swift
struct OcclusionState
```

## Topics

### Constants
- [static var visible: NSWindow.OcclusionState](nswindow/occlusionstate-swift.struct/visible.md)
  If set, at least part of the window is visible; if not set, the entire window is occluded. A window that has a nonrectangular shape can be entirely occluded onscreen, but if its bounding box falls into a visible region, the window is considered to be visible. Note that a completely transparent window may also be considered visible.
### Occlusion State Creation
- [init(rawValue: UInt)](nswindow/occlusionstate-swift.struct/init(rawvalue:).md)
  Creates an occlusion state using the given raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [NSWindow.SelectionDirection](nswindow/selectiondirection.md)
  Constants that specify the direction a window is currently using to change the key view.
- [NSWindow.ButtonType](nswindow/buttontype.md)
  Constants that provide a way to access standard title bar buttons.
- [NSRunLoop—Ordering Modes for NSWindow](nsrunloop-ordering-modes-for-nsw.md)
  Constants that specify the priority for runloop messages.
- [NSWindow.Depth](nswindow/depth.md)
  A type that represents the depth, or amount of memory, for a single pixel in a window or screen.
- [NSWindow.BackingStoreType](nswindow/backingstoretype.md)
  Constants that specify how the window device buffers the drawing done in a window.
- [NSWindow.OrderingMode](nswindow/orderingmode.md)
  Constants that let you specify how a window is ordered relative to another window.
- [NSWindow.SharingType](nswindow/sharingtype-swift.enum.md)
  Constants that represent the access levels other processes can have to a window’s content.
- [NSWindow.NumberListOptions](nswindow/numberlistoptions.md)
  Options to use when retrieving window numbers from the system.
- [NSWindow.AnimationBehavior](nswindow/animationbehavior-swift.enum.md)
  Constants that control the automatic window animation behavior windows use when ordering to the front or out of view.
- [NSWindow.CollectionBehavior](nswindow/collectionbehavior-swift.struct.md)
  Window collection behaviors related to Mission Control, Spaces, and Stage Manager.
- [NSWindow.TitleVisibility](nswindow/titlevisibility-swift.enum.md)
  Specifies the appearance of the window’s title bar area.
- [NSWindow.UserTabbingPreference](nswindow/usertabbingpreference-swift.enum.md)
  A value that indicates the user’s preference for window tabbing.
- [NSWindow.TabbingMode](nswindow/tabbingmode-swift.enum.md)
  The preferred tabbing behavior of a window.
- [Application Kit Version for Deferred Window Display Support](application-kit-version-for-deferred-window-display-support.md)
  The version of the AppKit.framework containing a specific bug fix or capability.
- [Application Kit Version for Custom Sheet Position](application-kit-version-for-custom-sheet-position.md)
  The version of the AppKit.framework containing a specific bug fix or capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/occlusionstate-swift.struct)*