# NetworkVPNAlwaysOnProxies_ProtocolObject

**Framework**: Device Management  
**Kind**: dictionary

The dictionary to use to configure HTTP servers  for `Proxies` for use with `VPN`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNAlwaysOnProxies_ProtocolObject
```

## Topics

### Objects
- [object NetworkVPNAlwaysOnProxies_Protocol_HTTPObject](networkvpnalwaysonproxies_protocol_httpobject.md)
  The dictionary to use to configure the HTTP (non-TLS) server.
- [object NetworkVPNAlwaysOnProxies_Protocol_HTTPSObject](networkvpnalwaysonproxies_protocol_httpsobject.md)
  The dictionary to use to configure the HTTPS (TLS) server.

## Properties

- `CredentialsAssetReference` (string): The identifier of an asset declaration that contains the credentials (user name and password) to authenticate with the proxy server.
- `HTTP` (NetworkVPNAlwaysOnProxies_Protocol_HTTPObject): The dictionary to use to configure the HTTP (non-TLS) server.
- `HTTPS` (NetworkVPNAlwaysOnProxies_Protocol_HTTPSObject): The dictionary to use to configure the HTTPS (TLS) server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnalwaysonproxies_protocolobject)*