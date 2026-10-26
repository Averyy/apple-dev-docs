# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

#### Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated symbols
- [static var texturedBackground: NSWindow.StyleMask](./nswindow/stylemask-swift.struct/texturedbackground.md)
  The window uses a textured background that darkens when the window is key or main and lightens when it is inactive, and may have a second gradient in the section below the window content.
### Deprecated constants
- [NSBorderlessWindowMask](./nsborderlesswindowmask.md)
  The window displays none of the usual peripheral elements.
- [NSTitledWindowMask](./nstitledwindowmask.md)
  The window displays a title bar.
- [NSClosableWindowMask](./nsclosablewindowmask.md)
  The window displays a close button.
- [NSMiniaturizableWindowMask](./nsminiaturizablewindowmask.md)
  The window displays a minimize button.
- [NSResizableWindowMask](./nsresizablewindowmask.md)
  The window displays a resize control.
- [NSTexturedBackgroundWindowMask](./nstexturedbackgroundwindowmask.md)
  The window displays with a metal-textured background. Additionally, the window may be moved by clicking and dragging anywhere in the window background. A bordered window with this mask gets rounded bottom corners.
- [NSUnifiedTitleAndToolbarWindowMask](./nsunifiedtitleandtoolbarwindowmask.md)
  The window’s title bar and toolbar have a unified look—that is, a continuous background. A horizontal separator line appears under the title bar and toolbar .
- [NSFullScreenWindowMask](./nsfullscreenwindowmask.md)
  The window can appear full screen. A fullscreen window does not draw its title bar, and may have special handling for its toolbar. This mask is automatically toggled when [`toggleFullScreen:`](./nswindow/togglefullscreen%28_%29.md) is called.
- [NSFullSizeContentViewWindowMask](./nsfullsizecontentviewwindowmask.md)
  When set, the content view consumes the full size of the window; it can be combined with other window style masks, but is only respected for windows with a title bar. Using this mask opts in to layer backing. Use the [`contentLayoutRect`](./nswindow/contentlayoutrect.md) or [`contentLayoutGuide`](./nswindow/contentlayoutguide.md) to lay out views underneath the title bar-toolbar area.
- [NSUnscaledWindowMask](./nsunscaledwindowmask.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/stylemask-deprecated-symbols)*