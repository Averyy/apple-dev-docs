# canMute

**Framework**: Media Device  
**Kind**: property

Indicates whether the device supports muting audio output.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
let canMute: Bool
```

#### Discussion

When `true`, the device supports mute/unmute functionality, allowing users to temporarily silence audio without changing the volume level. When `false`, mute controls should not be presented in the user interface for this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediaoutputdevice/canmute)*