# isPlaying

**Framework**: AVKit  
**Kind**: property  
**Required**: Yes

Indicates whether playback is active.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
var isPlaying: Bool { get set }
```

#### Discussion

Setting this to `true` should start playback; setting it to `false` should pause it. This property reflects playback intent — it should remain `true` while [`isBuffering`](avplaybackuserinterfaceplaybackcontrollable-9he54/isbuffering.md) is `true`, indicating that playback should resume automatically once sufficient data is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-9he54/isplaying)*