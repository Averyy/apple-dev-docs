# NSNonactivatingPanelMask

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The panel can receive keyboard input without activating the owning app.

**Availability**:
- macOS 10.0+ - Deprecated in 10.12

## Declaration

```c
static const NSWindowStyleMask NSNonactivatingPanelMask;
```

#### Discussion

Valid only for an instance of `NSPanel` or its subclasses; not valid for a window.

## See Also

### Deprecated
- [NSDocModalWindowMask](./nsdocmodalwindowmask.md)
  The panel is created as a modal sheet.
- [NSUtilityWindowMask](./nsutilitywindowmask.md)
  The panel is created as a floating window.
- [NSHUDWindowMask](./nshudwindowmask.md)
  The panel is created as a transparent panel (sometimes called a “heads-up display”).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsnonactivatingpanelmask)*