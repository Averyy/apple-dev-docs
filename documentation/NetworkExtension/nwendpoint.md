# NWEndpoint

**Framework**: Network Extension  
**Kind**: class

An abstract base class, shared by [`NWHostEndpoint`](nwhostendpoint.md) or [`NWBonjourServiceEndpoint`](nwbonjourserviceendpoint.md), that represents the source or destination of a network connection.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NWEndpoint
```

#### Overview

All endpoint objects are static collections of parameters that describe a network resource. They do not directly provide any resolution services, but instead must be used with other classes to be resolved and create connections.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [NWBonjourServiceEndpoint](nwbonjourserviceendpoint.md)
- [NWHostEndpoint](nwhostendpoint.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class NWHostEndpoint](nwhostendpoint.md)
  A network endpoint specified by DNS name (or IP address) and port.
- [class NWBonjourServiceEndpoint](nwbonjourserviceendpoint.md)
  A network endpoint specified as a Bonjour service name, type, and domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwendpoint)*