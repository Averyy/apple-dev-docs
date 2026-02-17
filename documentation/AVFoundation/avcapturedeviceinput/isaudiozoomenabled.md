# isAudioZoomEnabled

**Framework**: AVFoundation  
**Kind**: property

Whether or not audio zoom is enabled.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- tvOS 26.4+ (Beta)

## Declaration

```swift
var isAudioZoomEnabled: Bool { get set }
```

#### Discussion

Setting this property to `true` throws an exception if [`isAudioZoomSupported`](avcapturedeviceinput/isaudiozoomsupported.md) is `false`. Default is `true` when supported. When enabled, the sound field narrows or expands to match the field of view of the video device’s zoom factor. Set this property to `false` if you want to capture the full sound field regardless of video zoom. This property only takes effect when added to a session with a video device, and [`AVCaptureMultichannelAudioMode`](avcapturemultichannelaudiomode.md) is set to any value other than `AVCaptureMultichannelAudioModeNone`. When using multiple cameras in [`AVCaptureMultiCamSession`](avcapturemulticamsession.md), audio zoom is determined by the zoom factor of the preferred camera. The preferred camera is selected to match the mic position, either front or back. If more than one camera is available in that position, the camera with the widest field of view is chosen with virtual cameras preferred over single camera ones. If no camera is found to match the mic position, audio zoom is unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/isaudiozoomenabled)*