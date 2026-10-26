# outputPresentationLatency

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSTimeInterval outputPresentationLatency;
```

#### Discussion

This latency describes the maximum time it takes to present the audio at the output of a node.

## See Also

### Getting audio node properties
- [func withAUAudioUnit<R, E>((borrowing AUAudioUnit) throws(E) -> R) throws(E) -> R](./withauaudiounit%28_%29.md)
  Provides scoped access to the node’s AUAudioUnit
- [var auAudioUnit: AUAudioUnit](./auaudiounit-1gu8g.md)
  An audio unit object that wraps or underlies the implementation’s audio unit.
- [var latency: TimeInterval](./latency.md)
  The processing latency of the node, in seconds.
- [AUAudioUnit](./auaudiounit-1kkjr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/outputpresentationlatency)*