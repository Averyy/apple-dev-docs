# isRestorable

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the window configuration is preserved between application launches.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var isRestorable: Bool { get set }
```

#### Discussion

Set this property to [`true`](https://developer.apple.com/documentation/swift/true) if you want the window to be preserved or [`false`](https://developer.apple.com/documentation/swift/false) if you do not want it preserved. By default, the value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the window’s [`styleMask`](nswindow/stylemask-swift.property.md) property includes the [`NSTitledWindowMask`](nstitledwindowmask.md) flag. For other windows, the value is [`false`](https://developer.apple.com/documentation/swift/false). Setting a value explicitly overrides the default values.

Windows should be preserved between launch cycles to maintain interface continuity for the user. During subsequent launch cycles, the system tries to recreate the window and restore its configuration to the preserved state. Configuration data is updated as needed and saved automatically by the system.

If you enable preservation for a given window, you should also specify a restoration class for the window using the [`restorationClass`](nswindow/restorationclass.md) property.

## See Also

- [var restorationClass: (any NSWindowRestoration.Type)?](nswindow/restorationclass.md)
  The restoration class associated with the window.
- [func disableSnapshotRestoration()](nswindow/disablesnapshotrestoration.md)
  Disables snapshot restoration.
- [func enableSnapshotRestoration()](nswindow/enablesnapshotrestoration.md)
  Enables snapshot restoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/isrestorable)*