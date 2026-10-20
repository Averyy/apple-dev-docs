# shouldBypassEffect

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic) BOOL shouldBypassEffect;
```

*macOS*

```objc
@property (atomic) BOOL shouldBypassEffect;
```

#### Discussion

This version 3 property is bridged to the version 2 `kAudioUnitProperty_BypassEffect` API.

## See Also

### Optimizing Performance
- [var latency: TimeInterval](./latency.md)
  The audio unit’s processing latency, in seconds.
- [var tailTime: TimeInterval](./tailtime.md)
  The audio unit’s tail time, in seconds.
- [var renderQuality: Int](./renderquality.md)
  Provides a trade-off between rendering quality and CPU load.
- [var canProcessInPlace: Bool](./canprocessinplace.md)
  Determines whether an audio unit can process in place.
- [var isRenderingOffline: Bool](./isrenderingoffline.md)
  Communicates to an audio unit that it is rendering offline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/shouldbypasseffect)*