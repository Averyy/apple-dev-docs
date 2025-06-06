# worksWhenModal

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the panel receives keyboard and mouse events even when some other window is being run modally.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var worksWhenModal: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the panel receives keyboard and mouse events even when some other window is being run modally; when the value is [`false`](https://developer.apple.com/documentation/swift/false), the panel is prevented from receiving events while a modal loop or session is running. By default, the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), indicating a panel’s ineligibility for events during a modal loop or session. See [`How Modal Windows Work`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/WinPanel/Concepts/UsingModalWindows.html#//apple_ref/doc/uid/20000223) for more information on modal windows and panels.

## See Also

- [func runModalSession(NSApplication.ModalSession) -> NSApplication.ModalResponse](nsapplication/runmodalsession(_:).md)
  Runs a given modal session, as defined in a previous invocation of [`beginModalSession(for:)`](nsapplication/beginmodalsession(for:).md).
- [func runModal(for: NSWindow) -> NSApplication.ModalResponse](nsapplication/runmodal(for:).md)
  Starts a modal event loop for the specified window.
- [var isFloatingPanel: Bool](nspanel/isfloatingpanel.md)
  A Boolean value that indicates whether the receiver is a floating panel.
- [var becomesKeyOnlyIfNeeded: Bool](nspanel/becomeskeyonlyifneeded.md)
  A Boolean value that indicates whether the receiver becomes the key window only when needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspanel/workswhenmodal)*