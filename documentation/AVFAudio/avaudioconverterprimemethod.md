# AVAudioConverterPrimeMethod

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Options for the prime method property.

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
enum AVAudioConverterPrimeMethod
```

```c
enum AVAudioConverterPrimeMethod : NSInteger;
```

## Overview

For more information, see [`AVAudioConverterPrimeInfo`](./avaudioconverterprimeinfo.md).

## Topics

### Creating a priming method
- [init?(rawValue: Int)](./avaudioconverterprimemethod/init%28rawvalue%29.md)
### Choosing a priming method
- [AVAudioConverterPrimeMethod.pre](./avaudioconverterprimemethod/pre.md)
  An option to prime with leading and trailing input frames.
- [AVAudioConverterPrimeMethod.normal](./avaudioconverterprimemethod/normal.md)
  An option to prime with trailing (zero latency) frames where the converter assumes the leading frames are silence.
- [AVAudioConverterPrimeMethod.none](./avaudioconverterprimemethod/none.md)
  An option to prime the converter assumes leading and trailing frames are silence.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting priming information
- [var primeInfo: AVAudioConverterPrimeInfo](./avaudioconverter/primeinfo.md)
  The number of priming frames the converter uses.
- [var primeMethod: AVAudioConverterPrimeMethod](./avaudioconverter/primemethod.md)
  The priming method the sample rate converter or decoder uses.
- [struct AVAudioConverterPrimeInfo](./avaudioconverterprimeinfo.md)
  Priming information for audio conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioconverterprimemethod)*