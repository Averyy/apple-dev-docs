# CWLinkQualityNotificationRSSIKey

**Framework**: Core WLAN  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- macOS 10.6+ - Deprecated in 10.10

> **Deprecated**: Use -[CWWiFiClient startMonitoringEventWithType:error:] with the CWEventTypeLinkQualityDidChange event type

## Declaration

```swift
let CWLinkQualityNotificationRSSIKey: String
```

```c
extern NSString * const CWLinkQualityNotificationRSSIKey;
```

## Discussion

NSNumber containing the current RSSI value for the WLAN interface. Found in the *userInfo* dictionary for the *CWLinkQualityChangedNotification*.

## See Also

### Constants
- [let CWErrorDomain: String](./cwerrordomain.md)
- [let CWLinkQualityNotificationTransmitRateKey: String](./cwlinkqualitynotificationtransmitratekey.md)
- [CWBSSIDDidChangeNotification](./cwbssiddidchangenotification.md)
- [CWCountryCodeDidChangeNotification](./cwcountrycodedidchangenotification.md)
- [CWLinkDidChangeNotification](./cwlinkdidchangenotification.md)
- [CWLinkQualityDidChangeNotification](./cwlinkqualitydidchangenotification.md)
- [CWModeDidChangeNotification](./cwmodedidchangenotification.md)
- [CWPowerDidChangeNotification](./cwpowerdidchangenotification.md)
- [CWScanCacheDidUpdateNotification](./cwscancachedidupdatenotification.md)
- [CWSSIDDidChangeNotification](./cwssiddidchangenotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwlinkqualitynotificationrssikey)*