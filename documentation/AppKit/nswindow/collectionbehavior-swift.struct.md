# NSWindow.CollectionBehavior

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Window collection behaviors related to Mission Control, Spaces, and Stage Manager.

**Availability**:
- macOS 10.5+

## Declaration

```swift
struct CollectionBehavior
```

```c
enum NSWindowCollectionBehavior : NSUInteger;
```

#### Overview

Collection behaviors are properties you set on windows to control their display characteristics in window management technologies. Use them to specify a preference on how windows behave in window management technologies like Mission Control, Spaces, and Stage Manager.

To set a collection behavior on a window, assign one or more behavior options to the window’s [`collectionBehavior`](./collectionbehavior-swift.property.md) property:

**Swift**:

```swift
window.collectionBehavior = .primary
```

**Objective-C**:

```objc
window.collectionBehavior = NSWindowCollectionBehaviorPrimary;
```

Not all collection behaviors apply to all windowing management technologies, and some are mutually exclusive to their respective groups. For example, [`primary`](./collectionbehavior-swift.struct/primary.md), [`auxiliary`](./collectionbehavior-swift.struct/auxiliary.md), and [`canJoinAllApplications`](./collectionbehavior-swift.struct/canjoinallapplications.md) only apply to full screen and Stage Manager. They’re also mutually exclusive. Specify at most one per window.

## Topics

### Window Collection Behaviors Creation
- [init(rawValue: UInt)](./collectionbehavior-swift.struct/init%28rawvalue%29.md)
  Creates a window collection behavior using the given raw value.
### Stage Manager and full screen
- [static var primary: NSWindow.CollectionBehavior](./collectionbehavior-swift.struct/primary.md)
  The behavior marking this window as primary for both Stage Manager and full screen.
- [static var auxiliary: NSWindow.CollectionBehavior](./collectionbehavior-swift.struct/auxiliary.md)
  The behavior marking this window as auxiliary for both Stage Manager and full screen.
- [static var canJoinAllApplications: NSWindow.CollectionBehavior](./collectionbehavior-swift.struct/canjoinallapplications.md)
  The behavior marking this window as one that can join all apps for both Stage Manager and full screen.
### Spaces
- [static var canJoinAllSpaces: NSWindow.CollectionBehavior](./collectionbehavior-swift.struct/canjoinallspaces.md)
  The window can appear in all spaces.
- [static var moveToActiveSpace: NSWindow.CollectionBehavior](./collectionbehavior-swift.struct/movetoactivespace.md)
  When the window becomes active, move it to the active space instead of switching spaces.
### Mission Control
- [static var stationary: NSWindow.CollectionBehavior](./collectionbehavior-swift.struct/stationary.md)
  Mission Control doesn’t affect the window, so it stays visible and stationary, like the desktop window.
### Spaces and Mission Control
- [static var managed: NSWindow.CollectionBehavior](./collectionbehavior-swift.struct/managed.md)
  The window participates in Mission Control and Spaces.
- [static var transient: NSWindow.CollectionBehavior](./collectionbehavior-swift.struct/transient.md)
  The window floats in Spaces and hides in Mission Control.
### Full screen
- [static var fullScreenPrimary: NSWindow.CollectionBehavior](./collectionbehavior-swift.struct/fullscreenprimary.md)
  The window can enter full-screen mode.
- [static var fullScreenAuxiliary: NSWindow.CollectionBehavior](./collectionbehavior-swift.struct/fullscreenauxiliary.md)
  The window displays on the same space as the full screen window.
- [static var fullScreenNone: NSWindow.CollectionBehavior](./collectionbehavior-swift.struct/fullscreennone.md)
  The window doesn’t support full-screen mode.
- [static var fullScreenAllowsTiling: NSWindow.CollectionBehavior](./collectionbehavior-swift.struct/fullscreenallowstiling.md)
  The window can be a secondary full screen tile even if it can’t be a full screen window itself.
- [static var fullScreenDisallowsTiling: NSWindow.CollectionBehavior](./collectionbehavior-swift.struct/fullscreendisallowstiling.md)
  The window doesn’t support being a full-screen tile window, but may support being a full-screen window.
### Window cycling
- [static var participatesInCycle: NSWindow.CollectionBehavior](./collectionbehavior-swift.struct/participatesincycle.md)
  The window participates in the window cycle for use with the Cycle Through Windows menu item.
- [static var ignoresCycle: NSWindow.CollectionBehavior](./collectionbehavior-swift.struct/ignorescycle.md)
  The window isn’t part of the window cycle for use with the Cycle Through Windows menu item.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Constants
- [NSWindow.SelectionDirection](./selectiondirection.md)
  Constants that specify the direction a window is currently using to change the key view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior-swift.struct)*