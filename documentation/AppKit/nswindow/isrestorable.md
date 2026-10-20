# isRestorable

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the window configuration is preserved between application launches.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var isRestorable: Bool { get set }
```

```objc
@property (getter=isRestorable) BOOL restorable;
```

#### Discussion

Set this property to [`true`](../../Swift/true.md) if you want the window to be preserved or [`false`](../../Swift/false.md) if you do not want it preserved. By default, the value of this property is [`true`](../../Swift/true.md) if the window’s [`styleMask`](./stylemask-swift.property.md) property includes the [`NSTitledWindowMask`](../nstitledwindowmask.md) flag. For other windows, the value is [`false`](../../Swift/false.md). Setting a value explicitly overrides the default values.

Windows should be preserved between launch cycles to maintain interface continuity for the user. During subsequent launch cycles, the system tries to recreate the window and restore its configuration to the preserved state. Configuration data is updated as needed and saved automatically by the system.

If you enable preservation for a given window, you should also specify a restoration class for the window using the [`restorationClass`](./restorationclass.md) property.

## See Also

### Handling Window Restoration
- [var restorationClass: (any NSWindowRestoration.Type)?](./restorationclass.md)
  The restoration class associated with the window.
- [func disableSnapshotRestoration()](./disablesnapshotrestoration%28%29.md)
  Disables snapshot restoration.
- [func enableSnapshotRestoration()](./enablesnapshotrestoration%28%29.md)
  Enables snapshot restoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/isrestorable)*