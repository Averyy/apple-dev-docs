# AudioCodecGetPropertyProc

**Framework**: Audio Toolbox  
**Kind**: typealias

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AudioCodecGetPropertyProc = (UnsafeMutableRawPointer, AudioCodecPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus
```

## See Also

- [struct AudioCodecMagicCookieInfo](audiocodecmagiccookieinfo.md)
  A structure holding magic cookie information needed by some codecs.
- [struct AudioCodecPrimeInfo](audiocodecprimeinfo.md)
  A structure specifying the number of leading and trailing empty frames to be inserted.
- [typealias AudioCodec](audiocodec.md)
  An instance of a Component Manager component.
- [typealias AudioCodecAppendInputBufferListProc](audiocodecappendinputbufferlistproc.md)
- [typealias AudioCodecAppendInputDataProc](audiocodecappendinputdataproc.md)
- [typealias AudioCodecGetPropertyInfoProc](audiocodecgetpropertyinfoproc.md)
- [typealias AudioCodecInitializeProc](audiocodecinitializeproc.md)
- [typealias AudioCodecProduceOutputBufferListProc](audiocodecproduceoutputbufferlistproc.md)
- [typealias AudioCodecProduceOutputPacketsProc](audiocodecproduceoutputpacketsproc.md)
- [typealias AudioCodecPropertyID](audiocodecpropertyid.md)
  An integer identifying an audio codec property.
- [typealias AudioCodecResetProc](audiocodecresetproc.md)
- [typealias AudioCodecSetPropertyProc](audiocodecsetpropertyproc.md)
- [typealias AudioCodecUninitializeProc](audiocodecuninitializeproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocodecgetpropertyproc)*