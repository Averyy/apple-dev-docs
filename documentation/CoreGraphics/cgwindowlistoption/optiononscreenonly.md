# optionOnScreenOnly

**Framework**: Core Graphics  
**Kind**: property

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
static var optionOnScreenOnly: CGWindowListOption { get }
```

#### Discussion

List all windows that are currently onscreen. Windows are returned in order from front to back. When retrieving a list with this option, the `relativeToWindow` parameter should be set to [`kCGNullWindowID`](kcgnullwindowid.md).

## See Also

- [static var excludeDesktopElements: CGWindowListOption](cgwindowlistoption/excludedesktopelements.md)
- [static var optionAll: CGWindowListOption](cgwindowlistoption/optionall.md)
- [static var optionIncludingWindow: CGWindowListOption](cgwindowlistoption/optionincludingwindow.md)
- [static var optionOnScreenAboveWindow: CGWindowListOption](cgwindowlistoption/optiononscreenabovewindow.md)
- [static var optionOnScreenBelowWindow: CGWindowListOption](cgwindowlistoption/optiononscreenbelowwindow.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgwindowlistoption/optiononscreenonly)*