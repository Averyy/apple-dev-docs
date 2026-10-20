# rx

**Framework**: Core WLAN  
**Kind**: property  
**Role**: Type Property

A flag that indicates to use the cipher key for packets received by the interface.

**Availability**:
- macOS 10.7+

## Declaration

```swift
static var rx: CWCipherKeyFlags { get }
```

```c
kCWCipherKeyFlagsRx
```

## See Also

### Constants
- [static var unicast: CWCipherKeyFlags](./unicast.md)
  A flag that indicates to use the cipher key for unicast packets.
- [static var multicast: CWCipherKeyFlags](./multicast.md)
  A flag that indicates to use the cipher key for multicast packets.
- [static var tx: CWCipherKeyFlags](./tx.md)
  A flag that indicates to use the cipher key for packets sent from the interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwcipherkeyflags/rx)*