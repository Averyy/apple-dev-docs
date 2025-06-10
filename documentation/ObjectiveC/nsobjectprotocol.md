# NSObjectProtocol

**Framework**: Objective-C Runtime  
**Kind**: protocol

The group of methods that are fundamental to all Objective-C objects.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
protocol NSObjectProtocol
```

#### Overview

> **Note**:  This protocol is imported into Swift with the name `NSObjectProtocol`.

An object that conforms to this protocol can be considered a first-class object. Such an object can be asked about its:

- Class, and the place of its class in the inheritance hierarchy.
- Conformance to protocols.
- Ability to respond to a particular message.

The Cocoa root class [`NSObject`](nsobject-swift.class.md) adopts this protocol, so all objects inheriting from [`NSObject`](nsobject-swift.class.md) have the features described by this protocol.

## Topics

### Identifying Classes
- [var superclass: AnyClass?](nsobjectprotocol/superclass.md)
  Returns the class object for the receiver’s superclass.
### Identifying and Comparing Objects
- [func isEqual(Any?) -> Bool](nsobjectprotocol/isequal(_:).md)
  Returns a Boolean value that indicates whether the receiver and a given object are equal.
- [var hash: Int](nsobjectprotocol/hash.md)
  Returns an integer that can be used as a table address in a hash table structure.
- [func `self`() -> Self](nsobjectprotocol/self.md)
  Returns the receiver.
### Testing Object Inheritance, Behavior, and Conformance
- [func isKind(of: AnyClass) -> Bool](nsobjectprotocol/iskind(of:).md)
  Returns a Boolean value that indicates whether the receiver is an instance of given class or an instance of any class that inherits from that class.
- [func isMember(of: AnyClass) -> Bool](nsobjectprotocol/ismember(of:).md)
  Returns a Boolean value that indicates whether the receiver is an instance of a given class.
- [func responds(to: Selector!) -> Bool](nsobjectprotocol/responds(to:).md)
  Returns a Boolean value that indicates whether the receiver implements or inherits a method that can respond to a specified message.
- [func conforms(to: Protocol) -> Bool](nsobjectprotocol/conforms(to:).md)
  Returns a Boolean value that indicates whether the receiver conforms to a given protocol.
### Describing Objects
- [var description: String](nsobjectprotocol/description.md)
  A textual representation of the receiver.
- [var debugDescription: String](nsobjectprotocol/debugdescription.md)
  A textual representation of the receiver to use with a debugger.
### Sending Messages
- [func perform(Selector!) -> Unmanaged<AnyObject>!](nsobjectprotocol/perform(_:).md)
  Sends a specified message to the receiver and returns the result of the message.
- [func perform(Selector!, with: Any!) -> Unmanaged<AnyObject>!](nsobjectprotocol/perform(_:with:).md)
  Sends a message to the receiver with an object as the argument.
- [func perform(Selector!, with: Any!, with: Any!) -> Unmanaged<AnyObject>!](nsobjectprotocol/perform(_:with:with:).md)
  Sends a message to the receiver with two objects as arguments.
### Identifying Proxies
- [func isProxy() -> Bool](nsobjectprotocol/isproxy.md)
  Returns a Boolean value that indicates whether the receiver does not descend from [`NSObject`](nsobject-swift.class.md).

## Relationships

### Conforming Types
- [NSObject](nsobject-swift.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobjectprotocol)*