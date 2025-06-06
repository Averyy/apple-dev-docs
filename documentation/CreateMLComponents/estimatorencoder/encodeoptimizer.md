# encodeOptimizer(_:)

**Framework**: Create ML Components  
**Kind**: method  
**Required**: Yes

Encodes an estimator optimizer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
mutating func encodeOptimizer<T>(_ value: T) throws where T : Encodable
```

#### Discussion

Optimizers are used when fitting an estimator and usually contain state information such as momentum. This method encodes the optimizer state separately from model parameters.

## See Also

- [func encode<T>(T) throws](estimatorencoder/encode(_:).md)
  Encodes a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/estimatorencoder/encodeoptimizer(_:))*