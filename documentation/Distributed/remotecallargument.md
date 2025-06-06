# RemoteCallArgument

**Framework**: Distributed  
**Kind**: struct

Represents an argument passed to a distributed call target.

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
struct RemoteCallArgument<Value>
```

## Topics

### Initializers
- [init(label: String?, name: String, value: Value)](remotecallargument/init(label:name:value:).md)
### Instance Properties
- [var effectiveLabel: String](remotecallargument/effectivelabel.md)
  The effective label of this argument. This reflects the semantics of call sites of function declarations without explicit label definitions in Swift.
- [let label: String?](remotecallargument/label.md)
  The “argument label” of the argument. The label is the name visible name used in external calls made to this target, e.g. for `func hello(label name: String)` it is `label`.
- [let name: String](remotecallargument/name.md)
  The internal name of parameter this argument is accessible as in the function body. It is not part of the functions API and may change without breaking the target identifier.
- [let value: Value](remotecallargument/value.md)
  The value of the argument being passed to the call. As `RemoteCallArgument` is always used in conjunction with `recordArgument` and populated by the compiler, this Value will generally conform to a distributed actor system’s `SerializationRequirement`.

## See Also

- [struct RemoteCallTarget](remotecalltarget.md)
  Represents a ‘target’ of a distributed call, such as a `distributed func` or `distributed` computed property. Identification schemes may vary between systems, and are subject to evolution.
- [protocol DistributedTargetInvocationEncoder](distributedtargetinvocationencoder.md)
  Used to encode an invocation of a distributed target (method or computed property).
- [protocol DistributedTargetInvocationDecoder](distributedtargetinvocationdecoder.md)
  Decoder that must be provided to `executeDistributedTarget` and is used by the Swift runtime to decode arguments of the invocation.
- [protocol DistributedTargetInvocationResultHandler](distributedtargetinvocationresulthandler.md)
  Protocol a distributed invocation execution’s result handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/remotecallargument)*