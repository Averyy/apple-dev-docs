# Converter Priming Constants

**Framework**: Audio Toolbox

Constants used with the [`kAudioConverterPrimeMethod`](kaudioconverterprimemethod.md) property.

## Topics

### Constants
- [var kConverterPrimeMethod_Pre: UInt32](kconverterprimemethod_pre.md)
  Prime with `leading` + `trailing` input frames.
- [var kConverterPrimeMethod_Normal: UInt32](kconverterprimemethod_normal.md)
  Prime with `trailing` frames only, for zero latency. Leading frames are assumed to be silence.
- [var kConverterPrimeMethod_None: UInt32](kconverterprimemethod_none.md)
  Acts in “latency” mode. Leading and trailing frames are both assumed to be silence.

## See Also

- [Audio Converter Properties](1559928-audio-converter-properties.md)
  Audio converter properties, used with the [`AudioConverterGetPropertyInfo(_:_:_:_:)`](audioconvertergetpropertyinfo(_:_:_:_:).md), [`AudioConverterGetProperty(_:_:_:_:)`](audioconvertergetproperty(_:_:_:_:).md), and [`AudioConverterSetProperty(_:_:_:_:)`](audioconvertersetproperty(_:_:_:_:).md) functions.
- [Sample Rate Conversion Quality Identifiers](1559924-sample-rate-conversion-quality-i.md)
  Specifiers for sample rate conversion quality, used for the [`kAudioConverterSampleRateConverterQuality`](kaudioconvertersamplerateconverterquality.md) property.
- [Sample Rate Conversion Complexity Identifiers](1559923-sample-rate-conversion-complexit.md)
  Specifiers for the sample rate conversion algorithm, used for the [`kAudioConverterSampleRateConverterComplexity`](kaudioconvertersamplerateconvertercomplexity.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1559927-converter-priming-constants)*