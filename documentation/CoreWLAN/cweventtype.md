# CWEventType

**Framework**: Core WLAN  
**Kind**: enum

Wi-Fi event types.

**Availability**:
- macOS 10.10+

## Declaration

```swift
enum CWEventType
```

## Topics

### Constants
- [CWEventType.none](cweventtype/none.md)
  No specified event type.
- [CWEventType.powerDidChange](cweventtype/powerdidchange.md)
  Posts when the power state of any Wi-Fi interface changes.
- [CWEventType.ssidDidChange](cweventtype/ssiddidchange.md)
  Posts when the current SSID of any Wi-Fi interface changes.
- [CWEventType.bssidDidChange](cweventtype/bssiddidchange.md)
  Posts when the current BSSID of any Wi-Fi interface changes.
- [CWEventType.countryCodeDidChange](cweventtype/countrycodedidchange.md)
  Posts when the adopted country code of any Wi-Fi interface changes.
- [CWEventType.linkDidChange](cweventtype/linkdidchange.md)
  Posts when the link state for any Wi-Fi interface changes.
- [CWEventType.linkQualityDidChange](cweventtype/linkqualitydidchange.md)
  Posts when the RSSI or transmit rate for any Wi-Fi interface changes.
- [CWEventType.modeDidChange](cweventtype/modedidchange.md)
  Posts when the operating mode of any Wi-Fi interface changes.
- [CWEventType.scanCacheUpdated](cweventtype/scancacheupdated.md)
  Posts when the scan cache of any Wi-Fi interface is updated with new scan results.
- [CWEventType.unknown](cweventtype/unknown.md)
  Unknown event type.
### Enumeration Cases
- [CWEventType.btCoexStats](cweventtype/btcoexstats.md)
### Initializers
- [init?(rawValue: Int)](cweventtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum CWChannelBand](cwchannelband.md)
  CoreWLAN channel bands.
- [enum CWChannelWidth](cwchannelwidth.md)
  CoreWLAN channel widths.
- [struct CWCipherKeyFlags](cwcipherkeyflags.md)
  Cipher key flags.
- [enum CWErr](cwerr.md)
- [enum CWIBSSModeSecurity](cwibssmodesecurity.md)
  IBSS mode security types.
- [enum CWInterfaceMode](cwinterfacemode.md)
  Wi-Fi interface operating modes.
- [enum CWKeychainDomain](cwkeychaindomain.md)
  Keychain domain types that CoreWLAN keychain methods use.
- [enum CWPHYMode](cwphymode.md)
  CoreWLAN physical layer modes.
- [enum CWSecurity](cwsecurity.md)
  CoreWLAN security types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cweventtype)*