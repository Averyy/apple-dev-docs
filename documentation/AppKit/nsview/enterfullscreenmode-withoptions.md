# enterFullScreenMode(_:withOptions:)

**Framework**: AppKit  
**Kind**: method

Sets the view to full screen mode.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func enterFullScreenMode(_ screen: NSScreen, withOptions options: [NSView.FullScreenModeOptionKey : Any]? = nil) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the view was able to enter full screen mode, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

When the [`fullScreenModeApplicationPresentationOptions`](nsview/fullscreenmodeoptionkey/fullscreenmodeapplicationpresentationoptions.md) is contained in the options dictionary, the presentation options that were in effect when this method is invoked are not altered, and no displays are captured.

If you do not wish to capture the screen when going to full screen mode, you can add [`fullScreenModeApplicationPresentationOptions`](nsview/fullscreenmodeoptionkey/fullscreenmodeapplicationpresentationoptions.md) to the options dictionary with the value returned by the [`presentationOptions`](nsapplication/presentationoptions-swift.property.md).

When the [`fullScreenModeApplicationPresentationOptions`](nsview/fullscreenmodeoptionkey/fullscreenmodeapplicationpresentationoptions.md) options is specified, exiting full screen mode using [`exitFullScreenMode(options:)`](nsview/exitfullscreenmode(options:).md) will restore the previously active [`presentationOptions`](nsapplication/presentationoptions-swift.property.md).

##### Special Considerations

In OS X v 10.5, invoking this method when the view was not in a window would cause an exception. In macOS 10.6 and later, you can now send this message to a view not in a window. For applications that must also run in OS X v 10.5, a simple workaround is to place the view in an offscreen window.

## Parameters

- `screen`: The screen the view should cover.
- `options`: A dictionary of options for the mode. For possible keys, see  .

## See Also

- [func exitFullScreenMode(options: [NSView.FullScreenModeOptionKey : Any]?)](nsview/exitfullscreenmode(options:).md)
  Instructs the view to exit full screen mode.
- [var isInFullScreenMode: Bool](nsview/isinfullscreenmode.md)
  A Boolean value indicating whether the view is in full screen mode.
- [NSView.FullScreenModeOptionKey](nsview/fullscreenmodeoptionkey.md)
  These constants are keys that you can use in the options dictionary in [`enterFullScreenMode(_:withOptions:)`](nsview/enterfullscreenmode(_:withoptions:).md) and [`exitFullScreenMode(options:)`](nsview/exitfullscreenmode(options:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/enterfullscreenmode(_:withoptions:))*