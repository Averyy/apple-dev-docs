# isReady

**Framework**: AVKit  
**Kind**: property  
**Required**: Yes

Indicates whether the media source is ready to begin playback.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
var isReady: Bool { get }
```

#### Discussion

This property should transition from `false` to `true` once the source has loaded enough data to start playback, and should not revert. Use [`isBuffering`](avplaybackuserinterfaceplaybackcontrollable-9he54/isbuffering.md) to track temporary stalls that may occur after this point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-9he54/isready)*