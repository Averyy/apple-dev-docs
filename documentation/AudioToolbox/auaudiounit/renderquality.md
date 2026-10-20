# renderQuality

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

Provides a trade-off between rendering quality and CPU load.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var renderQuality: Int { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic) NSInteger renderQuality;
```

*macOS*

```objc
@property (atomic) NSInteger renderQuality;
```

#### Discussion

The range of valid values is 0 to 127.

This version 3 property is bridged to the version 2 `kAudioUnitProperty_RenderQuality` API.

## See Also

### Optimizing Performance
- [var latency: TimeInterval](./latency.md)
  The audio unit’s processing latency, in seconds.
- [var tailTime: TimeInterval](./tailtime.md)
  The audio unit’s tail time, in seconds.
- [var shouldBypassEffect: Bool](./shouldbypasseffect.md)
  Determines whether an effect should route input directly to output, without any processing.
- [var canProcessInPlace: Bool](./canprocessinplace.md)
  Determines whether an audio unit can process in place.
- [var isRenderingOffline: Bool](./isrenderingoffline.md)
  Communicates to an audio unit that it is rendering offline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/renderquality)*