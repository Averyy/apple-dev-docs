# fullScreenModeSetting

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Key whose corresponding value specifies the full screen mode setting.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let fullScreenModeSetting: NSView.FullScreenModeOptionKey
```

```c
extern NSViewFullScreenModeOptionKey const NSFullScreenModeSetting;
```

#### Discussion

The corresponding value is an instance of [`NSDictionary`](../../../Foundation/nsdictionary.md) that contains keys specified in Display Mode Standard Properties and Display Mode Optional Properties in [Quartz Display Services](../../../CoreGraphics/quartz-display-services.md).

When the [`fullScreenModeApplicationPresentationOptions`](./fullscreenmodeapplicationpresentationoptions.md) is specified in the options dictionary specifying this option as well will cause an exception.

## See Also

### Type Properties
- [static let fullScreenModeAllScreens: NSView.FullScreenModeOptionKey](./fullscreenmodeallscreens.md)
  Key whose corresponding value specifies whether the view should take over all screens.
- [static let fullScreenModeApplicationPresentationOptions: NSView.FullScreenModeOptionKey](./fullscreenmodeapplicationpresentationoptions.md)
  Key whose corresponding value specifies the application presentation options.
- [static let fullScreenModeWindowLevel: NSView.FullScreenModeOptionKey](./fullscreenmodewindowlevel.md)
  Key whose corresponding value specifies the screen mode window level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/fullscreenmodeoptionkey/fullscreenmodesetting)*