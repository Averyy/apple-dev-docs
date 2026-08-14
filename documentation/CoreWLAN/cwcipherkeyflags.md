# CWCipherKeyFlags

**Framework**: Core WLAN  
**Kind**: struct

Cipher key flags.

**Availability**:
- macOS 10.7+

## Declaration

```swift
struct CWCipherKeyFlags
```

#### Overview

Use these flags with [`setWEPKey(_:flags:index:)`](cwinterface/setwepkey(_:flags:index:).md).

## Topics

### Constants
- [static var unicast: CWCipherKeyFlags](cwcipherkeyflags/unicast.md)
  A flag that indicates to use the cipher key for unicast packets.
- [static var multicast: CWCipherKeyFlags](cwcipherkeyflags/multicast.md)
  A flag that indicates to use the cipher key for multicast packets.
- [static var tx: CWCipherKeyFlags](cwcipherkeyflags/tx.md)
  A flag that indicates to use the cipher key for packets sent from the interface.
- [static var rx: CWCipherKeyFlags](cwcipherkeyflags/rx.md)
  A flag that indicates to use the cipher key for packets received by the interface.
### Initializers
- [init(rawValue: UInt)](cwcipherkeyflags/init(rawvalue:).md)
  Creates a cipher key flags structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwcipherkeyflags)*