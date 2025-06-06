# safariDomains

**Framework**: Network Extension  
**Kind**: property

The website domains that the system routes connections from the Safari app through a per-app VPN.

**Availability**:
- macOS 10.15.4+

## Declaration

```swift
var safariDomains: [String] { get set }
```

#### Discussion

For per-app VPNs only, when the user navigates in Safari to a website within one of these domains, the system routes the website traffic through the VPN.

## See Also

- [class func forPerAppVPN() -> Self](netunnelprovidermanager/forperappvpn.md)
  Returns a tunnel provider manager for managing a per-app VPN configuration.
- [var appRules: [NEAppRule]](netunnelprovidermanager/apprules.md)
  The rules for specific apps in a per-app VPN.
- [var excludedDomains: [String]](netunnelprovidermanager/excludeddomains.md)
  The domains that the system excludes from a per-app VPN.
- [var associatedDomains: [String]](netunnelprovidermanager/associateddomains.md)
  The domains that the system routes network traffic through for a per-app VPN.
- [var calendarDomains: [String]](netunnelprovidermanager/calendardomains.md)
  The calendar servers that the system routes connections from the Calendar app through for a per-app VPN.
- [var contactsDomains: [String]](netunnelprovidermanager/contactsdomains.md)
  The contacts servers that the system routes connections from the Contacts app through for a per-app VPN.
- [var mailDomains: [String]](netunnelprovidermanager/maildomains.md)
  The mail servers that the system routes connections from the Mail app through for a per-app VPN.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelprovidermanager/safaridomains)*