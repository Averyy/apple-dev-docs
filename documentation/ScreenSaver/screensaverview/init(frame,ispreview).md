# init(frame:isPreview:)

**Framework**: Screen Saver  
**Kind**: init  
**Role**: Initializer

Creates a newly allocated screen saver view with the specified frame rectangle and preview information.

**Availability**:
- macOS 10.0+

## Declaration

```swift
init?(frame: NSRect, isPreview: Bool)
```

```objc
- (instancetype) initWithFrame:(NSRect) frame isPreview:(BOOL) isPreview;
```

## Discussion

The screen saver application installs the new view object into the view hierarchy of an [`NSWindow`](../../AppKit/nswindow.md) before the animation begins. This method is the designated initializer for the [`ScreenSaverView`](../screensaverview.md) class. Returns `self`.

## Parameters

- `frame`: The frame rectangle for the view.
- `isPreview`: [`true`](../../Swift/true.md) if this view provides a preview for system settings, or [`false`](../../Swift/false.md) if the system fills the screen with your view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/init(frame:ispreview:))*