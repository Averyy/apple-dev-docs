# recordArgument(_:)

**Framework**: Distributed  
**Kind**: method  
**Required**: Yes

Record an argument of `Argument` type. This will be invoked for every argument of the target, in declaration order.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func recordArgument<Value>(_ argument: RemoteCallArgument<Value>) throws
```

##### Serialization Requirement

Implementations of this method must ensure that the `Value` type parameter conforms to the types’ `SerializationRequirement`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/distributed/distributedtargetinvocationencoder/recordargument(_:))*