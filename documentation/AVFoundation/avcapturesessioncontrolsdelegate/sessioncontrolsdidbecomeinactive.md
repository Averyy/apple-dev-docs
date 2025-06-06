# sessionControlsDidBecomeInactive(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Required**: Yes

Tells the delegate when a capture session’s controls become inactive and unavailable for interaction.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
func sessionControlsDidBecomeInactive(_ session: AVCaptureSession)
```

## Parameters

- `session`: The capture session with inactive controls.

## See Also

- [func sessionControlsDidBecomeActive(AVCaptureSession)](avcapturesessioncontrolsdelegate/sessioncontrolsdidbecomeactive(_:).md)
  Tells the delegate when a capture session’s controls become active and available for interaction.
- [func sessionControlsWillEnterFullscreenAppearance(AVCaptureSession)](avcapturesessioncontrolsdelegate/sessioncontrolswillenterfullscreenappearance(_:).md)
  Tells the delegate when a capture session’s controls are about to enter a fullscreen appearance.
- [func sessionControlsWillExitFullscreenAppearance(AVCaptureSession)](avcapturesessioncontrolsdelegate/sessioncontrolswillexitfullscreenappearance(_:).md)
  Tells the delegate when a capture session’s controls are about to exit a fullscreen appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesessioncontrolsdelegate/sessioncontrolsdidbecomeinactive(_:))*