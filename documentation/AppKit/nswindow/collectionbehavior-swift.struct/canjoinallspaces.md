# canJoinAllSpaces

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The window can appear in all spaces.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static var canJoinAllSpaces: NSWindow.CollectionBehavior { get }
```

```c
NSWindowCollectionBehaviorCanJoinAllSpaces
```

#### Discussion

The menu bar behaves this way.

## See Also

### Spaces
- [static var moveToActiveSpace: NSWindow.CollectionBehavior](./movetoactivespace.md)
  When the window becomes active, move it to the active space instead of switching spaces.
- [NSWindowCollectionBehaviorDefault](../../nswindowcollectionbehavior/nswindowcollectionbehaviordefault.md)
  The window appears in only one space at a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/collectionbehavior-swift.struct/canjoinallspaces)*