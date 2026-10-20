# optionOnScreenOnly

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Type Property

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
static var optionOnScreenOnly: CGWindowListOption { get }
```

```c
kCGWindowListOptionOnScreenOnly
```

#### Discussion

List all windows that are currently onscreen. Windows are returned in order from front to back. When retrieving a list with this option, the `relativeToWindow` parameter should be set to [`kCGNullWindowID`](../kcgnullwindowid.md).

## See Also

### Type Properties
- [static var excludeDesktopElements: CGWindowListOption](./excludedesktopelements.md)
- [static var optionAll: CGWindowListOption](./optionall.md)
- [static var optionIncludingWindow: CGWindowListOption](./optionincludingwindow.md)
- [static var optionOnScreenAboveWindow: CGWindowListOption](./optiononscreenabovewindow.md)
- [static var optionOnScreenBelowWindow: CGWindowListOption](./optiononscreenbelowwindow.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgwindowlistoption/optiononscreenonly)*