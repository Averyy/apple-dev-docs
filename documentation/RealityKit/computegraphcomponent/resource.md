# resource

**Framework**: RealityKit  
**Kind**: property

The compute graph resource that defines the simulation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var resource: ComputeGraphResource? { get set }
```

#### Discussion

Assigning a new resource replaces the current graph and resets the simulation. Set to `nil` to detach the resource without destroying the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphcomponent/resource)*