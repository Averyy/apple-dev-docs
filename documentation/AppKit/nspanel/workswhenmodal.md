# worksWhenModal

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the panel receives keyboard and mouse events even when some other window is being run modally.

**Availability**:
- macOS

## Declaration

```swift
var worksWhenModal: Bool { get set }
```

```objc
@property BOOL worksWhenModal;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the panel receives keyboard and mouse events even when some other window is being run modally; when the value is [`false`](../../Swift/false.md), the panel is prevented from receiving events while a modal loop or session is running. By default, the value of this property is [`false`](../../Swift/false.md), indicating a panel’s ineligibility for events during a modal loop or session. See [How Modal Windows Work](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Concepts/UsingModalWindows.html#//apple_ref/doc/uid/20000223) for more information on modal windows and panels.

## See Also

### Related Documentation
- [func runModalSession(NSApplication.ModalSession) -> NSApplication.ModalResponse](../nsapplication/runmodalsession%28_%29.md)
  Runs a given modal session, as defined in a previous invocation of [`beginModalSession(for:)`](../nsapplication/beginmodalsession%28for%29.md).
- [func runModal(for: NSWindow) -> NSApplication.ModalResponse](../nsapplication/runmodal%28for%29.md)
  Starts a modal event loop for the specified window.
### Configuring Panels
- [var isFloatingPanel: Bool](./isfloatingpanel.md)
  A Boolean value that indicates whether the receiver is a floating panel.
- [var becomesKeyOnlyIfNeeded: Bool](./becomeskeyonlyifneeded.md)
  A Boolean value that indicates whether the receiver becomes the key window only when needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspanel/workswhenmodal)*