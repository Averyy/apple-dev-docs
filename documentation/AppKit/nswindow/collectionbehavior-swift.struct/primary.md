# primary

**Framework**: AppKit  
**Kind**: property

The behavior marking this window as primary for both Stage Manager and full screen.

**Availability**:
- macOS 13.0+

## Declaration

```swift
static var primary: NSWindow.CollectionBehavior { get }
```

#### Discussion

Marking a window collection behavior as primary means it becomes primary for both Stage Manager and full screen display modes.

To set a different behavior in full screen while keeping Stage Manager primary, set a more specific behavior just for full screen mode (see [`fullScreenAuxiliary`](nswindow/collectionbehavior-swift.struct/fullscreenauxiliary.md)).

Use this collection behavior for document or viewer windows.

> **Note**:  This property is mutually exclusive. Set only one of [`primary`](nswindow/collectionbehavior-swift.struct/primary.md), [`auxiliary`](nswindow/collectionbehavior-swift.struct/auxiliary.md), or [`canJoinAllApplications`](nswindow/collectionbehavior-swift.struct/canjoinallapplications.md) on a window handled by Stage Manager at a time.

## See Also

- [static var auxiliary: NSWindow.CollectionBehavior](nswindow/collectionbehavior-swift.struct/auxiliary.md)
  The behavior marking this window as auxiliary for both Stage Manager and full screen.
- [static var canJoinAllApplications: NSWindow.CollectionBehavior](nswindow/collectionbehavior-swift.struct/canjoinallapplications.md)
  The behavior marking this window as one that can join all apps for both Stage Manager and full screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior-swift.struct/primary)*