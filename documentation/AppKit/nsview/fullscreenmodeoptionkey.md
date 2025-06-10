# NSView.FullScreenModeOptionKey

**Framework**: AppKit  
**Kind**: struct

These constants are keys that you can use in the options dictionary in [`enterFullScreenMode(_:withOptions:)`](nsview/enterfullscreenmode(_:withoptions:).md) and [`exitFullScreenMode(options:)`](nsview/exitfullscreenmode(options:).md).

**Availability**:
- macOS ?+

## Declaration

```swift
struct FullScreenModeOptionKey
```

## Topics

### Type Properties
- [static let fullScreenModeAllScreens: NSView.FullScreenModeOptionKey](nsview/fullscreenmodeoptionkey/fullscreenmodeallscreens.md)
  Key whose corresponding value specifies whether the view should take over all screens.
- [static let fullScreenModeApplicationPresentationOptions: NSView.FullScreenModeOptionKey](nsview/fullscreenmodeoptionkey/fullscreenmodeapplicationpresentationoptions.md)
  Key whose corresponding value specifies the application presentation options.
- [static let fullScreenModeSetting: NSView.FullScreenModeOptionKey](nsview/fullscreenmodeoptionkey/fullscreenmodesetting.md)
  Key whose corresponding value specifies the full screen mode setting.
- [static let fullScreenModeWindowLevel: NSView.FullScreenModeOptionKey](nsview/fullscreenmodeoptionkey/fullscreenmodewindowlevel.md)
  Key whose corresponding value specifies the screen mode window level.
### Initializers
- [init(rawValue: String)](nsview/fullscreenmodeoptionkey/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func enterFullScreenMode(NSScreen, withOptions: [NSView.FullScreenModeOptionKey : Any]?) -> Bool](nsview/enterfullscreenmode(_:withoptions:).md)
  Sets the view to full screen mode.
- [func exitFullScreenMode(options: [NSView.FullScreenModeOptionKey : Any]?)](nsview/exitfullscreenmode(options:).md)
  Instructs the view to exit full screen mode.
- [var isInFullScreenMode: Bool](nsview/isinfullscreenmode.md)
  A Boolean value indicating whether the view is in full screen mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/fullscreenmodeoptionkey)*