# init(method:seed:filterParameters:)

**Framework**: Accelerate  
**Kind**: init

Returns a new random number generator.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
init?(method: BNNS.RandomGeneratorMethod, seed: UInt64? = nil, filterParameters: BNNSFilterParameters? = nil)
```

## Parameters

- `method`: The random number generation method.
- `seed`: An optional unsigned integer value the function uses to initialize the random number generator.
- `filterParameters`: The runtime filter parameters.

## See Also

- [BNNS.RandomGeneratorMethod](bnns/randomgeneratormethod.md)
  Constants that describe random number generation methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/randomgenerator/init(method:seed:filterparameters:))*