# unicast

**Framework**: Core WLAN  
**Kind**: property  
**Role**: Type Property

A flag that indicates to use the cipher key for unicast packets.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static var unicast: CWCipherKeyFlags { get }
```

```c
kCWCipherKeyFlagsUnicast
```

## See Also

### Constants
- [static var multicast: CWCipherKeyFlags](./multicast.md)
  A flag that indicates to use the cipher key for multicast packets.
- [static var tx: CWCipherKeyFlags](./tx.md)
  A flag that indicates to use the cipher key for packets sent from the interface.
- [static var rx: CWCipherKeyFlags](./rx.md)
  A flag that indicates to use the cipher key for packets received by the interface.
- [kCWCipherKeyFlagsNone](./kcwcipherkeyflagsnone.md)
  Open System authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwcipherkeyflags/unicast)*