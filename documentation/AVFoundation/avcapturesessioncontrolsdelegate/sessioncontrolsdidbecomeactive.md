# sessionControlsDidBecomeActive(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Required**: Yes

Tells the delegate when a capture session’s controls become active and available for interaction.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
func sessionControlsDidBecomeActive(_ session: AVCaptureSession)
```

## Parameters

- `session`: The capture session with active controls.

## See Also

- [func sessionControlsWillEnterFullscreenAppearance(AVCaptureSession)](avcapturesessioncontrolsdelegate/sessioncontrolswillenterfullscreenappearance(_:).md)
  Tells the delegate when a capture session’s controls are about to enter a fullscreen appearance.
- [func sessionControlsWillExitFullscreenAppearance(AVCaptureSession)](avcapturesessioncontrolsdelegate/sessioncontrolswillexitfullscreenappearance(_:).md)
  Tells the delegate when a capture session’s controls are about to exit a fullscreen appearance.
- [func sessionControlsDidBecomeInactive(AVCaptureSession)](avcapturesessioncontrolsdelegate/sessioncontrolsdidbecomeinactive(_:).md)
  Tells the delegate when a capture session’s controls become inactive and unavailable for interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesessioncontrolsdelegate/sessioncontrolsdidbecomeactive(_:))*