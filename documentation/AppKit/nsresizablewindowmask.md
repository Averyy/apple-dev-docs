# NSResizableWindowMask

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The window displays a resize control.

**Availability**:
- macOS 10.0+ - Deprecated in 10.12

## Declaration

```c
static const NSWindowStyleMask NSResizableWindowMask;
```

## See Also

### Deprecated constants
- [NSBorderlessWindowMask](./nsborderlesswindowmask.md)
  The window displays none of the usual peripheral elements.
- [NSTitledWindowMask](./nstitledwindowmask.md)
  The window displays a title bar.
- [NSClosableWindowMask](./nsclosablewindowmask.md)
  The window displays a close button.
- [NSMiniaturizableWindowMask](./nsminiaturizablewindowmask.md)
  The window displays a minimize button.
- [NSTexturedBackgroundWindowMask](./nstexturedbackgroundwindowmask.md)
  The window displays with a metal-textured background. Additionally, the window may be moved by clicking and dragging anywhere in the window background. A bordered window with this mask gets rounded bottom corners.
- [NSUnifiedTitleAndToolbarWindowMask](./nsunifiedtitleandtoolbarwindowmask.md)
  The window’s title bar and toolbar have a unified look—that is, a continuous background. A horizontal separator line appears under the title bar and toolbar .
- [NSFullScreenWindowMask](./nsfullscreenwindowmask.md)
  The window can appear full screen. A fullscreen window does not draw its title bar, and may have special handling for its toolbar. This mask is automatically toggled when [`toggleFullScreen(_:)`](./nswindow/togglefullscreen%28_%29.md) is called.
- [NSFullSizeContentViewWindowMask](./nsfullsizecontentviewwindowmask.md)
  When set, the content view consumes the full size of the window; it can be combined with other window style masks, but is only respected for windows with a title bar. Using this mask opts in to layer backing. Use the [`contentLayoutRect`](./nswindow/contentlayoutrect.md) or [`contentLayoutGuide`](./nswindow/contentlayoutguide.md) to lay out views underneath the title bar-toolbar area.
- [NSUnscaledWindowMask](./nsunscaledwindowmask.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresizablewindowmask)*