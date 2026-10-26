# CWPowerDidChangeNotification

**Framework**: Core WLAN  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- macOS 10.6+ - Deprecated in 10.10

## Declaration

```c
extern NSString * const CWPowerDidChangeNotification;
```

#### Discussion

Posted when the power state of any WLAN interface changes. The *object* for this notification is the corresponding BSD interface name. This notification does not contain a *userInfo* dictionary.

## See Also

### Constants
- [CWBSSIDDidChangeNotification](./cwbssiddidchangenotification.md)
- [CWCountryCodeDidChangeNotification](./cwcountrycodedidchangenotification.md)
- [let CWErrorDomain: String](./cwerrordomain.md)
- [CWLinkDidChangeNotification](./cwlinkdidchangenotification.md)
- [CWLinkQualityDidChangeNotification](./cwlinkqualitydidchangenotification.md)
- [let CWLinkQualityNotificationRSSIKey: String](./cwlinkqualitynotificationrssikey.md)
- [let CWLinkQualityNotificationTransmitRateKey: String](./cwlinkqualitynotificationtransmitratekey.md)
- [CWModeDidChangeNotification](./cwmodedidchangenotification.md)
- [CWScanCacheDidUpdateNotification](./cwscancachedidupdatenotification.md)
- [CWSSIDDidChangeNotification](./cwssiddidchangenotification.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwpowerdidchangenotification)*