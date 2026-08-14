# emitter::periodicBurst

**Framework**: Compute Graph  
**Kind**: func

Emit a burst of particles periodically.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
void emitter::periodicBurst(float2 intervalRange, uint burstSize)
```

#### Discussion

> **Note**: ![Graph](/images/com.apple.computegraph/emitter__periodicBurst.svg)

> **Note**: Reads from emitter state `PeriodicEmitterState state`, if it exists

## Parameters

- `intervalRange`: Minimum/Maximum duration between spawns. After each burst, the interval before the next burst will be chosen randomly in this interval.
- `burstSize`: Number of particles to emit at system creation or reset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/emitter/periodicburst)*