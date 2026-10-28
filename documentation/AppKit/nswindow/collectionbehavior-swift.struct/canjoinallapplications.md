# canJoinAllApplications

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The behavior marking this window as one that can join all apps for both Stage Manager and full screen.

**Availability**:
- macOS 13.0+

## Declaration

```swift
static var canJoinAllApplications: NSWindow.CollectionBehavior { get }
```

```c
NSWindowCollectionBehaviorCanJoinAllApplications
```

## Discussion

Windows marked with this behavior don’t participate in Stage Manager layout but can join the windows of other apps in full screen spaces when eligible.

Use this collection behavior for floating windows and system overlays. To opt out of joining other apps’ full screen spaces use [`fullScreenPrimary`](./fullscreenprimary.md).

> **Note**:  This property is mutually exclusive. Set only one of [`primary`](./primary.md), [`auxiliary`](./auxiliary.md), or [`canJoinAllApplications`](./canjoinallapplications.md) on a window handled by Stage Manager at a time.

## See Also

### Stage Manager and full screen
- [static var primary: NSWindow.CollectionBehavior](./primary.md)
  The behavior marking this window as primary for both Stage Manager and full screen.
- [static var auxiliary: NSWindow.CollectionBehavior](./auxiliary.md)
  The behavior marking this window as auxiliary for both Stage Manager and full screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior-swift.struct/canjoinallapplications)*