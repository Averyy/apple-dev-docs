# emitter::periodicBurst

**Framework**: ComputeGraph  
**Kind**: func

Emit a burst of particles periodically.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
void emitter::periodicBurst(float2 intervalRange, uint burstSize)
```

#### Discussion

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/820dd2a5b9077da2f0c820f55dd5c612/emitter__periodicBurst.svg)

> **Note**: Reads from emitter state `PeriodicEmitterState state`, if it exists

## Parameters

- `intervalRange`: Minimum/Maximum duration between spawns. After each burst, the interval before the next burst will be chosen randomly in this interval.
- `burstSize`: Number of particles to emit at system creation or reset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/emitter/periodicburst)*