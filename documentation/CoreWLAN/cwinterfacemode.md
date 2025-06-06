# CWInterfaceMode

**Framework**: Core WLAN  
**Kind**: enum

Wi-Fi interface operating modes.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum CWInterfaceMode
```

## Topics

### Constants
- [CWInterfaceMode.none](cwinterfacemode/none.md)
  Interface is not in any mode.
- [CWInterfaceMode.station](cwinterfacemode/station.md)
  Interface is participating in an infrastructure network as a non-AP station.
- [CWInterfaceMode.IBSS](cwinterfacemode/ibss.md)
  Interface is participating in an IBSS network.
- [CWInterfaceMode.hostAP](cwinterfacemode/hostap.md)
  Interface is participating in an infrastructure network as an access point.
### Initializers
- [init?(rawValue: Int)](cwinterfacemode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum CWChannelBand](cwchannelband.md)
  CoreWLAN channel bands.
- [enum CWChannelWidth](cwchannelwidth.md)
  CoreWLAN channel widths.
- [struct CWCipherKeyFlags](cwcipherkeyflags.md)
  Cipher key flags.
- [enum CWErr](cwerr.md)
- [enum CWEventType](cweventtype.md)
  Wi-Fi event types.
- [enum CWIBSSModeSecurity](cwibssmodesecurity.md)
  IBSS mode security types.
- [enum CWKeychainDomain](cwkeychaindomain.md)
  Keychain domain types that CoreWLAN keychain methods use.
- [enum CWPHYMode](cwphymode.md)
  CoreWLAN physical layer modes.
- [enum CWSecurity](cwsecurity.md)
  CoreWLAN security types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwinterfacemode)*