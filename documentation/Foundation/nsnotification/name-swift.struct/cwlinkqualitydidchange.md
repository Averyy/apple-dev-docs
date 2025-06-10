# CWLinkQualityDidChange

**Framework**: Foundation  
**Kind**: property

**Availability**:
- macOS 10.7+

## Declaration

```swift
static let CWLinkQualityDidChange: NSNotification.Name
```

#### Discussion

Posted when the link quality for any WLAN interface changes. The  for this notification is the corresponding BSD interface name. The  dictionary for this notification contains the current RSSI and current transmit rate for the given CoreWLAN interface.

## See Also

- [static let CWBSSIDDidChange: NSNotification.Name](nsnotification/name-swift.struct/cwbssiddidchange.md)
- [static let CWCountryCodeDidChange: NSNotification.Name](nsnotification/name-swift.struct/cwcountrycodedidchange.md)
- [static let CWLinkDidChange: NSNotification.Name](nsnotification/name-swift.struct/cwlinkdidchange.md)
- [static let CWModeDidChange: NSNotification.Name](nsnotification/name-swift.struct/cwmodedidchange.md)
- [static let CWPowerDidChange: NSNotification.Name](nsnotification/name-swift.struct/cwpowerdidchange.md)
- [static let CWSSIDDidChange: NSNotification.Name](nsnotification/name-swift.struct/cwssiddidchange.md)
- [static let CWScanCacheDidUpdate: NSNotification.Name](nsnotification/name-swift.struct/cwscancachedidupdate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/cwlinkqualitydidchange)*