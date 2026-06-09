# outputPresentationLatency

**Framework**: AVFAudio  
**Kind**: property

The maximum render pipeline latency downstream of the node, in seconds.

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
var outputPresentationLatency: TimeInterval { get }
```

#### Discussion

This latency describes the maximum time it takes to present the audio at the output of a node.

## See Also

- [func withAUAudioUnit<R, E>((borrowing AUAudioUnit) throws(E) -> R) throws(E) -> R](avaudionode/withauaudiounit(_:).md)
  Provides scoped access to the node’s AUAudioUnit
- [var auAudioUnit: AUAudioUnit](avaudionode/auaudiounit-1gu8g.md)
  An audio unit object that wraps or underlies the implementation’s audio unit.
- [var latency: TimeInterval](avaudionode/latency.md)
  The processing latency of the node, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/outputpresentationlatency)*