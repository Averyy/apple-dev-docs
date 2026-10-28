# CWCipherKeyFlags

**Framework**: Core WLAN  
**Kind**: struct  
**Role**: Structure

Cipher key flags.

**Availability**:
- macOS 10.7+

## Declaration

```swift
struct CWCipherKeyFlags
```

```c
enum CWCipherKeyFlags : NSUInteger;
```

## Overview

Use these flags with [`setWEPKey(_:flags:index:)`](./cwinterface/setwepkey%28_,flags,index%29.md).

## Topics

### Constants
- [static var unicast: CWCipherKeyFlags](./cwcipherkeyflags/unicast.md)
  A flag that indicates to use the cipher key for unicast packets.
- [static var multicast: CWCipherKeyFlags](./cwcipherkeyflags/multicast.md)
  A flag that indicates to use the cipher key for multicast packets.
- [static var tx: CWCipherKeyFlags](./cwcipherkeyflags/tx.md)
  A flag that indicates to use the cipher key for packets sent from the interface.
- [static var rx: CWCipherKeyFlags](./cwcipherkeyflags/rx.md)
  A flag that indicates to use the cipher key for packets received by the interface.
- [kCWCipherKeyFlagsNone](./cwcipherkeyflags/kcwcipherkeyflagsnone.md)
  Open System authentication.
### Initializers
- [init(rawValue: UInt)](./cwcipherkeyflags/init%28rawvalue%29.md)
  Creates a cipher key flags structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwcipherkeyflags)*