# AudioCodecPrimeInfo

**Framework**: Audio Toolbox  
**Kind**: struct

A structure specifying the number of leading and trailing empty frames to be inserted.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioCodecPrimeInfo
```

## Topics

### Initializers
- [init()](audiocodecprimeinfo/init.md)
- [init(leadingFrames: UInt32, trailingFrames: UInt32)](audiocodecprimeinfo/init(leadingframes:trailingframes:).md)
### Instance Properties
- [var leadingFrames: UInt32](audiocodecprimeinfo/leadingframes.md)
  An unsigned integer specifying the number of leading empty frames.
- [var trailingFrames: UInt32](audiocodecprimeinfo/trailingframes.md)
  An unsigned integer specifying the number of trailing empty frames.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct AudioCodecMagicCookieInfo](audiocodecmagiccookieinfo.md)
  A structure holding magic cookie information needed by some codecs.
- [typealias AudioCodec](audiocodec.md)
  An instance of a Component Manager component.
- [typealias AudioCodecAppendInputBufferListProc](audiocodecappendinputbufferlistproc.md)
- [typealias AudioCodecAppendInputDataProc](audiocodecappendinputdataproc.md)
- [typealias AudioCodecGetPropertyInfoProc](audiocodecgetpropertyinfoproc.md)
- [typealias AudioCodecGetPropertyProc](audiocodecgetpropertyproc.md)
- [typealias AudioCodecInitializeProc](audiocodecinitializeproc.md)
- [typealias AudioCodecProduceOutputBufferListProc](audiocodecproduceoutputbufferlistproc.md)
- [typealias AudioCodecProduceOutputPacketsProc](audiocodecproduceoutputpacketsproc.md)
- [typealias AudioCodecPropertyID](audiocodecpropertyid.md)
  An integer identifying an audio codec property.
- [typealias AudioCodecResetProc](audiocodecresetproc.md)
- [typealias AudioCodecSetPropertyProc](audiocodecsetpropertyproc.md)
- [typealias AudioCodecUninitializeProc](audiocodecuninitializeproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocodecprimeinfo)*