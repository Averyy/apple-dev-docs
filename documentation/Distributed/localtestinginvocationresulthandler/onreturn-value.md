# onReturn(value:)

**Framework**: Distributed  
**Kind**: method

Invoked when the distributed target execution returns successfully. The `value` is the return value of the executed distributed invocation target.

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
func onReturn<Success>(value: Success) async throws where Success : Decodable, Success : Encodable
```

##### Serialization Requirement

Implementations of this method must ensure that the `Success` type parameter conforms to the types’ `SerializationRequirement`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/localtestinginvocationresulthandler/onreturn(value:))*