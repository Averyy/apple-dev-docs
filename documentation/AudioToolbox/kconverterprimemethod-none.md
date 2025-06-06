# kConverterPrimeMethod_None

**Framework**: Audio Toolbox  
**Kind**: var

Acts in “latency” mode. Leading and trailing frames are both assumed to be silence.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kConverterPrimeMethod_None: UInt32 { get }
```

## See Also

- [var kConverterPrimeMethod_Pre: UInt32](kconverterprimemethod_pre.md)
  Prime with `leading` + `trailing` input frames.
- [var kConverterPrimeMethod_Normal: UInt32](kconverterprimemethod_normal.md)
  Prime with `trailing` frames only, for zero latency. Leading frames are assumed to be silence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kconverterprimemethod_none)*