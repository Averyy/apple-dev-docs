# NetworkVPNIPSecIdleObject

**Framework**: Device Management  
**Kind**: dictionary

Specifies details about how the system handles idle VPN connections.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNIPSecIdleObject
```

## Properties

- `Disconnect` (boolean): If `true`, disconnects after an on-demand connection idles.
- `Timer` (integer): The length of time to wait, in seconds, before disconnecting an on-demand connection.

## See Also

- [object NetworkVPNIPSecAuthenticationObject](networkvpnipsecauthenticationobject.md)
  Settings that control authentication.
- [object NetworkVPNIPSecDNSObject](networkvpnipsecdnsobject.md)
  A dictionary to use for all VPN types.
- [object NetworkVPNIPSecOnDemandObject](networkvpnipsecondemandobject.md)
  Specifies details about how the system controls on-demand VPN.
- [object NetworkVPNIPSecProxiesObject](networkvpnipsecproxiesobject.md)
  The dictionary to use to configure `Proxies` for use with `VPN`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnipsecidleobject)*