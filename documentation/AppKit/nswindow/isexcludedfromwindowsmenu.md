# isExcludedFromWindowsMenu

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window is excluded from the application’s Windows menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isExcludedFromWindowsMenu: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the window is excluded from the Windows menu; otherwise, [`false`](https://developer.apple.com/documentation/swift/false). The default initial setting is [`false`](https://developer.apple.com/documentation/swift/false).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/isexcludedfromwindowsmenu)*