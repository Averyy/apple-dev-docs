# tailTime

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

The audio unit’s tail time, in seconds.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var tailTime: TimeInterval { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly) NSTimeInterval tailTime;
```

*macOS*

```objc
@property (atomic, readonly) NSTimeInterval tailTime;
```

## Discussion

This property reflects the time interval between when the input stream ends or otherwise transitions to silence, and when the output stream becomes silent. This should also reflect the duration of an effect (e.g. reverberation).

This version 3 property is bridged to the version 2 `kAudioUnitProperty_TailTime` API.

## See Also

### Optimizing Performance
- [var latency: TimeInterval](./latency.md)
  The audio unit’s processing latency, in seconds.
- [var renderQuality: Int](./renderquality.md)
  Provides a trade-off between rendering quality and CPU load.
- [var shouldBypassEffect: Bool](./shouldbypasseffect.md)
  Determines whether an effect should route input directly to output, without any processing.
- [var canProcessInPlace: Bool](./canprocessinplace.md)
  Determines whether an audio unit can process in place.
- [var isRenderingOffline: Bool](./isrenderingoffline.md)
  Communicates to an audio unit that it is rendering offline.
- [osWorkgroup](./osworkgroup.md)
  The workgroup associated with the audio device underlying this Audio Unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/tailtime)*