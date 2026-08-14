# random::integer_using

**Framework**: Compute Graph  
**Kind**: func

Generates a pseudo-random 32-bit unsigned integer using a specific seed.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
uint random::integer_using(uint seed)
```

#### Return Value

A pseudo-random 32-bit unsigned integer.

#### Discussion

This function generates a random integer covering the full range of 32-bit unsigned values using the provided seed. The seed is not modified, allowing for reproducible random number generation. Use this when you need deterministic randomness or want to control the random sequence independently.

> **Note**: ![Graph](/images/com.apple.computegraph/random__integer_using.svg)

## Parameters

- `seed`: The seed value to use for random number generation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/random/integer_using)*