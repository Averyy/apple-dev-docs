# fullScreenModeSetting

**Framework**: AppKit  
**Kind**: property

Key whose corresponding value specifies the full screen mode setting.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let fullScreenModeSetting: NSView.FullScreenModeOptionKey
```

#### Discussion

The corresponding value is an instance of [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary) that contains keys specified in Display Mode Standard Properties and Display Mode Optional Properties in [`Quartz Display Services`](https://developer.apple.com/documentation/CoreGraphics/quartz-display-services).

When the [`fullScreenModeApplicationPresentationOptions`](nsview/fullscreenmodeoptionkey/fullscreenmodeapplicationpresentationoptions.md) is specified in the options dictionary specifying this option as well will cause an exception.

## See Also

- [static let fullScreenModeAllScreens: NSView.FullScreenModeOptionKey](nsview/fullscreenmodeoptionkey/fullscreenmodeallscreens.md)
  Key whose corresponding value specifies whether the view should take over all screens.
- [static let fullScreenModeApplicationPresentationOptions: NSView.FullScreenModeOptionKey](nsview/fullscreenmodeoptionkey/fullscreenmodeapplicationpresentationoptions.md)
  Key whose corresponding value specifies the application presentation options.
- [static let fullScreenModeWindowLevel: NSView.FullScreenModeOptionKey](nsview/fullscreenmodeoptionkey/fullscreenmodewindowlevel.md)
  Key whose corresponding value specifies the screen mode window level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/fullscreenmodeoptionkey/fullscreenmodesetting)*