# NSView.FullScreenModeOptionKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

These constants are keys that you can use in the options dictionary in [`enterFullScreenMode(_:withOptions:)`](./enterfullscreenmode%28_,withoptions%29.md) and [`exitFullScreenMode(options:)`](./exitfullscreenmode%28options%29.md).

**Availability**:
- macOS

## Declaration

```swift
struct FullScreenModeOptionKey
```

```c
typedef NSString * NSViewFullScreenModeOptionKey;
```

## Topics

### Type Properties
- [static let fullScreenModeAllScreens: NSView.FullScreenModeOptionKey](./fullscreenmodeoptionkey/fullscreenmodeallscreens.md)
  Key whose corresponding value specifies whether the view should take over all screens.
- [static let fullScreenModeApplicationPresentationOptions: NSView.FullScreenModeOptionKey](./fullscreenmodeoptionkey/fullscreenmodeapplicationpresentationoptions.md)
  Key whose corresponding value specifies the application presentation options.
- [static let fullScreenModeSetting: NSView.FullScreenModeOptionKey](./fullscreenmodeoptionkey/fullscreenmodesetting.md)
  Key whose corresponding value specifies the full screen mode setting.
- [static let fullScreenModeWindowLevel: NSView.FullScreenModeOptionKey](./fullscreenmodeoptionkey/fullscreenmodewindowlevel.md)
  Key whose corresponding value specifies the screen mode window level.
### Initializers
- [init(rawValue: String)](./fullscreenmodeoptionkey/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Drawing the View in Fullscreen Mode
- [func enterFullScreenMode(NSScreen, withOptions: [NSView.FullScreenModeOptionKey : Any]?) -> Bool](./enterfullscreenmode%28_,withoptions%29.md)
  Sets the view to full screen mode.
- [func exitFullScreenMode(options: [NSView.FullScreenModeOptionKey : Any]?)](./exitfullscreenmode%28options%29.md)
  Instructs the view to exit full screen mode.
- [var isInFullScreenMode: Bool](./isinfullscreenmode.md)
  A Boolean value indicating whether the view is in full screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/fullscreenmodeoptionkey)*