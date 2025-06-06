# optionOnScreenBelowWindow

**Framework**: Core Graphics  
**Kind**: property

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
static var optionOnScreenBelowWindow: CGWindowListOption { get }
```

#### Discussion

List all windows that are currently onscreen and in behind the window specified in the `relativeToWindow` parameter. Windows are returned in order from front to back.

## See Also

- [static var excludeDesktopElements: CGWindowListOption](cgwindowlistoption/excludedesktopelements.md)
- [static var optionAll: CGWindowListOption](cgwindowlistoption/optionall.md)
- [static var optionIncludingWindow: CGWindowListOption](cgwindowlistoption/optionincludingwindow.md)
- [static var optionOnScreenAboveWindow: CGWindowListOption](cgwindowlistoption/optiononscreenabovewindow.md)
- [static var optionOnScreenOnly: CGWindowListOption](cgwindowlistoption/optiononscreenonly.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgwindowlistoption/optiononscreenbelowwindow)*