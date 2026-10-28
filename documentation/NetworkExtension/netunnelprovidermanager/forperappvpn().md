# forPerAppVPN()

**Framework**: Network Extension  
**Kind**: method  
**Role**: Type Method

Returns a tunnel provider manager for managing a per-app VPN configuration.

**Availability**:
- macOS 10.15.4+

## Declaration

```swift
class func forPerAppVPN() -> Self
```

```objc
+ (instancetype) forPerAppVPN;
```

## Return Value

An object you use to configure a per-app VPN.

## See Also

### Configuring a per-app VPN
- [var appRules: [NEAppRule]](./apprules.md)
  The rules for specific apps in a per-app VPN.
- [var excludedDomains: [String]](./excludeddomains.md)
  The domains that the system excludes from a per-app VPN.
- [var associatedDomains: [String]](./associateddomains.md)
  The domains that the system routes network traffic through for a per-app VPN.
- [var calendarDomains: [String]](./calendardomains.md)
  The calendar servers that the system routes connections from the Calendar app through for a per-app VPN.
- [var contactsDomains: [String]](./contactsdomains.md)
  The contacts servers that the system routes connections from the Contacts app through for a per-app VPN.
- [var mailDomains: [String]](./maildomains.md)
  The mail servers that the system routes connections from the Mail app through for a per-app VPN.
- [var safariDomains: [String]](./safaridomains.md)
  The website domains that the system routes connections from the Safari app through a per-app VPN.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelprovidermanager/forperappvpn())*