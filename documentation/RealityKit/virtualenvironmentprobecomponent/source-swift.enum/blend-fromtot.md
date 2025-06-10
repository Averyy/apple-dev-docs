# VirtualEnvironmentProbeComponent.Source.blend(from:to:t:)

**Framework**: RealityKit  
**Kind**: case

A source that blends between two pregenerated probes based on the provided blend factor.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
case blend(from: VirtualEnvironmentProbeComponent.Probe, to: VirtualEnvironmentProbeComponent.Probe, t: Float)
```

#### Discussion

The blend factor is in the range `[0.0, 1.0]` where a value of `0.0` uses only the first probe, and `1.0` uses only the second probe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/virtualenvironmentprobecomponent/source-swift.enum/blend(from:to:t:))*