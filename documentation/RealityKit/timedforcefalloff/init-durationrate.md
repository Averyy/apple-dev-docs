# init(duration:rate:)

**Framework**: RealityKit  
**Kind**: init

Creates a timed force falloff.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
init(duration: TimeInterval, rate: Double = 1.0)
```

#### Discussion

- When the rate is , no falloff occurs. (Rigid bodies outside the bounds are culled.)
- When the rate is , falloff occurs slower and is sublinear.
- When the rate is , falloff is linear.
- When the rate is , falloff occurs faster and is nonlinear.

## Parameters

- `duration`: The lifetime of the effect in seconds.
- `rate`: Controls how fast or slow falloff occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/timedforcefalloff/init(duration:rate:))*