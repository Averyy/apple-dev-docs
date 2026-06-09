# latency

**Framework**: AVFAudio  
**Kind**: property

The processing latency of the node, in seconds.

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
var latency: TimeInterval { get }
```

#### Discussion

This latency reflects the delay due to signal processing. A value of `0` indicates either no latency or an unknown latency.

## See Also

- [func withAUAudioUnit<R, E>((borrowing AUAudioUnit) throws(E) -> R) throws(E) -> R](avaudionode/withauaudiounit(_:).md)
  Provides scoped access to the node’s AUAudioUnit
- [var auAudioUnit: AUAudioUnit](avaudionode/auaudiounit-1gu8g.md)
  An audio unit object that wraps or underlies the implementation’s audio unit.
- [var outputPresentationLatency: TimeInterval](avaudionode/outputpresentationlatency.md)
  The maximum render pipeline latency downstream of the node, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/latency)*