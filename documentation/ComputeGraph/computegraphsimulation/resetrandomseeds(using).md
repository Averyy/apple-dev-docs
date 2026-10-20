# resetRandomSeeds(using:)

**Framework**: Compute Graph  
**Kind**: method

Resets random seeds using the provided randomness function.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro ?+

## Declaration

```swift
final func resetRandomSeeds(using randomness: () -> UInt32)
```

#### Discussion

`randomness` will be called multiple times, for each of seeds used by the simulation


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/resetrandomseeds(using:))*