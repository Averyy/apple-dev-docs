# CWIBSSModeSecurity

**Framework**: Core WLAN  
**Kind**: enum  
**Role**: Enumeration

IBSS mode security types.

**Availability**:
- macOS 10.7+ - Deprecated in 11.0

## Declaration

```swift
enum CWIBSSModeSecurity
```

```c
enum CWIBSSModeSecurity : NSInteger;
```

## Topics

### Constants
- [CWIBSSModeSecurity.none](./cwibssmodesecurity/none.md)
  Open System authentication.
- [CWIBSSModeSecurity.WEP40](./cwibssmodesecurity/wep40.md)
  WEP security.
- [CWIBSSModeSecurity.WEP104](./cwibssmodesecurity/wep104.md)
  WPA Personal authentication.
### Initializers
- [init?(rawValue: Int)](./cwibssmodesecurity/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Enumerations
- [enum CWChannelBand](./cwchannelband.md)
  CoreWLAN channel bands.
- [enum CWChannelWidth](./cwchannelwidth.md)
  CoreWLAN channel widths.
- [struct CWCipherKeyFlags](./cwcipherkeyflags.md)
  Cipher key flags.
- [enum CWErr](./cwerr.md)
- [enum CWEventType](./cweventtype.md)
  Wi-Fi event types.
- [enum CWInterfaceMode](./cwinterfacemode.md)
  Wi-Fi interface operating modes.
- [enum CWKeychainDomain](./cwkeychaindomain.md)
  Keychain domain types that CoreWLAN keychain methods use.
- [enum CWPHYMode](./cwphymode.md)
  CoreWLAN physical layer modes.
- [enum CWSecurity](./cwsecurity.md)
  CoreWLAN security types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwibssmodesecurity)*