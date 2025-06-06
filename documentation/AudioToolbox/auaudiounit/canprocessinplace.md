# canProcessInPlace

**Framework**: Audio Toolbox  
**Kind**: property

Determines whether an audio unit can process in place.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var canProcessInPlace: Bool { get }
```

#### Discussion

In-place processing is the ability for an audio unit to transform an input signal to an output signal in-place in the input buffer, without requiring a separate output buffer.

A host can express its desire to process in place by using null `mData` pointers in the output buffer list. If so, the audio unit may process in-place in the input buffers.

This version 3 property is partially bridged to the version 2 `kAudioUnitProperty_InPlaceProcessing` API. It is not settable in version 3.

## See Also

- [var renderBlock: AURenderBlock](auaudiounit/renderblock.md)
  The block that hosts use to ask the audio unit to render audio.
- [var latency: TimeInterval](auaudiounit/latency.md)
  The audio unit’s processing latency, in seconds.
- [var tailTime: TimeInterval](auaudiounit/tailtime.md)
  The audio unit’s tail time, in seconds.
- [var renderQuality: Int](auaudiounit/renderquality.md)
  Provides a trade-off between rendering quality and CPU load.
- [var shouldBypassEffect: Bool](auaudiounit/shouldbypasseffect.md)
  Determines whether an effect should route input directly to output, without any processing.
- [var isRenderingOffline: Bool](auaudiounit/isrenderingoffline.md)
  Communicates to an audio unit that it is rendering offline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/canprocessinplace)*