# exitFullScreenMode(options:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Instructs the view to exit full screen mode.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func exitFullScreenMode(options: [NSView.FullScreenModeOptionKey : Any]? = nil)
```

```objc
- (void) exitFullScreenModeWithOptions:(NSDictionary<NSString *,id> *) options;
```

## Discussion

When the [`fullScreenModeApplicationPresentationOptions`](./fullscreenmodeoptionkey/fullscreenmodeapplicationpresentationoptions.md) options is specified when [`enterFullScreenMode(_:withOptions:)`](./enterfullscreenmode%28_,withoptions%29.md) is invoked, exiting full screen mode will restore the previously active [`presentationOptions`](../nsapplication/presentationoptions-swift.property.md).

## Parameters

- `options`: A dictionary of options for the mode. For possible keys, see `Full Screen Mode Options`.

## See Also

### Drawing the View in Fullscreen Mode
- [func enterFullScreenMode(NSScreen, withOptions: [NSView.FullScreenModeOptionKey : Any]?) -> Bool](./enterfullscreenmode%28_,withoptions%29.md)
  Sets the view to full screen mode.
- [var isInFullScreenMode: Bool](./isinfullscreenmode.md)
  A Boolean value indicating whether the view is in full screen mode.
- [NSView.FullScreenModeOptionKey](./fullscreenmodeoptionkey.md)
  These constants are keys that you can use in the options dictionary in [`enterFullScreenMode(_:withOptions:)`](./enterfullscreenmode%28_,withoptions%29.md) and [`exitFullScreenMode(options:)`](./exitfullscreenmode%28options%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/exitfullscreenmode(options:))*