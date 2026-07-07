# random::seed

**Framework**: Compute Graph  
**Kind**: func

Returns the current random seed, without incrementing it.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
uint random::seed()
```

#### Return Value

The current random seed as a 32-bit unsigned integer.

#### Discussion

This function retrieves the current state of the random number generator’s seed without modifying it, allowing you to inspect or save the seed value for later use.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/91c98126b197b5911014ad52ab35dd01/random__seed.svg)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/random/seed)*