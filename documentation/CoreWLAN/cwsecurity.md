# CWSecurity

**Framework**: Core WLAN  
**Kind**: enum  
**Role**: Enumeration

CoreWLAN security types.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum CWSecurity
```

```c
enum CWSecurity : NSInteger;
```

## Topics

### Constants
- [CWSecurity.none](./cwsecurity/none.md)
  Open System authentication.
- [CWSecurity.WEP](./cwsecurity/wep.md)
  WEP security.
- [CWSecurity.wpaPersonal](./cwsecurity/wpapersonal.md)
  WPA Personal authentication.
- [CWSecurity.wpaPersonalMixed](./cwsecurity/wpapersonalmixed.md)
  WPA/WPA2 Personal authentication.
- [CWSecurity.wpa2Personal](./cwsecurity/wpa2personal.md)
  WPA2 Personal authentication.
- [CWSecurity.personal](./cwsecurity/personal.md)
  Personal authentication.
- [CWSecurity.dynamicWEP](./cwsecurity/dynamicwep.md)
  Dynamic WEP security.
- [CWSecurity.wpaEnterprise](./cwsecurity/wpaenterprise.md)
  WPA Enterprise authentication.
- [CWSecurity.wpaEnterpriseMixed](./cwsecurity/wpaenterprisemixed.md)
  WPA/WPA2 Enterprise authentication.
- [CWSecurity.wpa2Enterprise](./cwsecurity/wpa2enterprise.md)
  WPA2 Enterprise authentication.
- [CWSecurity.enterprise](./cwsecurity/enterprise.md)
  Enterprise authentication.
- [CWSecurity.wpa3Personal](./cwsecurity/wpa3personal.md)
  WPA3 Personal authentication.
- [CWSecurity.wpa3Enterprise](./cwsecurity/wpa3enterprise.md)
  WPA3 Enterprise authentication.
- [CWSecurity.wpa3Transition](./cwsecurity/wpa3transition.md)
  WPA3 Transition (WPA3/WPA2 Personal) authentication.
- [CWSecurity.unknown](./cwsecurity/unknown.md)
  Unknown security type.
### Enumeration Cases
- [CWSecurity.OWE](./cwsecurity/owe.md)
- [CWSecurity.oweTransition](./cwsecurity/owetransition.md)
### Initializers
- [init?(rawValue: Int)](./cwsecurity/init%28rawvalue%29.md)

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
- [enum CWKeychainDomain](./cwkeychaindomain.md)
  Keychain domain types that CoreWLAN keychain methods use.
- [enum CWPHYMode](./cwphymode.md)
  CoreWLAN physical layer modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwsecurity)*