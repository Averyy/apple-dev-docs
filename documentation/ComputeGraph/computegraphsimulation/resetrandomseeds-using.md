# resetRandomSeeds(using:)

**Framework**: Compute Graph  
**Kind**: method

Resets random seeds using the provided randomness function.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro ?+

## Declaration

```swift
final func resetRandomSeeds(using randomness: () -> UInt32)
```

#### Discussion

`randomness` will be called multiple times, for each of seeds used by the simulation


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/resetrandomseeds(using:))*