# NSXPCInterface

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An interface that may be sent to an exported object or remote object proxy.

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
class NSXPCInterface
```

```objc
@interface NSXPCInterface : NSObject
```

## Overview

This object holds all information about the interface of an exported object or remote object proxy. It describes what messages are allowed, what kinds of objects are allowed as arguments, what the signature of any reply blocks are, and information about additional proxy objects.

## Topics

### Initializers
- [init(with: Protocol)](./nsxpcinterface/init%28with%29.md)
  Returns an NSXPCInterface instance for a given protocol.
- [init(withProtocol: Protocol)](./nsxpcinterface/init%28withprotocol%29.md)
### Instance Properties
- [var `protocol`: Protocol](./nsxpcinterface/protocol.md)
  The Objective-C protocol that this interface is based on.
### Instance Methods
- [func classes(for: Selector, argumentIndex: Int, ofReply: Bool) -> Set<AnyHashable>](./nsxpcinterface/classes%28for,argumentindex,ofreply%29.md)
  Returns the current list of allowed classes that can appear within the specified collection object argument to the specified method.
- [func forSelector(Selector, argumentIndex: Int, ofReply: Bool) -> NSXPCInterface?](./nsxpcinterface/forselector%28_,argumentindex,ofreply%29.md)
  Returns the interface previously set for the specified selector and parameter.
- [func setClasses(Set<AnyHashable>, for: Selector, argumentIndex: Int, ofReply: Bool)](./nsxpcinterface/setclasses%28_,for,argumentindex,ofreply%29.md)
  Sets the classes that can appear within the (numerically) specified collection object argument to the specified method.
- [func setInterface(NSXPCInterface, for: Selector, argumentIndex: Int, ofReply: Bool)](./nsxpcinterface/setinterface%28_,for,argumentindex,ofreply%29.md)
  Configures a specific parameter of a method to be sent as a proxy object instead of copied.
- [func setXPCType(xpc_type_t, for: Selector, argumentIndex: Int, ofReply: Bool)](./nsxpcinterface/setxpctype%28_,for,argumentindex,ofreply%29.md)
- [func xpcType(for: Selector, argumentIndex: Int, ofReply: Bool) -> xpc_type_t?](./nsxpcinterface/xpctype%28for,argumentindex,ofreply%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### XPC Client
- [protocol NSXPCProxyCreating](./nsxpcproxycreating.md)
  Methods for creating new proxy objects.
- [class NSXPCConnection](./nsxpcconnection.md)
  A bidirectional communication channel between two processes.
- [class NSXPCCoder](./nsxpccoder.md)
  A coder that encodes and decodes objects that your app sends over an XPC connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcinterface)*