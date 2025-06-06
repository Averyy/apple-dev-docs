# excludedDomains

**Framework**: Network Extension  
**Kind**: property

The domains that the system excludes from a per-app VPN.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var excludedDomains: [String] { get set }
```

## Mentions

- [Routing your VPN network traffic](routing-your-vpn-network-traffic.md)

#### Discussion

For per-app VPNs only, the system doesn’t route network traffic to servers within these domains.

## See Also

- [class func forPerAppVPN() -> Self](netunnelprovidermanager/forperappvpn.md)
  Returns a tunnel provider manager for managing a per-app VPN configuration.
- [var appRules: [NEAppRule]](netunnelprovidermanager/apprules.md)
  The rules for specific apps in a per-app VPN.
- [var associatedDomains: [String]](netunnelprovidermanager/associateddomains.md)
  The domains that the system routes network traffic through for a per-app VPN.
- [var calendarDomains: [String]](netunnelprovidermanager/calendardomains.md)
  The calendar servers that the system routes connections from the Calendar app through for a per-app VPN.
- [var contactsDomains: [String]](netunnelprovidermanager/contactsdomains.md)
  The contacts servers that the system routes connections from the Contacts app through for a per-app VPN.
- [var mailDomains: [String]](netunnelprovidermanager/maildomains.md)
  The mail servers that the system routes connections from the Mail app through for a per-app VPN.
- [var safariDomains: [String]](netunnelprovidermanager/safaridomains.md)
  The website domains that the system routes connections from the Safari app through a per-app VPN.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelprovidermanager/excludeddomains)*