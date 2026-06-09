# NetworkVPNAlwaysOnProxies_Protocol_HTTPObject

**Framework**: Device Management  
**Kind**: dictionary

The dictionary to use to configure the HTTP (non-TLS) server.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNAlwaysOnProxies_Protocol_HTTPObject
```

## Properties

- `Enable` (boolean): If `true`, enables proxy for HTTP traffic.
- `HostName` (string): The host name of the HTTP proxy.
- `Port` (integer): The port number of the HTTP proxy. This field is required if `HostName` is specified.

## See Also

- [object NetworkVPNAlwaysOnProxies_Protocol_HTTPSObject](networkvpnalwaysonproxies_protocol_httpsobject.md)
  The dictionary to use to configure the HTTPS (TLS) server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnalwaysonproxies_protocol_httpobject)*