# AVAudioConverterPrimeMethod.none

**Framework**: AVFAudio  
**Kind**: case  
**Role**: Case

An option to prime the converter assumes leading and trailing frames are silence.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case none
```

```c
AVAudioConverterPrimeMethod_None
```

## See Also

### Choosing a priming method
- [AVAudioConverterPrimeMethod.pre](./pre.md)
  An option to prime with leading and trailing input frames.
- [AVAudioConverterPrimeMethod.normal](./normal.md)
  An option to prime with trailing (zero latency) frames where the converter assumes the leading frames are silence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverterprimemethod/none)*