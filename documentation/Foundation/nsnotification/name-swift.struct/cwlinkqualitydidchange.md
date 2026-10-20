# CWLinkQualityDidChange

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

**Availability**:
- macOS 10.7+ - Deprecated in 10.10

> **Deprecated**: Use -[CWWiFiClient startMonitoringEventWithType:error:] with the CWEventTypeLinkQualityDidChange event type

## Declaration

```swift
static let CWLinkQualityDidChange: NSNotification.Name
```

#### Discussion

Posted when the link quality for any WLAN interface changes. The *object* for this notification is the corresponding BSD interface name. The *userInfo* dictionary for this notification contains the current RSSI and current transmit rate for the given CoreWLAN interface.

## See Also

### Core WLAN
- [static let CWBSSIDDidChange: NSNotification.Name](./cwbssiddidchange.md)
- [static let CWCountryCodeDidChange: NSNotification.Name](./cwcountrycodedidchange.md)
- [static let CWLinkDidChange: NSNotification.Name](./cwlinkdidchange.md)
- [static let CWModeDidChange: NSNotification.Name](./cwmodedidchange.md)
- [static let CWPowerDidChange: NSNotification.Name](./cwpowerdidchange.md)
- [static let CWSSIDDidChange: NSNotification.Name](./cwssiddidchange.md)
- [static let CWScanCacheDidUpdate: NSNotification.Name](./cwscancachedidupdate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/cwlinkqualitydidchange)*