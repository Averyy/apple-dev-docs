# random::integer_using

**Framework**: ComputeGraph  
**Kind**: func

Generates a pseudo-random 32-bit unsigned integer using a specific seed.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
uint random::integer_using(uint seed)
```

#### Return Value

A pseudo-random 32-bit unsigned integer.

#### Discussion

This function generates a random integer covering the full range of 32-bit unsigned values using the provided seed. The seed is not modified, allowing for reproducible random number generation. Use this when you need deterministic randomness or want to control the random sequence independently.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/cb7024e4bcc2bae32639fe217885d7d3/random__integer_using.svg)

## Parameters

- `seed`: The seed value to use for random number generation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/random/integer_using)*