# shouldBypassEffect

**Framework**: Audio Toolbox  
**Kind**: property

Determines whether an effect should route input directly to output, without any processing.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var shouldBypassEffect: Bool { get set }
```

#### Discussion

This version 3 property is bridged to the version 2 `kAudioUnitProperty_BypassEffect` API.

## See Also

- [var latency: TimeInterval](auaudiounit/latency.md)
  The audio unit’s processing latency, in seconds.
- [var tailTime: TimeInterval](auaudiounit/tailtime.md)
  The audio unit’s tail time, in seconds.
- [var renderQuality: Int](auaudiounit/renderquality.md)
  Provides a trade-off between rendering quality and CPU load.
- [var canProcessInPlace: Bool](auaudiounit/canprocessinplace.md)
  Determines whether an audio unit can process in place.
- [var isRenderingOffline: Bool](auaudiounit/isrenderingoffline.md)
  Communicates to an audio unit that it is rendering offline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/shouldbypasseffect)*