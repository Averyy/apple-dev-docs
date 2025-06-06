# exitFullScreenMode(options:)

**Framework**: AppKit  
**Kind**: method

Instructs the view to exit full screen mode.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func exitFullScreenMode(options: [NSView.FullScreenModeOptionKey : Any]? = nil)
```

#### Discussion

When the [`fullScreenModeApplicationPresentationOptions`](nsview/fullscreenmodeoptionkey/fullscreenmodeapplicationpresentationoptions.md) options is specified when [`enterFullScreenMode(_:withOptions:)`](nsview/enterfullscreenmode(_:withoptions:).md) is invoked, exiting full screen mode will restore the previously active [`presentationOptions`](nsapplication/presentationoptions-swift.property.md).

## Parameters

- `options`: A dictionary of options for the mode. For possible keys, see  .

## See Also

- [func enterFullScreenMode(NSScreen, withOptions: [NSView.FullScreenModeOptionKey : Any]?) -> Bool](nsview/enterfullscreenmode(_:withoptions:).md)
  Sets the view to full screen mode.
- [var isInFullScreenMode: Bool](nsview/isinfullscreenmode.md)
  A Boolean value indicating whether the view is in full screen mode.
- [NSView.FullScreenModeOptionKey](nsview/fullscreenmodeoptionkey.md)
  These constants are keys that you can use in the options dictionary in [`enterFullScreenMode(_:withOptions:)`](nsview/enterfullscreenmode(_:withoptions:).md) and [`exitFullScreenMode(options:)`](nsview/exitfullscreenmode(options:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/exitfullscreenmode(options:))*