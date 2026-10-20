# AudioCodecMagicCookieInfo

**Framework**: Audio Toolbox  
**Kind**: struct  
**Role**: Structure

A structure holding magic cookie information needed by some codecs.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct AudioCodecMagicCookieInfo
```

```c
struct AudioCodecMagicCookieInfo;
```

#### Overview

This structure is passed as input to the [`AudioCodecGetProperty(_:_:_:_:)`](./audiocodecgetproperty%28_,_,_,_%29.md) function for the `kAudioCodecPropertyFormatList` property. The first `4 + sizeof(void *)` bytes of the buffer pointed to by the function’s `outPropertyData` parameter contains this structure on input.

## Topics

### Initializers
- [init()](./audiocodecmagiccookieinfo/init%28%29.md)
- [init(mMagicCookieSize: UInt32, mMagicCookie: UnsafeRawPointer?)](./audiocodecmagiccookieinfo/init%28mmagiccookiesize,mmagiccookie%29.md)
### Instance Properties
- [var mMagicCookie: UnsafeRawPointer?](./audiocodecmagiccookieinfo/mmagiccookie.md)
  Generic constant pointer to the magic cookie.
- [var mMagicCookieSize: UInt32](./audiocodecmagiccookieinfo/mmagiccookiesize.md)
  The size of the magic cookie.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Codec Types
- [struct AudioCodecPrimeInfo](./audiocodecprimeinfo.md)
  A structure specifying the number of leading and trailing empty frames to be inserted.
- [typealias AudioCodec](./audiocodec.md)
  An instance of a Component Manager component.
- [typealias AudioCodecAppendInputBufferListProc](./audiocodecappendinputbufferlistproc.md)
- [typealias AudioCodecAppendInputDataProc](./audiocodecappendinputdataproc.md)
- [typealias AudioCodecGetPropertyInfoProc](./audiocodecgetpropertyinfoproc.md)
- [typealias AudioCodecGetPropertyProc](./audiocodecgetpropertyproc.md)
- [typealias AudioCodecInitializeProc](./audiocodecinitializeproc.md)
- [typealias AudioCodecProduceOutputBufferListProc](./audiocodecproduceoutputbufferlistproc.md)
- [typealias AudioCodecProduceOutputPacketsProc](./audiocodecproduceoutputpacketsproc.md)
- [typealias AudioCodecPropertyID](./audiocodecpropertyid.md)
  An integer identifying an audio codec property.
- [typealias AudioCodecResetProc](./audiocodecresetproc.md)
- [typealias AudioCodecSetPropertyProc](./audiocodecsetpropertyproc.md)
- [typealias AudioCodecUninitializeProc](./audiocodecuninitializeproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocodecmagiccookieinfo)*