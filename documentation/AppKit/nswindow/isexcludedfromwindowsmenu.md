# isExcludedFromWindowsMenu

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window is excluded from the application’s Windows menu.

**Availability**:
- macOS

## Declaration

```swift
var isExcludedFromWindowsMenu: Bool { get set }
```

```objc
@property (getter=isExcludedFromWindowsMenu) BOOL excludedFromWindowsMenu;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the window is excluded from the Windows menu; otherwise, [`false`](../../Swift/false.md). The default initial setting is [`false`](../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/isexcludedfromwindowsmenu)*