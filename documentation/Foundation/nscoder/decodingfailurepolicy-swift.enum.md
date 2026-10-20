# NSCoder.DecodingFailurePolicy

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NSDecodingFailurePolicy : NSInteger;
```

## Topics

### Failure Policies
- [NSCoder.DecodingFailurePolicy.raiseException](./decodingfailurepolicy-swift.enum/raiseexception.md)
  A failure policy that directs the coder to raise an exception.
- [NSCoder.DecodingFailurePolicy.setErrorAndReturn](./decodingfailurepolicy-swift.enum/seterrorandreturn.md)
  A failure policy that directs the coder to capture the failure as an error object.
### Initializers
- [init?(rawValue: Int)](./decodingfailurepolicy-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting a Coder
- [var allowsKeyedCoding: Bool](./allowskeyedcoding.md)
  A Boolean value that indicates whether the receiver supports keyed coding of objects.
- [func containsValue(forKey: String) -> Bool](./containsvalue%28forkey%29.md)
  Returns a Boolean value that indicates whether an encoded value is available for a string.
- [var decodingFailurePolicy: NSCoder.DecodingFailurePolicy](./decodingfailurepolicy-swift.property.md)
  The action the coder should take when decoding fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscoder/decodingfailurepolicy-swift.enum)*