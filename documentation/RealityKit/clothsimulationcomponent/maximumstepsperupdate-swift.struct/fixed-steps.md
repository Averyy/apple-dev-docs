# fixed(steps:)

**Framework**: RealityKit  
**Kind**: method

A fixed maximum number of steps per update is manually configured.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func fixed(steps: Int) -> ClothSimulationComponent.MaximumStepsPerUpdate
```

#### Return Value

A fixed maximum-steps-per-update configuration.

## Parameters

- `steps`: The maximum number of time steps to process per update. Clamped to a minimum of 1.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/maximumstepsperupdate-swift.struct/fixed(steps:))*