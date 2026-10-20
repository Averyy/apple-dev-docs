# contactsDomains

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The contacts servers that the system routes connections from the Contacts app through for a per-app VPN.

**Availability**:
- macOS 10.15.4+

## Declaration

```swift
var contactsDomains: [String] { get set }
```

```objc
@property (copy) NSArray<NSString *> * contactsDomains;
```

#### Discussion

This property applies only to per-app VPNs.

## See Also

### Configuring a per-app VPN
- [class func forPerAppVPN() -> Self](./forperappvpn%28%29.md)
  Returns a tunnel provider manager for managing a per-app VPN configuration.
- [var appRules: [NEAppRule]](./apprules.md)
  The rules for specific apps in a per-app VPN.
- [var excludedDomains: [String]](./excludeddomains.md)
  The domains that the system excludes from a per-app VPN.
- [var associatedDomains: [String]](./associateddomains.md)
  The domains that the system routes network traffic through for a per-app VPN.
- [var calendarDomains: [String]](./calendardomains.md)
  The calendar servers that the system routes connections from the Calendar app through for a per-app VPN.
- [var mailDomains: [String]](./maildomains.md)
  The mail servers that the system routes connections from the Mail app through for a per-app VPN.
- [var safariDomains: [String]](./safaridomains.md)
  The website domains that the system routes connections from the Safari app through a per-app VPN.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelprovidermanager/contactsdomains)*