# particleLifetimeRange

**Framework**: SpriteKit  
**Kind**: property

The range of allowed random values for a particle’s lifetime.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
@MainActor
var particleLifetimeRange: CGFloat { get set }
```

#### Discussion

The default value is `0.0`. If non-zero, the lifetime of each particle is randomly determined and may vary by plus or minus half of the range value.

## See Also

- [var particleLifetime: CGFloat](skemitternode/particlelifetime.md)
  The average lifetime of a particle, in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode/particlelifetimerange)*