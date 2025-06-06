# disableSnapshotRestoration()

**Framework**: AppKit  
**Kind**: method

Disables snapshot restoration.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func disableSnapshotRestoration()
```

#### Discussion

After disabling snapshot restoration, the system doesn’t snapshot the window’s restorable state.

## See Also

- [var isRestorable: Bool](nswindow/isrestorable.md)
  A Boolean value indicating whether the window configuration is preserved between application launches.
- [var restorationClass: (any NSWindowRestoration.Type)?](nswindow/restorationclass.md)
  The restoration class associated with the window.
- [func enableSnapshotRestoration()](nswindow/enablesnapshotrestoration.md)
  Enables snapshot restoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/disablesnapshotrestoration())*