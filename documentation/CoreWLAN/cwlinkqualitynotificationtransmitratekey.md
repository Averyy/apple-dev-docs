# CWLinkQualityNotificationTransmitRateKey

**Framework**: Core WLAN  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- macOS 10.6+ - Deprecated in 10.10

> **Deprecated**: Use -[CWWiFiClient startMonitoringEventWithType:error:] with the CWEventTypeLinkQualityDidChange event type

## Declaration

```swift
let CWLinkQualityNotificationTransmitRateKey: String
```

```c
extern NSString * const CWLinkQualityNotificationTransmitRateKey;
```

#### Discussion

NSNumber containing the current transmit rate value for the WLAN interface. Found in the *userInfo* dictionary for the *CWLinkQualityChangedNotification*.

## See Also

### Constants
- [let CWErrorDomain: String](./cwerrordomain.md)
- [let CWLinkQualityNotificationRSSIKey: String](./cwlinkqualitynotificationrssikey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwlinkqualitynotificationtransmitratekey)*