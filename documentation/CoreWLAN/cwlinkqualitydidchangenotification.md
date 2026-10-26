# CWLinkQualityDidChangeNotification

**Framework**: Core WLAN  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- macOS 10.7+ - Deprecated in 10.10

## Declaration

```c
extern NSString * const CWLinkQualityDidChangeNotification;
```

#### Discussion

Posted when the link quality for any WLAN interface changes. The *object* for this notification is the corresponding BSD interface name. The *userInfo* dictionary for this notification contains the current RSSI and current transmit rate for the given CoreWLAN interface.

## See Also

### Constants
- [CWBSSIDDidChangeNotification](./cwbssiddidchangenotification.md)
- [CWCountryCodeDidChangeNotification](./cwcountrycodedidchangenotification.md)
- [let CWErrorDomain: String](./cwerrordomain.md)
- [CWLinkDidChangeNotification](./cwlinkdidchangenotification.md)
- [let CWLinkQualityNotificationRSSIKey: String](./cwlinkqualitynotificationrssikey.md)
- [let CWLinkQualityNotificationTransmitRateKey: String](./cwlinkqualitynotificationtransmitratekey.md)
- [CWModeDidChangeNotification](./cwmodedidchangenotification.md)
- [CWPowerDidChangeNotification](./cwpowerdidchangenotification.md)
- [CWScanCacheDidUpdateNotification](./cwscancachedidupdatenotification.md)
- [CWSSIDDidChangeNotification](./cwssiddidchangenotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwlinkqualitydidchangenotification)*