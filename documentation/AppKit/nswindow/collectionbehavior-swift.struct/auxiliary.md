# auxiliary

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The behavior marking this window as auxiliary for both Stage Manager and full screen.

**Availability**:
- macOS 13.0+

## Declaration

```swift
static var auxiliary: NSWindow.CollectionBehavior { get }
```

```c
NSWindowCollectionBehaviorAuxiliary
```

#### Discussion

Marking a window collection behavior as auxiliary means it becomes auxiliary for both Stage Manager and full screen display modes. Auxiliary windows prefer being shown alongside primary windows.

To set a different behavior in full screen, while keeping Stage Manager auxiliary, set a more specific behavior just for full screen mode (see [`fullScreenNone`](./fullscreennone.md)).

**Swift**:

```swift
window.collectionBehavior = [.auxiliary, .fullScreenNone]
```

**Objective-C**:

```objc
window.collectionBehavior |= (NSWindowCollectionBehaviorAuxiliary | NSWindowCollectionBehaviorFullScreenNone);
```

Use this collection behavior for About or Settings windows as well as utility panes.

> **Note**:  This property is mutually exclusive. Set only one of [`primary`](./primary.md), [`auxiliary`](./auxiliary.md), or [`canJoinAllApplications`](./canjoinallapplications.md) on a window handled by Stage Manager at a time.

## See Also

### Stage Manager and full screen
- [static var primary: NSWindow.CollectionBehavior](./primary.md)
  The behavior marking this window as primary for both Stage Manager and full screen.
- [static var canJoinAllApplications: NSWindow.CollectionBehavior](./canjoinallapplications.md)
  The behavior marking this window as one that can join all apps for both Stage Manager and full screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior-swift.struct/auxiliary)*