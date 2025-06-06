# auxiliary

**Framework**: AppKit  
**Kind**: property

The behavior marking this window as auxiliary for both Stage Manager and full screen.

**Availability**:
- macOS 13.0+

## Declaration

```swift
static var auxiliary: NSWindow.CollectionBehavior { get }
```

#### Discussion

Marking a window collection behavior as auxiliary means it becomes auxiliary for both Stage Manager and full screen display modes. Auxiliary windows prefer being shown alongside primary windows.

To set a different behavior in full screen, while keeping Stage Manager auxiliary, set a more specific behavior just for full screen mode (see [`fullScreenNone`](nswindow/collectionbehavior-swift.struct/fullscreennone.md)).

Use this collection behavior for About or Settings windows as well as utility panes.

> **Note**:  This property is mutually exclusive. Set only one of [`primary`](nswindow/collectionbehavior-swift.struct/primary.md), [`auxiliary`](nswindow/collectionbehavior-swift.struct/auxiliary.md), or [`canJoinAllApplications`](nswindow/collectionbehavior-swift.struct/canjoinallapplications.md) on a window handled by Stage Manager at a time.

 This property is mutually exclusive. Set only one of [`primary`](nswindow/collectionbehavior-swift.struct/primary.md), [`auxiliary`](nswindow/collectionbehavior-swift.struct/auxiliary.md), or [`canJoinAllApplications`](nswindow/collectionbehavior-swift.struct/canjoinallapplications.md) on a window handled by Stage Manager at a time.

## See Also

- [static var primary: NSWindow.CollectionBehavior](nswindow/collectionbehavior-swift.struct/primary.md)
  The behavior marking this window as primary for both Stage Manager and full screen.
- [static var canJoinAllApplications: NSWindow.CollectionBehavior](nswindow/collectionbehavior-swift.struct/canjoinallapplications.md)
  The behavior marking this window as one that can join all apps for both Stage Manager and full screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior-swift.struct/auxiliary)*