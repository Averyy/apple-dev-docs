# NetworkVPNIPSecOnDemandObject

**Framework**: Device Management  
**Kind**: dictionary

Specifies details about how the system controls on-demand VPN.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNIPSecOnDemandObject
```

## Topics

### Objects
- [object NetworkVPNIPSecRulesElementObject](networkvpnipsecruleselementobject.md)
  An array of dictionaries defining On Demand Rules.

## Properties

- `Enabled` (boolean): If `true`, enables VPN On Demand.
- `Rules` ([NetworkVPNIPSecRulesElementObject]): An array of dictionaries defining On Demand Rules.

## See Also

- [object NetworkVPNIPSecAuthenticationObject](networkvpnipsecauthenticationobject.md)
  Settings that control authentication.
- [object NetworkVPNIPSecDNSObject](networkvpnipsecdnsobject.md)
  A dictionary to use for all VPN types.
- [object NetworkVPNIPSecIdleObject](networkvpnipsecidleobject.md)
  Specifies details about how the system handles idle VPN connections.
- [object NetworkVPNIPSecProxiesObject](networkvpnipsecproxiesobject.md)
  The dictionary to use to configure `Proxies` for use with `VPN`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnipsecondemandobject)*