# optionAll

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Type Property

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
static var optionAll: CGWindowListOption { get }
```

```c
kCGWindowListOptionAll
```

## Discussion

List all windows, including both onscreen and offscreen windows. When retrieving a list with this option, the `relativeToWindow` parameter should be set to [`kCGNullWindowID`](../kcgnullwindowid.md).

## See Also

### Type Properties
- [static var excludeDesktopElements: CGWindowListOption](./excludedesktopelements.md)
- [static var optionIncludingWindow: CGWindowListOption](./optionincludingwindow.md)
- [static var optionOnScreenAboveWindow: CGWindowListOption](./optiononscreenabovewindow.md)
- [static var optionOnScreenBelowWindow: CGWindowListOption](./optiononscreenbelowwindow.md)
- [static var optionOnScreenOnly: CGWindowListOption](./optiononscreenonly.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgwindowlistoption/optionall)*