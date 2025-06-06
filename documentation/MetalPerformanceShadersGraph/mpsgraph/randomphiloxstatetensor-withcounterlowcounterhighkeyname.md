# randomPhiloxStateTensor(withCounterLow:counterHigh:key:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a tensor representing state using the Philox algorithm with given counter and key values.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func randomPhiloxStateTensor(withCounterLow counterLow: Int, counterHigh: Int, key: Int, name: String?) -> MPSGraphTensor
```

#### Return Value

An MPSGraphTensor representing a random state, to be passed as an input to a random op.

#### Discussion

See randomPhiloxStateTensorWithSeed.

## Parameters

- `counterLow`: The value to initilaize lower 64 bits of counter to. Philox utilizes a 128 bit counter
- `counterHigh`: The value to initilaize upper 64 bits of counter to. Philox utilizes a 128 bit counter
- `key`: The value to initialize the key to in Philox algorithm.
- `name`: Name for the operation


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/randomphiloxstatetensor(withcounterlow:counterhigh:key:name:))*