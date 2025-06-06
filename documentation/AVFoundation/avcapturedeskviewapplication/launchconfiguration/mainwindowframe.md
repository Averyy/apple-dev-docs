# mainWindowFrame

**Framework**: AVFoundation  
**Kind**: property

The frame for Desk View after it launches.

**Availability**:
- Mac Catalyst 16.1+
- macOS 13.0+

## Declaration

```swift
var mainWindowFrame: CGRect { get set }
```

#### Discussion

The default value is [`zero`](https://developer.apple.com/documentation/CoreFoundation/CGRect/zero), which tells the system to use the previously set frame. The system uses global screen coordinates to display the frame. When Desk View launches from a native macOS app, the window origin is bottom-left. When it launches from a [`Mac Catalyst`](https://developer.apple.com/documentation/UIKit/mac-catalyst) app, the window origin is top-left.

## See Also

- [var requiresSetUpModeCompletion: Bool](avcapturedeskviewapplication/launchconfiguration/requiressetupmodecompletion.md)
  A Boolean value that specifies whether the system requires the user to complete setup mode before it executes the completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeskviewapplication/launchconfiguration/mainwindowframe)*