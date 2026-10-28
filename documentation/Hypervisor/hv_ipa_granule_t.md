# hv_ipa_granule_t

**Framework**: Hypervisor  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 26.0+

## Declaration

```swift
struct hv_ipa_granule_t
```

```c
typedef enum { ... } hv_ipa_granule_t;
```

## Overview

Supported intermediate physical address (IPA) granules.

## Topics

### Initializers
- [init(UInt32)](./hv_ipa_granule_t/init%28_%29.md)
- [init(rawValue: UInt32)](./hv_ipa_granule_t/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./hv_ipa_granule_t/rawvalue.md)
### Enumeration Cases
- [HV_IPA_GRANULE_16KB](./hv_ipa_granule_16kb.md)
- [HV_IPA_GRANULE_4KB](./hv_ipa_granule_4kb.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hypervisor/hv_ipa_granule_t)*