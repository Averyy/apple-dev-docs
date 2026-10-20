# AudioCodecInitializeProc

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias AudioCodecInitializeProc = (UnsafeMutableRawPointer, UnsafePointer<AudioStreamBasicDescription>?, UnsafePointer<AudioStreamBasicDescription>?, UnsafeRawPointer?, UInt32) -> OSStatus
```

```c
typedef int (*)(void *, const struct AudioStreamBasicDescription *, const struct AudioStreamBasicDescription *, const void *, unsigned int) AudioCodecInitializeProc;
```

## See Also

### Codec Types
- [struct AudioCodecMagicCookieInfo](./audiocodecmagiccookieinfo.md)
  A structure holding magic cookie information needed by some codecs.
- [struct AudioCodecPrimeInfo](./audiocodecprimeinfo.md)
  A structure specifying the number of leading and trailing empty frames to be inserted.
- [typealias AudioCodec](./audiocodec.md)
  An instance of a Component Manager component.
- [typealias AudioCodecAppendInputBufferListProc](./audiocodecappendinputbufferlistproc.md)
- [typealias AudioCodecAppendInputDataProc](./audiocodecappendinputdataproc.md)
- [typealias AudioCodecGetPropertyInfoProc](./audiocodecgetpropertyinfoproc.md)
- [typealias AudioCodecGetPropertyProc](./audiocodecgetpropertyproc.md)
- [typealias AudioCodecProduceOutputBufferListProc](./audiocodecproduceoutputbufferlistproc.md)
- [typealias AudioCodecProduceOutputPacketsProc](./audiocodecproduceoutputpacketsproc.md)
- [typealias AudioCodecPropertyID](./audiocodecpropertyid.md)
  An integer identifying an audio codec property.
- [typealias AudioCodecResetProc](./audiocodecresetproc.md)
- [typealias AudioCodecSetPropertyProc](./audiocodecsetpropertyproc.md)
- [typealias AudioCodecUninitializeProc](./audiocodecuninitializeproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocodecinitializeproc)*