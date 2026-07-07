# isDisabled

**Framework**: Audio Toolbox  
**Kind**: property

Indicates whether the host is bypassing the renderer due to poor performance.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
var isDisabled: Bool { get }
```

#### Discussion

The host may set this property when the Audio Unit exhibits problematic behavior such as excessive CPU usage that impacts real-time performance or non-compliance with API requirements.

When YES, the host bypasses the spatial Audio Unit in the audio signal chain and the Audio Unit does not render audio. When NO, the Audio Unit receives input and must render audio when it is matched a Bluetooth headphone device.

The Audio Unit should monitor this property to detect when the host disables the Audio Unit.

This property supports Key-Value Observing (KVO).


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auheadtrackingbinauralrenderer/isdisabled)*