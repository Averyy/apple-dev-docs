# lifetime

**Framework**: Compute Graph  
**Kind**: property

The initial lifetime of the particle in seconds.

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
var lifetime: Float { get set }
```

#### Discussion

This determines how long the particle will exist before being automatically removed from the simulation. A value of 0 or negative means the particle will be removed immediately or never spawn.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/elementspawnparameters/lifetime)*