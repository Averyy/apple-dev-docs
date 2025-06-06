# RemoteCallTarget

**Framework**: Distributed  
**Kind**: struct

Represents a ‘target’ of a distributed call, such as a `distributed func` or `distributed` computed property. Identification schemes may vary between systems, and are subject to evolution.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct RemoteCallTarget
```

#### Overview

Actor systems generally should treat the `identifier` as an opaque string, and pass it along to the remote system for in their `remoteCall` implementation. Alternative approaches are possible, where the identifiers are either compressed, cached, or represented in other ways, as long as the recipient system is able to determine which target was intended to be invoked.

The string representation will attempt to pretty print the target identifier, however its exact format is not specified and may change in future versions.

## Topics

### Operators
- [static func == (RemoteCallTarget, RemoteCallTarget) -> Bool](remotecalltarget/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(String)](remotecalltarget/init(_:).md)
### Instance Properties
- [var description: String](remotecalltarget/description.md)
  Attempts to pretty format the underlying target identifier. If unable to, returns the raw underlying identifier.
- [var hashValue: Int](remotecalltarget/hashvalue.md)
  The hash value.
- [var identifier: String](remotecalltarget/identifier.md)
  The underlying identifier of the target, returned as-is.
### Instance Methods
- [func hash(into: inout Hasher)](remotecalltarget/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](remotecalltarget/equatable-implementations.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)

## See Also

- [struct RemoteCallArgument](remotecallargument.md)
  Represents an argument passed to a distributed call target.
- [protocol DistributedTargetInvocationEncoder](distributedtargetinvocationencoder.md)
  Used to encode an invocation of a distributed target (method or computed property).
- [protocol DistributedTargetInvocationDecoder](distributedtargetinvocationdecoder.md)
  Decoder that must be provided to `executeDistributedTarget` and is used by the Swift runtime to decode arguments of the invocation.
- [protocol DistributedTargetInvocationResultHandler](distributedtargetinvocationresulthandler.md)
  Protocol a distributed invocation execution’s result handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/remotecalltarget)*