# lifetime

**Framework**: Compute Graph  
**Kind**: property

The initial lifetime of the particle in seconds.

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
var lifetime: Float { get set }
```

#### Discussion

This determines how long the particle will exist before being automatically removed from the simulation. A value of 0 or negative means the particle will be removed immediately or never spawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/elementspawnparameters/lifetime)*