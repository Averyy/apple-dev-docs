# NetworkVPNVPNPluginProxies_ProtocolObject

**Framework**: Device Management  
**Kind**: dictionary

The dictionary to use to configure HTTP servers  for `Proxies` for use with `VPN`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNVPNPluginProxies_ProtocolObject
```

## Topics

### Objects
- [object NetworkVPNVPNPluginProxies_Protocol_HTTPObject](networkvpnvpnpluginproxies_protocol_httpobject.md)
  The dictionary to use to configure the HTTP (non-TLS) server.
- [object NetworkVPNVPNPluginProxies_Protocol_HTTPSObject](networkvpnvpnpluginproxies_protocol_httpsobject.md)
  The dictionary to use to configure the HTTPS (TLS) server.

## Properties

- `CredentialsAssetReference` (string): The identifier of an asset declaration that contains the credentials (user name and password) to authenticate with the proxy server.
- `HTTP` (NetworkVPNVPNPluginProxies_Protocol_HTTPObject): The dictionary to use to configure the HTTP (non-TLS) server.
- `HTTPS` (NetworkVPNVPNPluginProxies_Protocol_HTTPSObject): The dictionary to use to configure the HTTPS (TLS) server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnvpnpluginproxies_protocolobject)*