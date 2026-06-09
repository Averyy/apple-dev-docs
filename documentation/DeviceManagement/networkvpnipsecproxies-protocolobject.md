# NetworkVPNIPSecProxies_ProtocolObject

**Framework**: Device Management  
**Kind**: dictionary

The dictionary to use to configure HTTP servers  for `Proxies` for use with `VPN`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNIPSecProxies_ProtocolObject
```

## Topics

### Objects
- [object NetworkVPNIPSecProxies_Protocol_HTTPObject](networkvpnipsecproxies_protocol_httpobject.md)
  The dictionary to use to configure the HTTP (non-TLS) server.
- [object NetworkVPNIPSecProxies_Protocol_HTTPSObject](networkvpnipsecproxies_protocol_httpsobject.md)
  The dictionary to use to configure the HTTPS (TLS) server.

## Properties

- `CredentialsAssetReference` (string): The identifier of an asset declaration that contains the credentials (user name and password) to authenticate with the proxy server.
- `HTTP` (NetworkVPNIPSecProxies_Protocol_HTTPObject): The dictionary to use to configure the HTTP (non-TLS) server.
- `HTTPS` (NetworkVPNIPSecProxies_Protocol_HTTPSObject): The dictionary to use to configure the HTTPS (TLS) server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnipsecproxies_protocolobject)*