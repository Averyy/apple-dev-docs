# isBuffering

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Indicates whether the media source is currently stalled waiting for data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
@MainActor
var isBuffering: Bool { get }
```

## Discussion

Returns `true` when the source cannot immediately sustain continuous playback. This may occur both before [`isReady`](./isready.md) becomes `true` during initial loading, and after [`isReady`](./isready.md) is `true` during mid-playback stalls. When `true`, [`isPlaying`](./isplaying.md) may still be `true`, indicating that playback should resume automatically once sufficient data is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-9he54/isbuffering)*