# NWHostEndpoint

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

A network endpoint specified by DNS name (or IP address) and port.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_endpoint_t`](../Network/nw_endpoint_t.md) type from the [Network](../Network/Network.md) framework instead.

## Declaration

```swift
class NWHostEndpoint
```

```objc
@interface NWHostEndpoint : NWEndpoint
```

## Topics

### Initializing host endpoints
- [convenience init(hostname: String, port: String)](./nwhostendpoint/init%28hostname,port%29.md)
  Create a host endpoint with a hostname and port.
### Getting endpoint properties
- [var hostname: String](./nwhostendpoint/hostname.md)
  The endpoint’s hostname.
- [var port: String](./nwhostendpoint/port.md)
  The endpoint’s port, represented as a string.

## Relationships

### Inherits From
- [NWEndpoint](./nwendpoint.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Endpoints
- [class NWBonjourServiceEndpoint](./nwbonjourserviceendpoint.md)
  A network endpoint specified as a Bonjour service name, type, and domain.
- [class NWEndpoint](./nwendpoint.md)
  An abstract base class, shared by [`NWHostEndpoint`](./nwhostendpoint.md) or [`NWBonjourServiceEndpoint`](./nwbonjourserviceendpoint.md), that represents the source or destination of a network connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwhostendpoint)*