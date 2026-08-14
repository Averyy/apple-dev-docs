# NWBonjourServiceEndpoint

**Framework**: Network Extension  
**Kind**: class

A network endpoint specified as a Bonjour service name, type, and domain.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NWBonjourServiceEndpoint
```

#### Overview

For example, the Bonjour service `MyMusicStudio._music._tcp.local.` has the name `"MyMusicStudio"`, the type `"_music._tcp"`, and the domain `"local"`.

## Topics

### Initializing Bonjour service endpoints
- [convenience init(name: String, type: String, domain: String)](nwbonjourserviceendpoint/init(name:type:domain:).md)
  Create an endpoint with a Bonjour service name, type, and domain. All fields must be specified.
### Getting endpoint properties
- [var name: String](nwbonjourserviceendpoint/name.md)
  The endpoint’s Bonjour service name.
- [var type: String](nwbonjourserviceendpoint/type.md)
  The endpoint’s Bonjour service type.
- [var domain: String](nwbonjourserviceendpoint/domain.md)
  The endpoint’s Bonjour service domain, such as `"local"`.

## Relationships

### Inherits From
- [NWEndpoint](nwendpoint.md)
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
- [class NWEndpoint](nwendpoint.md)
  An abstract base class, shared by [`NWHostEndpoint`](nwhostendpoint.md) or [`NWBonjourServiceEndpoint`](nwbonjourserviceendpoint.md), that represents the source or destination of a network connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwbonjourserviceendpoint)*