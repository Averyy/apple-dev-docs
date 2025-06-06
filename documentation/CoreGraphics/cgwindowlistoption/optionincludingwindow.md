# optionIncludingWindow

**Framework**: Core Graphics  
**Kind**: property

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
static var optionIncludingWindow: CGWindowListOption { get }
```

#### Discussion

Include the specified window (from the `relativeToWindow` parameter) in the returned list. You must combine this option with the [`optionOnScreenAboveWindow`](cgwindowlistoption/optiononscreenabovewindow.md) or [`optionOnScreenBelowWindow`](cgwindowlistoption/optiononscreenbelowwindow.md) option to retrieve meaningful results.

## See Also

- [static var excludeDesktopElements: CGWindowListOption](cgwindowlistoption/excludedesktopelements.md)
- [static var optionAll: CGWindowListOption](cgwindowlistoption/optionall.md)
- [static var optionOnScreenAboveWindow: CGWindowListOption](cgwindowlistoption/optiononscreenabovewindow.md)
- [static var optionOnScreenBelowWindow: CGWindowListOption](cgwindowlistoption/optiononscreenbelowwindow.md)
- [static var optionOnScreenOnly: CGWindowListOption](cgwindowlistoption/optiononscreenonly.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgwindowlistoption/optionincludingwindow)*