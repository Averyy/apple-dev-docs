# NetworkVPNIPSecProxies_Protocol_HTTPSObject

**Framework**: Device Management  
**Kind**: dictionary

The dictionary to use to configure the HTTPS (TLS) server.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNIPSecProxies_Protocol_HTTPSObject
```

## Properties

- `Enable` (boolean): If `true`, enables proxy for HTTPS traffic.
- `HostName` (string): The host name of the HTTPS proxy.
- `Port` (integer): The port number of the HTTPS proxy. This field is required if `HostName` is specified.

## See Also

- [object NetworkVPNIPSecProxies_Protocol_HTTPObject](networkvpnipsecproxies_protocol_httpobject.md)
  The dictionary to use to configure the HTTP (non-TLS) server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnipsecproxies_protocol_httpsobject)*