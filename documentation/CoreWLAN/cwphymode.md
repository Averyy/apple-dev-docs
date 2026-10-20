# CWPHYMode

**Framework**: Core WLAN  
**Kind**: enum  
**Role**: Enumeration

CoreWLAN physical layer modes.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum CWPHYMode
```

```c
enum CWPHYMode : NSInteger;
```

## Topics

### Constants
- [CWPHYMode.modeNone](./cwphymode/modenone.md)
  No specified mode.
- [CWPHYMode.mode11a](./cwphymode/mode11a.md)
  IEEE 802.11a PHY.
- [CWPHYMode.mode11b](./cwphymode/mode11b.md)
  IEEE 802.11b PHY.
- [CWPHYMode.mode11g](./cwphymode/mode11g.md)
  IEEE 802.11g PHY.
- [CWPHYMode.mode11n](./cwphymode/mode11n.md)
  IEEE 802.11n PHY.
- [CWPHYMode.mode11ac](./cwphymode/mode11ac.md)
  IEEE 802.11ac PHY.
### Enumeration Cases
- [CWPHYMode.mode11ax](./cwphymode/mode11ax.md)
- [CWPHYMode.mode11be](./cwphymode/mode11be.md)
### Initializers
- [init?(rawValue: Int)](./cwphymode/init%28rawvalue%29.md)

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
- [enum CWSecurity](./cwsecurity.md)
  CoreWLAN security types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwphymode)*