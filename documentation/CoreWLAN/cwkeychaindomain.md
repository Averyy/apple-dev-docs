# CWKeychainDomain

**Framework**: Core WLAN  
**Kind**: enum  
**Role**: Enumeration

Keychain domain types that CoreWLAN keychain methods use.

**Availability**:
- macOS 10.10+

## Declaration

```swift
enum CWKeychainDomain
```

```c
enum CWKeychainDomain : NSInteger;
```

## Topics

### Constants
- [CWKeychainDomain.none](./cwkeychaindomain/none.md)
  No keychain domain specified.
- [CWKeychainDomain.user](./cwkeychaindomain/user.md)
  The user keychain domain.
- [CWKeychainDomain.system](./cwkeychaindomain/system.md)
  The system keychain domain.
### Initializers
- [init?(rawValue: Int)](./cwkeychaindomain/init%28rawvalue%29.md)

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
- [enum CWIBSSModeSecurity](./cwibssmodesecurity.md)
  IBSS mode security types.
- [enum CWInterfaceMode](./cwinterfacemode.md)
  Wi-Fi interface operating modes.
- [enum CWPHYMode](./cwphymode.md)
  CoreWLAN physical layer modes.
- [enum CWSecurity](./cwsecurity.md)
  CoreWLAN security types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwkeychaindomain)*