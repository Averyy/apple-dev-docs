# AudioConverterPrimeInfo

**Framework**: Audio Toolbox  
**Kind**: struct

Specifies priming information for an audio converter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioConverterPrimeInfo
```

#### Overview

Some audio data format conversions, particularly those involving sample-rate conversion, yield higher quality output when leading or trailing frames are available to the converter. The appropriate number of these so-called  depends on the input audio data format.

You specify leading or trailing frames in the `leadingFrames` and `trailingFrames` fields of an `AudioConverterPrimeInfo` structure. You then configure your audio converter by calling the [`AudioConverterSetProperty(_:_:_:_:)`](audioconvertersetproperty(_:_:_:_:).md) function for the [`kAudioConverterPrimeInfo`](kaudioconverterprimeinfo.md) property, specifying this structure as the property value. You also indicate to the converter which priming option to use by setting the [`kAudioConverterPrimeMethod`](kaudioconverterprimemethod.md) property.

When you configure an audio converter by specifying leading or trailing frames, you alter the behavior of the [`AudioConverterFillComplexBuffer(_:_:_:_:_:_:)`](audioconverterfillcomplexbuffer(_:_:_:_:_:_:).md) function. The very first call to that function, or the first call after calling [`AudioConverterReset(_:)`](audioconverterreset(_:).md), results in a request for additional input frames when the converter object invokes your [`AudioConverterComplexInputDataProc`](audioconvertercomplexinputdataproc.md) callback. The number of priming frames requested depends on the priming option you specify, as shown in below.

| Priming option | Number of priming frames (approximate) |
| --- | --- |
| `kConverterPrimeMethod_Pre` | `leadingFrames` + `trailingFrames` |
| `kConverterPrimeMethod_Normal` | `trailingFrames` |
| `kConverterPrimeMethod_None` | `0` |

The default priming option is that specified by the `kConverterPrimeMethod_Normal` constant. This option requires no preseeking of the input stream. It generates `trailingFrames` of latency at output.

The `kConverterPrimeMethod_Pre` priming option results in a first invocation of your callback that asks for approximately `leadingFrames` + `trailingFrames` priming frames. Latency at output will correspond, approximately, to this duration.

The `kConverterPrimeMethod_None` priming constant is especially useful in real-time applications that process live input. This option minimizes output latency, but is appropriate only for formats that do not require priming frames.

In a digital audio workstation, the `kConverterPrimeMethod_Pre` option may be preferable for real-time applications. This is because your application may be able to provide priming frames by preloading them from disk or memory, avoiding latency while still supporting audio formats that require priming.

## Topics

### Initializers
- [init()](audioconverterprimeinfo/init.md)
- [init(leadingFrames: UInt32, trailingFrames: UInt32)](audioconverterprimeinfo/init(leadingframes:trailingframes:).md)
### Instance Properties
- [var leadingFrames: UInt32](audioconverterprimeinfo/leadingframes.md)
  The number of leading frames of input audio data required for the converter to perform high-quality conversion.
- [var trailingFrames: UInt32](audioconverterprimeinfo/trailingframes.md)
  The number of trailing frames of input audio data required by the converter to perform high-quality conversion. Trailing frames follow, in time, the expected final input frame. Your application should be prepared to provide this number of additional input frames except when using the `kConverterPrimeMethod_None` value for the `kAudioConverterPrimeMethod` property. If no additional frames are available in the input stream (because, for example, the desired end frame is at the end of an audio file), then the audio converter synthesizes a sufficient number of silent (`0`-valued) trailing frames.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias AudioConverterRef](audioconverterref.md)
  A reference to an audio converter object.
- [typealias AudioConverterPropertyID](audioconverterpropertyid.md)
  An audio converter property identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconverterprimeinfo)*