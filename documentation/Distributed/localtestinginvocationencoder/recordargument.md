# recordArgument(_:)

**Framework**: Distributed  
**Kind**: method

Record an argument of `Argument` type. This will be invoked for every argument of the target, in declaration order.

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
mutating func recordArgument<Value>(_ argument: RemoteCallArgument<Value>) throws where Value : Decodable, Value : Encodable
```

##### Serialization Requirement

Implementations of this method must ensure that the `Value` type parameter conforms to the types’ `SerializationRequirement`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/localtestinginvocationencoder/recordargument(_:))*