# sessionControlsDidBecomeActive(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) sessionControlsDidBecomeActive:(AVCaptureSession *) session;
```

## Parameters

- `session`: The capture session with active controls.

## See Also

### Responding to control events
- [func sessionControlsWillEnterFullscreenAppearance(AVCaptureSession)](./sessioncontrolswillenterfullscreenappearance%28_%29.md)
  Tells the delegate when a capture session’s controls are about to enter a fullscreen appearance.
- [func sessionControlsWillExitFullscreenAppearance(AVCaptureSession)](./sessioncontrolswillexitfullscreenappearance%28_%29.md)
  Tells the delegate when a capture session’s controls are about to exit a fullscreen appearance.
- [func sessionControlsDidBecomeInactive(AVCaptureSession)](./sessioncontrolsdidbecomeinactive%28_%29.md)
  Tells the delegate when a capture session’s controls become inactive and unavailable for interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesessioncontrolsdelegate/sessioncontrolsdidbecomeactive(_:))*