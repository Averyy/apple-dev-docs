# NWEndpoint

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

An abstract base class, shared by [`NWHostEndpoint`](./nwhostendpoint.md) or [`NWBonjourServiceEndpoint`](./nwbonjourserviceendpoint.md), that represents the source or destination of a network connection.

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
class NWEndpoint
```

```objc
@interface NWEndpoint : NSObject
```

#### Overview

All endpoint objects are static collections of parameters that describe a network resource. They do not directly provide any resolution services, but instead must be used with other classes to be resolved and create connections.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NWBonjourServiceEndpoint](./nwbonjourserviceendpoint.md)
- [NWHostEndpoint](./nwhostendpoint.md)
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
- [class NWHostEndpoint](./nwhostendpoint.md)
  A network endpoint specified by DNS name (or IP address) and port.
- [class NWBonjourServiceEndpoint](./nwbonjourserviceendpoint.md)
  A network endpoint specified as a Bonjour service name, type, and domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwendpoint)*