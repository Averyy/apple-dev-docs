# NSXPCListenerEndpoint

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An object that names a specific XPC listener.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSXPCListenerEndpoint
```

```objc
@interface NSXPCListenerEndpoint : NSObject
```

## Overview

An instance of [`NSXPCListenerEndpoint`](./nsxpclistenerendpoint.md) may be retrieved from an [`NSXPCListener`](./nsxpclistener.md) instance and sent over existing [`NSXPCConnection`](./nsxpcconnection.md)s. A process may then use the endpoint to create a new [`NSXPCConnection`](./nsxpcconnection.md) to the original [`NSXPCListener`](./nsxpclistener.md).

This pattern is useful if you have a service which multiplexes work to other services. The service can act as an intermediate helper. The requesting application does not need to know specifically which service it is connecting to, just that it implements a known [`NSXPCInterface`](./nsxpcinterface.md).

## Topics

### Initializers
- [init?(coder: NSCoder)](./nsxpclistenerendpoint/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### XPC Services
- [class NSXPCListener](./nsxpclistener.md)
  A listener that waits for new incoming connections, configures them, and accepts or rejects them.
- [protocol NSXPCListenerDelegate](./nsxpclistenerdelegate.md)
  The protocol that delegates to the XPC listener use to accept or reject new connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpclistenerendpoint)*