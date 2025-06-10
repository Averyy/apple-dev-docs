# NSCoder.DecodingFailurePolicy

**Framework**: Foundation  
**Kind**: enum

Policies describing the action the coder should take when encountering decode failures.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum DecodingFailurePolicy
```

## Topics

### Failure Policies
- [NSCoder.DecodingFailurePolicy.raiseException](nscoder/decodingfailurepolicy-swift.enum/raiseexception.md)
  A failure policy that directs the coder to raise an exception.
- [NSCoder.DecodingFailurePolicy.setErrorAndReturn](nscoder/decodingfailurepolicy-swift.enum/seterrorandreturn.md)
  A failure policy that directs the coder to capture the failure as an error object.
- [NSCoder.DecodingFailurePolicy.raiseException](nscoder/decodingfailurepolicy-swift.enum/raiseexception.md)
  A failure policy that directs the coder to raise an exception.
- [NSCoder.DecodingFailurePolicy.setErrorAndReturn](nscoder/decodingfailurepolicy-swift.enum/seterrorandreturn.md)
  A failure policy that directs the coder to capture the failure as an error object.
### Initializers
- [init?(rawValue: Int)](nscoder/decodingfailurepolicy-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var allowsKeyedCoding: Bool](nscoder/allowskeyedcoding.md)
  A Boolean value that indicates whether the receiver supports keyed coding of objects.
- [func containsValue(forKey: String) -> Bool](nscoder/containsvalue(forkey:).md)
  Returns a Boolean value that indicates whether an encoded value is available for a string.
- [var decodingFailurePolicy: NSCoder.DecodingFailurePolicy](nscoder/decodingfailurepolicy-swift.property.md)
  The action the coder should take when decoding fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodingfailurepolicy-swift.enum)*