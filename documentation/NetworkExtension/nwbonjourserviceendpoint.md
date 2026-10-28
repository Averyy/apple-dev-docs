# NWBonjourServiceEndpoint

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

A network endpoint specified as a Bonjour service name, type, and domain.

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
class NWBonjourServiceEndpoint
```

```objc
@interface NWBonjourServiceEndpoint : NWEndpoint
```

## Overview

For example, the Bonjour service `MyMusicStudio._music._tcp.local.` has the name `"MyMusicStudio"`, the type `"_music._tcp"`, and the domain `"local"`.

## Topics

### Initializing Bonjour service endpoints
- [convenience init(name: String, type: String, domain: String)](./nwbonjourserviceendpoint/init%28name,type,domain%29.md)
  Create an endpoint with a Bonjour service name, type, and domain. All fields must be specified.
### Getting endpoint properties
- [var name: String](./nwbonjourserviceendpoint/name.md)
  The endpoint’s Bonjour service name.
- [var type: String](./nwbonjourserviceendpoint/type.md)
  The endpoint’s Bonjour service type.
- [var domain: String](./nwbonjourserviceendpoint/domain.md)
  The endpoint’s Bonjour service domain, such as `"local"`.

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
- [class NWHostEndpoint](./nwhostendpoint.md)
  A network endpoint specified by DNS name (or IP address) and port.
- [class NWEndpoint](./nwendpoint.md)
  An abstract base class, shared by [`NWHostEndpoint`](./nwhostendpoint.md) or [`NWBonjourServiceEndpoint`](./nwbonjourserviceendpoint.md), that represents the source or destination of a network connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwbonjourserviceendpoint)*