# AVAudioEngineManualRenderingMode.realtime

**Framework**: AVFAudio  
**Kind**: case

An engine that operates under real-time constraints and doesn’t make blocking calls while rendering.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
case realtime
```

#### Discussion

You can only use the block-based render mechanism in this mode. See [`manualRenderingBlock`](avaudioengine/manualrenderingblock.md).

## See Also

- [AVAudioEngineManualRenderingMode.offline](avaudioenginemanualrenderingmode/offline.md)
  An engine that operates in an offline mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioenginemanualrenderingmode/realtime)*