# withAUAudioUnit(_:)

**Framework**: AVFAudio  
**Kind**: method

Provides scoped access to the node’s AUAudioUnit

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func withAUAudioUnit<R, E>(_ body: (borrowing AUAudioUnit) throws(E) -> R) throws(E) -> R where E : Error
```

#### Return Value

The value returned by the closure

#### Discussion

This method provides thread-safe, scoped access to the underlying AUAudioUnit. The audio unit reference is only valid within the closure and must not be retained or accessed outside of it.

> **Note**: Rethrows any error thrown by the closure

## Parameters

- `body`: A closure that receives the AUAudioUnit instance

## See Also

- [var auAudioUnit: AUAudioUnit](avaudionode/auaudiounit-1gu8g.md)
  An audio unit object that wraps or underlies the implementation’s audio unit.
- [var latency: TimeInterval](avaudionode/latency.md)
  The processing latency of the node, in seconds.
- [var outputPresentationLatency: TimeInterval](avaudionode/outputpresentationlatency.md)
  The maximum render pipeline latency downstream of the node, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode/withauaudiounit(_:))*