# emitter::continuous

**Framework**: ComputeGraph  
**Kind**: func

Continuously emit particles at a fixed rate.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
void emitter::continuous(float rate, float maxBurst)
```

#### Discussion

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/ba1078030d9b378f614f1a229ce01630/emitter__continuous.svg)

> **Note**: Reads from emitter state `ContinuousEmitterState state`, if it exists

## Parameters

- `rate`: Number of particles per second to emit. If this value results in a fractional number of particles to emit in a given frame, the remainder will be carried into the next frame.
- `maxBurst`: Maximum number of particles to emit in a single frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/emitter/continuous)*