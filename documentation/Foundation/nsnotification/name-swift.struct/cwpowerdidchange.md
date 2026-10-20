# CWPowerDidChange

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

**Availability**:
- macOS 10.6+ - Deprecated in 10.10

> **Deprecated**: Use -[CWWiFiClient startMonitoringEventWithType:error:] with the CWEventTypePowerDidChange event type

## Declaration

```swift
static let CWPowerDidChange: NSNotification.Name
```

#### Discussion

Posted when the power state of any WLAN interface changes. The *object* for this notification is the corresponding BSD interface name. This notification does not contain a *userInfo* dictionary.

## See Also

### Core WLAN
- [static let CWBSSIDDidChange: NSNotification.Name](./cwbssiddidchange.md)
- [static let CWCountryCodeDidChange: NSNotification.Name](./cwcountrycodedidchange.md)
- [static let CWLinkDidChange: NSNotification.Name](./cwlinkdidchange.md)
- [static let CWLinkQualityDidChange: NSNotification.Name](./cwlinkqualitydidchange.md)
- [static let CWModeDidChange: NSNotification.Name](./cwmodedidchange.md)
- [static let CWSSIDDidChange: NSNotification.Name](./cwssiddidchange.md)
- [static let CWScanCacheDidUpdate: NSNotification.Name](./cwscancachedidupdate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/cwpowerdidchange)*