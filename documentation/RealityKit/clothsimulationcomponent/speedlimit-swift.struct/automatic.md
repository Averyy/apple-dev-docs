# automatic

**Framework**: RealityKit  
**Kind**: property

Automatically configured speed limit, which limits particle displacement per time step to reduce self-collision tunneling. The limit is proportionate to the particle density of the simulation; a higher density produces a more aggressive speed cap.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static var automatic: ClothSimulationComponent.SpeedLimit { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/speedlimit-swift.struct/automatic)*