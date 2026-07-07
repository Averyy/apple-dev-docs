# isBuffering

**Framework**: AVKit  
**Kind**: property  
**Required**: Yes

Indicates whether the media source is currently stalled waiting for data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
var isBuffering: Bool { get }
```

#### Discussion

Returns `true` when the source cannot immediately sustain continuous playback. This may occur both before [`isReady`](avplaybackuserinterfaceplaybackcontrollable-9he54/isready.md) becomes `true` during initial loading, and after [`isReady`](avplaybackuserinterfaceplaybackcontrollable-9he54/isready.md) is `true` during mid-playback stalls. When `true`, [`isPlaying`](avplaybackuserinterfaceplaybackcontrollable-9he54/isplaying.md) may still be `true`, indicating that playback should resume automatically once sufficient data is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-9he54/isbuffering)*