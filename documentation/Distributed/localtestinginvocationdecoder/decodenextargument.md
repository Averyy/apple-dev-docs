# decodeNextArgument()

**Framework**: Distributed  
**Kind**: method

Attempt to decode the next argument from the underlying buffers into pre-allocated storage pointed at by ‘pointer’.

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
final func decodeNextArgument<Argument>() throws -> Argument where Argument : Decodable, Argument : Encodable
```

#### Discussion

This method should throw if it has no more arguments available, if decoding the argument failed, or, optionally, if the argument type we’re trying to decode does not match the stored type.

The result of the decoding operation must be stored into the provided ‘pointer’ rather than returning a value. This pattern allows the runtime to use a heavily optimized, pre-allocated buffer for all the arguments and their expected types. The ‘pointer’ passed here is a pointer to a “slot” in that pre-allocated buffer. That buffer will then be passed to a thunk that performs the actual distributed (local) instance method invocation.

##### Serialization Requirement

Implementations of this method must ensure that the `Argument` type parameter conforms to the types’ `SerializationRequirement`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/localtestinginvocationdecoder/decodenextargument())*