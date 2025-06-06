# sessionControlsWillExitFullscreenAppearance(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Required**: Yes

Tells the delegate when a capture session’s controls are about to exit a fullscreen appearance.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
func sessionControlsWillExitFullscreenAppearance(_ session: AVCaptureSession)
```

#### Discussion

When your app receives this callback, it should resume showing portions of the interface it hid when controls entered a fullscreen appearance.

The system calls this method before [`sessionControlsDidBecomeInactive(_:)`](avcapturesessioncontrolsdelegate/sessioncontrolsdidbecomeinactive(_:).md).

## Parameters

- `session`: The capture session with controls that are exiting a fullscreen appearance.

## See Also

- [func sessionControlsDidBecomeActive(AVCaptureSession)](avcapturesessioncontrolsdelegate/sessioncontrolsdidbecomeactive(_:).md)
  Tells the delegate when a capture session’s controls become active and available for interaction.
- [func sessionControlsWillEnterFullscreenAppearance(AVCaptureSession)](avcapturesessioncontrolsdelegate/sessioncontrolswillenterfullscreenappearance(_:).md)
  Tells the delegate when a capture session’s controls are about to enter a fullscreen appearance.
- [func sessionControlsDidBecomeInactive(AVCaptureSession)](avcapturesessioncontrolsdelegate/sessioncontrolsdidbecomeinactive(_:).md)
  Tells the delegate when a capture session’s controls become inactive and unavailable for interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesessioncontrolsdelegate/sessioncontrolswillexitfullscreenappearance(_:))*