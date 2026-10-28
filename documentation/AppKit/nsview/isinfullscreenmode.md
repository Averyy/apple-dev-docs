# isInFullScreenMode

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view is in full screen mode.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var isInFullScreenMode: Bool { get }
```

```objc
@property (readonly, getter=isInFullScreenMode) BOOL inFullScreenMode;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the view is in full screen mode or [`false`](../../Swift/false.md) when it is not.

## See Also

### Drawing the View in Fullscreen Mode
- [func enterFullScreenMode(NSScreen, withOptions: [NSView.FullScreenModeOptionKey : Any]?) -> Bool](./enterfullscreenmode%28_,withoptions%29.md)
  Sets the view to full screen mode.
- [func exitFullScreenMode(options: [NSView.FullScreenModeOptionKey : Any]?)](./exitfullscreenmode%28options%29.md)
  Instructs the view to exit full screen mode.
- [NSView.FullScreenModeOptionKey](./fullscreenmodeoptionkey.md)
  These constants are keys that you can use in the options dictionary in [`enterFullScreenMode(_:withOptions:)`](./enterfullscreenmode%28_,withoptions%29.md) and [`exitFullScreenMode(options:)`](./exitfullscreenmode%28options%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/isinfullscreenmode)*