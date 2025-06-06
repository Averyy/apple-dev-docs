# enableSnapshotRestoration()

**Framework**: AppKit  
**Kind**: method

Enables snapshot restoration.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func enableSnapshotRestoration()
```

#### Discussion

While snapshot restoration is enabled, the system snapshots the window’s restorable state.

## See Also

- [var isRestorable: Bool](nswindow/isrestorable.md)
  A Boolean value indicating whether the window configuration is preserved between application launches.
- [var restorationClass: (any NSWindowRestoration.Type)?](nswindow/restorationclass.md)
  The restoration class associated with the window.
- [func disableSnapshotRestoration()](nswindow/disablesnapshotrestoration.md)
  Disables snapshot restoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/enablesnapshotrestoration())*