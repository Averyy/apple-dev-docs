# NSWindow.SelectionDirection

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the direction a window is currently using to change the key view.

**Availability**:
- macOS

## Declaration

```swift
enum SelectionDirection
```

```c
enum NSSelectionDirection : NSUInteger;
```

## Overview

The window uses these constants for [`keyViewSelectionDirection`](./keyviewselectiondirection.md).

## Topics

### Constants
- [NSWindow.SelectionDirection.directSelection](./selectiondirection/directselection.md)
  The window isn’t traversing the key view loop.
- [NSWindow.SelectionDirection.selectingNext](./selectiondirection/selectingnext.md)
  The window is proceeding to the next valid key view.
- [NSWindow.SelectionDirection.selectingPrevious](./selectiondirection/selectingprevious.md)
  The window is proceeding to the previous valid key view.
### Initializers
- [init?(rawValue: UInt)](./selectiondirection/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [NSWindow.ButtonType](./buttontype.md)
  Constants that provide a way to access standard title bar buttons.
- [NSRunLoop—Ordering Modes for NSWindow](../nsrunloop-ordering-modes-for-nsw.md)
  Constants that specify the priority for runloop messages.
- [NSWindow.Depth](./depth.md)
  A type that represents the depth, or amount of memory, for a single pixel in a window or screen.
- [NSWindow.BackingStoreType](./backingstoretype.md)
  Constants that specify how the window device buffers the drawing done in a window.
- [NSWindow.OrderingMode](./orderingmode.md)
  Constants that let you specify how a window is ordered relative to another window.
- [NSWindow.SharingType](./sharingtype-swift.enum.md)
  Constants that represent the access levels other processes can have to a window’s content.
- [NSWindow.NumberListOptions](./numberlistoptions.md)
  Options to use when retrieving window numbers from the system.
- [NSWindow.AnimationBehavior](./animationbehavior-swift.enum.md)
  Constants that control the automatic window animation behavior windows use when ordering to the front or out of view.
- [NSWindow.CollectionBehavior](./collectionbehavior-swift.struct.md)
  Window collection behaviors related to Mission Control, Spaces, and Stage Manager.
- [NSWindow.OcclusionState](./occlusionstate-swift.struct.md)
  Specifies whether the window is occluded.
- [NSWindow.TitleVisibility](./titlevisibility-swift.enum.md)
  Specifies the appearance of the window’s title bar area.
- [NSWindow.UserTabbingPreference](./usertabbingpreference-swift.enum.md)
  A value that indicates the user’s preference for window tabbing.
- [NSWindow.TabbingMode](./tabbingmode-swift.enum.md)
  The preferred tabbing behavior of a window.
- [Application Kit Version for Deferred Window Display Support](../application-kit-version-for-deferred-window-display-support.md)
  The version of the AppKit.framework containing a specific bug fix or capability.
- [Application Kit Version for Custom Sheet Position](../application-kit-version-for-custom-sheet-position.md)
  The version of the AppKit.framework containing a specific bug fix or capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/selectiondirection)*