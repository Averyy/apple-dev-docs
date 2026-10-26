# NSHUDWindowMask

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The panel is created as a transparent panel (sometimes called a “heads-up display”).

**Availability**:
- macOS 10.0+ - Deprecated in 10.12

## Declaration

```c
static const NSWindowStyleMask NSHUDWindowMask;
```

#### Discussion

Valid only for an instance of `NSPanel` or its subclasses; not valid for a window.

Using the C bitwise OR operator, `NSHUDWindowMask` can be combined with other style masks (some of which are documented in Window Style Masks) with the following results:

- **`NSBorderlessWindowMask`**: Borderless window with transparent panel transparency and window level. A panel that uses `NSBorderlessWindowMask` can’t become key unless you implement [`canBecomeKey`](./nswindow/canbecomekey.md) to return [`true`](../Swift/true.md). Note that you can also set a panel’s style mask to `NSBorderlessWindowMask` in Interface Builder by deselecting Title Bar in the Appearance section of the Attributes inspector.
- **`NSTitledWindowMask` `|` `NSUtilityWindowMask`**: Titled window with transparent panel transparency and window level. This combination can be additionally combined with any of the following:

  - **`NSClosableWindowMask`**: Titled window with transparent panel close box, transparency, and window level.
  - **`NSResizableWindowMask`**: Titled window with transparent panel resize corner, transparency, and window level.
  - **`NSNonactivatingPanelMask`**: No effect on appearance, but owning app is not necessarily active when this window is the key window.

The following constants cannot be combined with `NSHUDWindowMask`: `NSMiniaturizableWindowMask`, `NSTexturedBackgroundWindowMask`, `NSDocModalWindowMask`, and `NSUnifiedTitleAndToolbarWindowMask`.

## See Also

### Deprecated
- [NSDocModalWindowMask](./nsdocmodalwindowmask.md)
  The panel is created as a modal sheet.
- [NSUtilityWindowMask](./nsutilitywindowmask.md)
  The panel is created as a floating window.
- [NSNonactivatingPanelMask](./nsnonactivatingpanelmask.md)
  The panel can receive keyboard input without activating the owning app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshudwindowmask)*