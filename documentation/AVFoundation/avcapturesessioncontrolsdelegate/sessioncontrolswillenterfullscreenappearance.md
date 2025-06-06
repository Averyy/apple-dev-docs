# sessionControlsWillEnterFullscreenAppearance(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Required**: Yes

Tells the delegate when a capture session’s controls are about to enter a fullscreen appearance.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
func sessionControlsWillEnterFullscreenAppearance(_ session: AVCaptureSession)
```

#### Discussion

When controls enter a fullscreen appearance, your app should hide portions of its user interface, including duplicative or unnecessary elements. Few onscreen elements should be visible so people can focus on their control interactions while viewing the camera preview unobstructed.

## Parameters

- `session`: The capture session with controls that are entering a fullscreen appearance.

## See Also

- [func sessionControlsDidBecomeActive(AVCaptureSession)](avcapturesessioncontrolsdelegate/sessioncontrolsdidbecomeactive(_:).md)
  Tells the delegate when a capture session’s controls become active and available for interaction.
- [func sessionControlsWillExitFullscreenAppearance(AVCaptureSession)](avcapturesessioncontrolsdelegate/sessioncontrolswillexitfullscreenappearance(_:).md)
  Tells the delegate when a capture session’s controls are about to exit a fullscreen appearance.
- [func sessionControlsDidBecomeInactive(AVCaptureSession)](avcapturesessioncontrolsdelegate/sessioncontrolsdidbecomeinactive(_:).md)
  Tells the delegate when a capture session’s controls become inactive and unavailable for interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesessioncontrolsdelegate/sessioncontrolswillenterfullscreenappearance(_:))*