# recordReturnType(_:)

**Framework**: Distributed  
**Kind**: method

Record the return type of the distributed method. This method will not be invoked if the target is returning `Void`.

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
mutating func recordReturnType<R>(_ type: R.Type) throws where R : Decodable, R : Encodable
```

##### Serialization Requirement

Implementations of this method must ensure that the `R` type parameter conforms to the types’ `SerializationRequirement`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/localtestinginvocationencoder/recordreturntype(_:))*