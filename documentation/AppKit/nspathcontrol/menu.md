# menu

**Framework**: AppKit  
**Kind**: property

The menu that is used for the path control’s cells.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var menu: NSMenu? { get set }
```

#### Discussion

This property overrides the [`NSView`](nsview.md) implementation of `menu` and forwards the message to the `NSPathControlCell`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspathcontrol/menu)*