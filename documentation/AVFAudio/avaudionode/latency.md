# latency

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSTimeInterval latency;
```

#### Discussion

This latency reflects the delay due to signal processing. A value of `0` indicates either no latency or an unknown latency.

## See Also

### Getting audio node properties
- [func withAUAudioUnit<R, E>((borrowing AUAudioUnit) throws(E) -> R) throws(E) -> R](./withauaudiounit%28_%29.md)
  Provides scoped access to the node’s AUAudioUnit
- [var auAudioUnit: AUAudioUnit](./auaudiounit-1gu8g.md)
  An audio unit object that wraps or underlies the implementation’s audio unit.
- [var outputPresentationLatency: TimeInterval](./outputpresentationlatency.md)
  The maximum render pipeline latency downstream of the node, in seconds.
- [AUAudioUnit](./auaudiounit-1kkjr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/latency)*