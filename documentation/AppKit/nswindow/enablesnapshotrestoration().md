# enableSnapshotRestoration()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Enables snapshot restoration.

**Availability**:
- macOS

## Declaration

```swift
func enableSnapshotRestoration()
```

```objc
- (void) enableSnapshotRestoration;
```

#### Discussion

While snapshot restoration is enabled, the system snapshots the window’s restorable state.

## See Also

### Handling Window Restoration
- [var isRestorable: Bool](./isrestorable.md)
  A Boolean value indicating whether the window configuration is preserved between application launches.
- [var restorationClass: (any NSWindowRestoration.Type)?](./restorationclass.md)
  The restoration class associated with the window.
- [func disableSnapshotRestoration()](./disablesnapshotrestoration%28%29.md)
  Disables snapshot restoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/enablesnapshotrestoration())*