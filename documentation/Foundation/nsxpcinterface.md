# NSXPCInterface

**Framework**: Foundation  
**Kind**: class

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

#### Overview

This object holds all information about the interface of an exported object or remote object proxy. It describes what messages are allowed, what kinds of objects are allowed as arguments, what the signature of any reply blocks are, and information about additional proxy objects.

## Topics

### Initializers
- [init(with: Protocol)](nsxpcinterface/init(with:).md)
  Returns an NSXPCInterface instance for a given protocol.
### Instance Properties
- [var `protocol`: Protocol](nsxpcinterface/protocol.md)
  The Objective-C protocol that this interface is based on.
### Instance Methods
- [func classes(for: Selector, argumentIndex: Int, ofReply: Bool) -> Set<AnyHashable>](nsxpcinterface/classes(for:argumentindex:ofreply:).md)
  Returns the current list of allowed classes that can appear within the specified collection object argument to the specified method.
- [func forSelector(Selector, argumentIndex: Int, ofReply: Bool) -> NSXPCInterface?](nsxpcinterface/forselector(_:argumentindex:ofreply:).md)
  Returns the interface previously set for the specified selector and parameter.
- [func setClasses(Set<AnyHashable>, for: Selector, argumentIndex: Int, ofReply: Bool)](nsxpcinterface/setclasses(_:for:argumentindex:ofreply:).md)
  Sets the classes that can appear within the (numerically) specified collection object argument to the specified method.
- [func setInterface(NSXPCInterface, for: Selector, argumentIndex: Int, ofReply: Bool)](nsxpcinterface/setinterface(_:for:argumentindex:ofreply:).md)
  Configures a specific parameter of a method to be sent as a proxy object instead of copied.
- [func setXPCType(xpc_type_t, for: Selector, argumentIndex: Int, ofReply: Bool)](nsxpcinterface/setxpctype(_:for:argumentindex:ofreply:).md)
- [func xpcType(for: Selector, argumentIndex: Int, ofReply: Bool) -> xpc_type_t?](nsxpcinterface/xpctype(for:argumentindex:ofreply:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSXPCProxyCreating](nsxpcproxycreating.md)
  Methods for creating new proxy objects.
- [class NSXPCConnection](nsxpcconnection.md)
  A bidirectional communication channel between two processes.
- [class NSXPCCoder](nsxpccoder.md)
  A coder that encodes and decodes objects that your app sends over an XPC connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcinterface)*