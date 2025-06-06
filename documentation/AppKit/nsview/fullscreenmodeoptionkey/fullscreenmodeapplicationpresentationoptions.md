# fullScreenModeApplicationPresentationOptions

**Framework**: AppKit  
**Kind**: property

Key whose corresponding value specifies the application presentation options.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let fullScreenModeApplicationPresentationOptions: NSView.FullScreenModeOptionKey
```

#### Discussion

The corresponding value is an instance of [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) containing an unsigned integer value of [`NSApplication.PresentationOptions`](nsapplication/presentationoptions-swift.struct.md). Those options can be combined using the C bit-wise `OR` operator before created the `NSNumber` instance. See [`NSApplication`](nsapplication.md) constants section [`NSApplication.PresentationOptions`](nsapplication/presentationoptions-swift.struct.md) for more information on these options.

## See Also

- [static let fullScreenModeAllScreens: NSView.FullScreenModeOptionKey](nsview/fullscreenmodeoptionkey/fullscreenmodeallscreens.md)
  Key whose corresponding value specifies whether the view should take over all screens.
- [static let fullScreenModeSetting: NSView.FullScreenModeOptionKey](nsview/fullscreenmodeoptionkey/fullscreenmodesetting.md)
  Key whose corresponding value specifies the full screen mode setting.
- [static let fullScreenModeWindowLevel: NSView.FullScreenModeOptionKey](nsview/fullscreenmodeoptionkey/fullscreenmodewindowlevel.md)
  Key whose corresponding value specifies the screen mode window level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/fullscreenmodeoptionkey/fullscreenmodeapplicationpresentationoptions)*