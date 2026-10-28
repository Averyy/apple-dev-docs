# CIDataMatrixCodeDescriptor.ECCVersion

**Framework**: Core Image  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the Data Matrix code ECC version.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum ECCVersion
```

```c
enum CIDataMatrixCodeECCVersion : NSInteger;
```

## Overview

ECC 000 - 140 symbols offer five levels of error correction using convolutional code error correction. Each successive level or error correction offers more protection for the message data but increases the size of the symbol required to carry a given message. See the ISO/IEC 16022:2006 spec for other modes.

ECC 200 symbols utilize Reed-Solomon error correction. The error correction capacity for any given Data Matrix symbol is fixed by the size (in rows and columns) of the symbol. See Table 7 of ISO/IEC 16022:2006(E) for more details.

## Topics

### Enumeration Cases
- [CIDataMatrixCodeDescriptor.ECCVersion.v000](./eccversion-swift.enum/v000.md)
  Indicates error correction using convolutional code error correction with no data protection.
- [CIDataMatrixCodeDescriptor.ECCVersion.v050](./eccversion-swift.enum/v050.md)
  Indicates 1/4 of the symbol is dedicated to convolutional code error correction.
- [CIDataMatrixCodeDescriptor.ECCVersion.v080](./eccversion-swift.enum/v080.md)
  Indicates 1/3 of the symbol is dedicated to convolutional code error correction.
- [CIDataMatrixCodeDescriptor.ECCVersion.v100](./eccversion-swift.enum/v100.md)
  Indicates 1/2 of the symbol is dedicated to convolutional code error correction.
- [CIDataMatrixCodeDescriptor.ECCVersion.v140](./eccversion-swift.enum/v140.md)
  Indicates 3/4 of the symbol is dedicated to convolutional code error correction.
- [CIDataMatrixCodeDescriptor.ECCVersion.v200](./eccversion-swift.enum/v200.md)
  Indicates error correction using Reed-Solomon error correction. Data protection overhead varies based on symbol size.
### Initializers
- [init?(rawValue: Int)](./eccversion-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor/eccversion-swift.enum)*