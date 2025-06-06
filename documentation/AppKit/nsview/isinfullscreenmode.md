# isInFullScreenMode

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the view is in full screen mode.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var isInFullScreenMode: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the view is in full screen mode or [`false`](https://developer.apple.com/documentation/swift/false) when it is not.

## See Also

- [func enterFullScreenMode(NSScreen, withOptions: [NSView.FullScreenModeOptionKey : Any]?) -> Bool](nsview/enterfullscreenmode(_:withoptions:).md)
  Sets the view to full screen mode.
- [func exitFullScreenMode(options: [NSView.FullScreenModeOptionKey : Any]?)](nsview/exitfullscreenmode(options:).md)
  Instructs the view to exit full screen mode.
- [NSView.FullScreenModeOptionKey](nsview/fullscreenmodeoptionkey.md)
  These constants are keys that you can use in the options dictionary in [`enterFullScreenMode(_:withOptions:)`](nsview/enterfullscreenmode(_:withoptions:).md) and [`exitFullScreenMode(options:)`](nsview/exitfullscreenmode(options:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/isinfullscreenmode)*