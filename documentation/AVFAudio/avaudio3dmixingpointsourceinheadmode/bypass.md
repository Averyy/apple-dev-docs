# AVAudio3DMixingPointSourceInHeadMode.bypass

**Framework**: AVFAudio  
**Kind**: case

The point source distributes into each output channel inside the head of the listener.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
case bypass
```

#### Discussion

This option enables transitions between traditional, nonspatialized rendering and spatialized sources outside of the listener’s head.

## See Also

- [AVAudio3DMixingPointSourceInHeadMode.mono](avaudio3dmixingpointsourceinheadmode/mono.md)
  The point source remains a single mono source inside the head of the listener regardless of the channels it consists of.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudio3dmixingpointsourceinheadmode/bypass)*