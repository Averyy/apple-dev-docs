# Sample Rate Conversion Complexity Identifiers

**Framework**: Audio Toolbox

Specifiers for the sample rate conversion algorithm, used for the [`kAudioConverterSampleRateConverterComplexity`](kaudioconvertersamplerateconvertercomplexity.md) property.

## Topics

### Constants
- [var kAudioConverterSampleRateConverterComplexity_Linear: UInt32](kaudioconvertersamplerateconvertercomplexity_linear.md)
  Specifies linear interpolation for sample rate conversion. This provides the lowest quality and is, computationally, the least expensive option.
- [var kAudioConverterSampleRateConverterComplexity_Normal: UInt32](kaudioconvertersamplerateconvertercomplexity_normal.md)
  Specifies the normal-complexity sample rate conversion algorithm. This is the default value.
- [var kAudioConverterSampleRateConverterComplexity_Mastering: UInt32](kaudioconvertersamplerateconvertercomplexity_mastering.md)
  Specifies a mastering-quality sample rate conversion algorithm. This provides the highest quality and is, computationally, the most expensive option.
- [var kAudioConverterSampleRateConverterComplexity_MinimumPhase: UInt32](kaudioconvertersamplerateconvertercomplexity_minimumphase.md)

## See Also

- [Audio Converter Properties](1559928-audio-converter-properties.md)
  Audio converter properties, used with the [`AudioConverterGetPropertyInfo(_:_:_:_:)`](audioconvertergetpropertyinfo(_:_:_:_:).md), [`AudioConverterGetProperty(_:_:_:_:)`](audioconvertergetproperty(_:_:_:_:).md), and [`AudioConverterSetProperty(_:_:_:_:)`](audioconvertersetproperty(_:_:_:_:).md) functions.
- [Converter Priming Constants](1559927-converter-priming-constants.md)
  Constants used with the [`kAudioConverterPrimeMethod`](kaudioconverterprimemethod.md) property.
- [Sample Rate Conversion Quality Identifiers](1559924-sample-rate-conversion-quality-i.md)
  Specifiers for sample rate conversion quality, used for the [`kAudioConverterSampleRateConverterQuality`](kaudioconvertersamplerateconverterquality.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1559923-sample-rate-conversion-complexit)*