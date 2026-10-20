# disableSnapshotRestoration()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Disables snapshot restoration.

**Availability**:
- macOS

## Declaration

```swift
func disableSnapshotRestoration()
```

```objc
- (void) disableSnapshotRestoration;
```

#### Discussion

After disabling snapshot restoration, the system doesn’t snapshot the window’s restorable state.

## See Also

### Handling Window Restoration
- [var isRestorable: Bool](./isrestorable.md)
  A Boolean value indicating whether the window configuration is preserved between application launches.
- [var restorationClass: (any NSWindowRestoration.Type)?](./restorationclass.md)
  The restoration class associated with the window.
- [func enableSnapshotRestoration()](./enablesnapshotrestoration%28%29.md)
  Enables snapshot restoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/disablesnapshotrestoration())*