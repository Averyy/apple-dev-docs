# optionAll

**Framework**: Core Graphics  
**Kind**: property

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
static var optionAll: CGWindowListOption { get }
```

#### Discussion

List all windows, including both onscreen and offscreen windows. When retrieving a list with this option, the `relativeToWindow` parameter should be set to [`kCGNullWindowID`](kcgnullwindowid.md).

## See Also

- [static var excludeDesktopElements: CGWindowListOption](cgwindowlistoption/excludedesktopelements.md)
- [static var optionIncludingWindow: CGWindowListOption](cgwindowlistoption/optionincludingwindow.md)
- [static var optionOnScreenAboveWindow: CGWindowListOption](cgwindowlistoption/optiononscreenabovewindow.md)
- [static var optionOnScreenBelowWindow: CGWindowListOption](cgwindowlistoption/optiononscreenbelowwindow.md)
- [static var optionOnScreenOnly: CGWindowListOption](cgwindowlistoption/optiononscreenonly.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgwindowlistoption/optionall)*