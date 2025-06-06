# kAudioConverterApplicableEncodeSampleRates

**Framework**: Audio Toolbox  
**Kind**: var

An array of `AudioValueRange` structures that describes applicable sample rates based on current settings.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioConverterApplicableEncodeSampleRates: AudioConverterPropertyID { get }
```

## See Also

- [var kAudioConverterPropertyMinimumInputBufferSize: AudioConverterPropertyID](kaudioconverterpropertyminimuminputbuffersize.md)
  A `UInt32` value that indicates the size, in bytes, of the smallest buffer of input data that can be supplied via the audio converter input callback or as the input to the [`AudioConverterConvertBuffer(_:_:_:_:_:)`](audioconverterconvertbuffer(_:_:_:_:_:).md) function.
- [var kAudioConverterPropertyMinimumOutputBufferSize: AudioConverterPropertyID](kaudioconverterpropertyminimumoutputbuffersize.md)
  A `UInt32` value that indicates the size, in bytes, of the smallest buffer of output data that can be supplied to AudioConverterFillComplexBuffer or as the output to AudioConverterConvertBuffer
- [var kAudioConverterPropertyMaximumInputBufferSize: AudioConverterPropertyID](kaudioconverterpropertymaximuminputbuffersize.md)
  Deprecated. The audio converter input callback may be passed any number of packets of data. If fewer are packets are returned than required, then the input proc is called again. If more packets are passed than required, they remain in the client’s buffer and are consumed as needed.
- [var kAudioConverterPropertyMaximumInputPacketSize: AudioConverterPropertyID](kaudioconverterpropertymaximuminputpacketsize.md)
  A `UInt32` value that indicates the size, in bytes, of the largest single packet of data in the input format. This is mostly useful for variable bit rate compressed data (decoders).
- [var kAudioConverterPropertyMaximumOutputPacketSize: AudioConverterPropertyID](kaudioconverterpropertymaximumoutputpacketsize.md)
  A `UInt32` value that indicates the size, in bytes, of the largest single packet of data in the output format. This is mostly useful for variable bit rate compressed data (encoders).
- [var kAudioConverterPropertyCalculateInputBufferSize: AudioConverterPropertyID](kaudioconverterpropertycalculateinputbuffersize.md)
  A `UInt32` value that on input holds a size, in bytes, that is desired for the output data. On output, it holds the size, in bytes, of the input buffer required to generate that much output data. Note that some converters cannot do this calculation.
- [var kAudioConverterPropertyCalculateOutputBufferSize: AudioConverterPropertyID](kaudioconverterpropertycalculateoutputbuffersize.md)
  A `UInt32` value that on input holds a size, in bytes, that is desired for the input data. On output, it holds the size, in bytes, of the output buffer required to hold the output data to be generated. Some converters cannot do this calculation.
- [var kAudioConverterPropertyInputCodecParameters: AudioConverterPropertyID](kaudioconverterpropertyinputcodecparameters.md)
  The value of this property varies from format to format and is considered private to the format. It is treated as a buffer of untyped data.
- [var kAudioConverterPropertyOutputCodecParameters: AudioConverterPropertyID](kaudioconverterpropertyoutputcodecparameters.md)
  The value of this property varies from format to format and is considered private to the format. It is treated as a buffer of untyped data.
- [var kAudioConverterSampleRateConverterAlgorithm: AudioConverterPropertyID](kaudioconvertersamplerateconverteralgorithm.md)
  A value that indicates the sample rate conversion algorithm.
- [var kAudioConverterSampleRateConverterComplexity: AudioConverterPropertyID](kaudioconvertersamplerateconvertercomplexity.md)
  The sample rate conversion algorithm.
- [var kAudioConverterSampleRateConverterQuality: AudioConverterPropertyID](kaudioconvertersamplerateconverterquality.md)
  The rendering quality of the sample rate converter.
- [var kAudioConverterSampleRateConverterInitialPhase: AudioConverterPropertyID](kaudioconvertersamplerateconverterinitialphase.md)
  A `Float64` value equal to `0.0`.
- [var kAudioConverterCodecQuality: AudioConverterPropertyID](kaudioconvertercodecquality.md)
  The rendering quality of a codec. A `UInt32` value.
- [var kAudioConverterPrimeMethod: AudioConverterPropertyID](kaudioconverterprimemethod.md)
  The priming method, usually for sample-rate conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudioconverterapplicableencodesamplerates)*