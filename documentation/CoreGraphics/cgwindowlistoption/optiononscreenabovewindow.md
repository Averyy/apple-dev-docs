# optionOnScreenAboveWindow

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Type Property

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
static var optionOnScreenAboveWindow: CGWindowListOption { get }
```

```c
kCGWindowListOptionOnScreenAboveWindow
```

#### Discussion

List all windows that are currently onscreen and in front of the window specified in the `relativeToWindow` parameter. Windows are returned in order from front to back.

## See Also

### Type Properties
- [static var excludeDesktopElements: CGWindowListOption](./excludedesktopelements.md)
- [static var optionAll: CGWindowListOption](./optionall.md)
- [static var optionIncludingWindow: CGWindowListOption](./optionincludingwindow.md)
- [static var optionOnScreenBelowWindow: CGWindowListOption](./optiononscreenbelowwindow.md)
- [static var optionOnScreenOnly: CGWindowListOption](./optiononscreenonly.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgwindowlistoption/optiononscreenabovewindow)*