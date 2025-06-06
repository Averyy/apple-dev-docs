# NWHostEndpoint

**Framework**: Network Extension  
**Kind**: class

A network endpoint specified by DNS name (or IP address) and port.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NWHostEndpoint
```

## Topics

### Initializing host endpoints
- [convenience init(hostname: String, port: String)](nwhostendpoint/init(hostname:port:).md)
  Create a host endpoint with a hostname and port.
### Getting endpoint properties
- [var hostname: String](nwhostendpoint/hostname.md)
  The endpoint’s hostname.
- [var port: String](nwhostendpoint/port.md)
  The endpoint’s port, represented as a string.

## Relationships

### Inherits From
- [NWEndpoint](nwendpoint.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NWBonjourServiceEndpoint](nwbonjourserviceendpoint.md)
  A network endpoint specified as a Bonjour service name, type, and domain.
- [class NWEndpoint](nwendpoint.md)
  An abstract base class, shared by [`NWHostEndpoint`](nwhostendpoint.md) or [`NWBonjourServiceEndpoint`](nwbonjourserviceendpoint.md), that represents the source or destination of a network connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwhostendpoint)*