# primary

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The behavior marking this window as primary for both Stage Manager and full screen.

**Availability**:
- macOS 13.0+

## Declaration

```swift
static var primary: NSWindow.CollectionBehavior { get }
```

```c
NSWindowCollectionBehaviorPrimary
```

## Discussion

Marking a window collection behavior as primary means it becomes primary for both Stage Manager and full screen display modes.

To set a different behavior in full screen while keeping Stage Manager primary, set a more specific behavior just for full screen mode (see [`fullScreenAuxiliary`](./fullscreenauxiliary.md)).

**Swift**:

```swift
window.collectionBehavior = [.primary, .fullScreenAuxiliary]
```

**Objective-C**:

```objc
window.collectionBehavior |= (NSWindowCollectionBehaviorPrimary | NSWindowCollectionBehaviorFullScreenAuxiliary);
```

Use this collection behavior for document or viewer windows.

> **Note**:  This property is mutually exclusive. Set only one of [`primary`](./primary.md), [`auxiliary`](./auxiliary.md), or [`canJoinAllApplications`](./canjoinallapplications.md) on a window handled by Stage Manager at a time.

## See Also

### Stage Manager and full screen
- [static var auxiliary: NSWindow.CollectionBehavior](./auxiliary.md)
  The behavior marking this window as auxiliary for both Stage Manager and full screen.
- [static var canJoinAllApplications: NSWindow.CollectionBehavior](./canjoinallapplications.md)
  The behavior marking this window as one that can join all apps for both Stage Manager and full screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior-swift.struct/primary)*