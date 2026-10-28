# mainWindowFrame

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The frame for Desk View after it launches.

**Availability**:
- Mac Catalyst 16.1+
- macOS 13.0+

## Declaration

```swift
var mainWindowFrame: CGRect { get set }
```

```objc
@property CGRect mainWindowFrame;
```

## Discussion

The default value is [`zero`](../../../CoreFoundation/cgrect/zero.md), which tells the system to use the previously set frame. The system uses global screen coordinates to display the frame. When Desk View launches from a native macOS app, the window origin is bottom-left. When it launches from a [Mac Catalyst](../../../UIKit/mac-catalyst.md) app, the window origin is top-left.

## See Also

### Customizing the presentation
- [var requiresSetUpModeCompletion: Bool](./requiressetupmodecompletion.md)
  A Boolean value that specifies whether the system requires the user to complete setup mode before it executes the completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeskviewapplication/launchconfiguration/mainwindowframe)*