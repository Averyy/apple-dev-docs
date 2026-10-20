# BNNS.RandomGeneratorMethod

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

Constants that describe random number generation methods.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
enum RandomGeneratorMethod
```

## Topics

### Random Number Generation Methods
- [BNNS.RandomGeneratorMethod.aesCtr](./randomgeneratormethod/aesctr.md)
  A constant that specifes an implementation that’s based on the Advanced Encryption Standard (AES) hash of a counter.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Creating a Random Number Generator
- [init?(method: BNNS.RandomGeneratorMethod, seed: UInt64?, filterParameters: BNNSFilterParameters?)](./randomgenerator/init%28method,seed,filterparameters%29.md)
  Returns a new random number generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/randomgeneratormethod)*