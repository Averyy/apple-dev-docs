# init(frame:isPreview:)

**Framework**: Screen Saver  
**Kind**: init

Creates a newly allocated screen saver view with the specified frame rectangle and preview information.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
init?(frame: NSRect, isPreview: Bool)
```

#### Discussion

The screen saver application installs the new view object into the view hierarchy of an [`NSWindow`](https://developer.apple.com/documentation/AppKit/NSWindow) before the animation begins. This method is the designated initializer for the [`ScreenSaverView`](screensaverview.md) class. Returns `self`.

## Parameters

- `frame`: The frame rectangle for the view.
- `isPreview`:   if this view provides a preview for system settings, or   if the system fills the screen with your view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/init(frame:ispreview:))*