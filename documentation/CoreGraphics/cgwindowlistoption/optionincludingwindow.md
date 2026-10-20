# optionIncludingWindow

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Type Property

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
static var optionIncludingWindow: CGWindowListOption { get }
```

```c
kCGWindowListOptionIncludingWindow
```

#### Discussion

Include the specified window (from the `relativeToWindow` parameter) in the returned list. You must combine this option with the [`optionOnScreenAboveWindow`](./optiononscreenabovewindow.md) or [`optionOnScreenBelowWindow`](./optiononscreenbelowwindow.md) option to retrieve meaningful results.

## See Also

### Type Properties
- [static var excludeDesktopElements: CGWindowListOption](./excludedesktopelements.md)
- [static var optionAll: CGWindowListOption](./optionall.md)
- [static var optionOnScreenAboveWindow: CGWindowListOption](./optiononscreenabovewindow.md)
- [static var optionOnScreenBelowWindow: CGWindowListOption](./optiononscreenbelowwindow.md)
- [static var optionOnScreenOnly: CGWindowListOption](./optiononscreenonly.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgwindowlistoption/optionincludingwindow)*