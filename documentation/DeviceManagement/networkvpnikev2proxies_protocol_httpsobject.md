# NetworkVPNIKEV2Proxies_Protocol_HTTPSObject

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

The dictionary to use to configure the HTTPS (TLS) server.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```
object NetworkVPNIKEV2Proxies_Protocol_HTTPSObject
```

## Properties

- `Enable` (boolean): If `true`, enables proxy for HTTPS traffic.

  **Default**: `false`
- `HostName` (string): The host name of the HTTPS proxy.
- `Port` (integer): The port number of the HTTPS proxy. This field is required if `HostName` is specified.

  **Minimum**: `0`; **Maximum**: `65535`

## See Also

### Objects
- [object NetworkVPNIKEV2Proxies_Protocol_HTTPObject](./networkvpnikev2proxies_protocol_httpobject.md)
  The dictionary to use to configure the HTTP (non-TLS) server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnikev2proxies_protocol_httpsobject)*