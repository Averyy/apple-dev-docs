# Audio Converter Properties

**Framework**: Audio Toolbox

Audio converter properties, used with the [`AudioConverterGetPropertyInfo(_:_:_:_:)`](audioconvertergetpropertyinfo(_:_:_:_:).md), [`AudioConverterGetProperty(_:_:_:_:)`](audioconvertergetproperty(_:_:_:_:).md), and [`AudioConverterSetProperty(_:_:_:_:)`](audioconvertersetproperty(_:_:_:_:).md) functions.

## Topics

### Constants
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
- [var kAudioConverterPrimeInfo: AudioConverterPropertyID](kaudioconverterprimeinfo.md)
  An [`AudioConverterPrimeInfo`](audioconverterprimeinfo.md) structure.
- [var kAudioConverterChannelMap: AudioConverterPropertyID](kaudioconverterchannelmap.md)
  An array of `SInt32` values that specify an input-to-output channel mapping.
- [var kAudioConverterDecompressionMagicCookie: AudioConverterPropertyID](kaudioconverterdecompressionmagiccookie.md)
  A `void*` value that points to memory set up by the caller. This property is required by some audio data formats in order to decompress the input data.
- [var kAudioConverterCompressionMagicCookie: AudioConverterPropertyID](kaudioconvertercompressionmagiccookie.md)
  A `void*` value that points to memory set up by the caller. This property is returned by the converter so that your application may store it along with the output data. This property can then be passed back to the converter for decompression at a later time.
- [var kAudioConverterEncodeBitRate: AudioConverterPropertyID](kaudioconverterencodebitrate.md)
  A `UInt32` value containing the number of bits per second to aim for when encoding data. Some decoders also allow you to query this property to discover the bit rate.
- [var kAudioConverterEncodeAdjustableSampleRate: AudioConverterPropertyID](kaudioconverterencodeadjustablesamplerate.md)
  A `Float64` value that specifies an output sample rate.
- [var kAudioConverterInputChannelLayout: AudioConverterPropertyID](kaudioconverterinputchannellayout.md)
  An `AudioChannelLayout` structure that specifies an audio converter’s input channel layout.
- [var kAudioConverterOutputChannelLayout: AudioConverterPropertyID](kaudioconverteroutputchannellayout.md)
  An `AudioChannelLayout` structure that specifies an audio converter’s output channel layout.
- [var kAudioConverterApplicableEncodeBitRates: AudioConverterPropertyID](kaudioconverterapplicableencodebitrates.md)
  An array of `AudioValueRange` structures that describes applicable bit rates based on current settings.
- [var kAudioConverterAvailableEncodeBitRates: AudioConverterPropertyID](kaudioconverteravailableencodebitrates.md)
  An array of `AudioValueRange` structures that describes the available bit rates based on the input format. You can determine the available bit rates using Audio Format Services.
- [var kAudioConverterApplicableEncodeSampleRates: AudioConverterPropertyID](kaudioconverterapplicableencodesamplerates.md)
  An array of `AudioValueRange` structures that describes applicable sample rates based on current settings.
- [var kAudioConverterAvailableEncodeSampleRates: AudioConverterPropertyID](kaudioconverteravailableencodesamplerates.md)
  An array of `AudioValueRange` structures that describes the available sample rates based on the input format. You can determine the available sample rates using Audio Format Services.
- [var kAudioConverterAvailableEncodeChannelLayoutTags: AudioConverterPropertyID](kaudioconverteravailableencodechannellayouttags.md)
  An array of `AudioChannelLayoutTag` values for the format and number of channels specified in the encoder’s input format.
- [var kAudioConverterCurrentOutputStreamDescription: AudioConverterPropertyID](kaudioconvertercurrentoutputstreamdescription.md)
  The current, completely specified output `AudioStreamBasicDescription` structure.
- [var kAudioConverterCurrentInputStreamDescription: AudioConverterPropertyID](kaudioconvertercurrentinputstreamdescription.md)
  The current, completely specified input `AudioStreamBasicDescription` structure.
- [var kAudioConverterPropertySettings: AudioConverterPropertyID](kaudioconverterpropertysettings.md)
  An array (of type `CFArray`) of property settings for converters.
- [var kAudioConverterPropertyBitDepthHint: AudioConverterPropertyID](kaudioconverterpropertybitdepthhint.md)
  A `UInt32` value that designates the source bit depth to preserve.
- [var kAudioConverterPropertyFormatList: AudioConverterPropertyID](kaudioconverterpropertyformatlist.md)
  An array of `AudioFormatListItem` structures that describes the set of data formats produced by the encoder end of an audio converter.
- [var kAudioConverterPropertyCanResumeFromInterruption: AudioConverterPropertyID](kaudioconverterpropertycanresumefrominterruption.md)
  Indicates whether the underlying codec supports resumption of processing following an audio interruption. A read-only `UInt32` value.

## See Also

- [Converter Priming Constants](1559927-converter-priming-constants.md)
  Constants used with the [`kAudioConverterPrimeMethod`](kaudioconverterprimemethod.md) property.
- [Sample Rate Conversion Quality Identifiers](1559924-sample-rate-conversion-quality-i.md)
  Specifiers for sample rate conversion quality, used for the [`kAudioConverterSampleRateConverterQuality`](kaudioconvertersamplerateconverterquality.md) property.
- [Sample Rate Conversion Complexity Identifiers](1559923-sample-rate-conversion-complexit.md)
  Specifiers for the sample rate conversion algorithm, used for the [`kAudioConverterSampleRateConverterComplexity`](kaudioconvertersamplerateconvertercomplexity.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1559928-audio-converter-properties)*