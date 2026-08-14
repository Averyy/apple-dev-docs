# ClothSimulationComponent.Solver

**Framework**: RealityKit  
**Kind**: struct

The permanent solver configuration of a cloth simulation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Solver
```

#### Overview

The solver used for a simulation affects the quality, performance and power cost of the simulation.

## Topics

### Creating a solver
- [static func gaussSeidel(iterationCount: Int) -> ClothSimulationComponent.Solver](clothsimulationcomponent/solver-swift.struct/gaussseidel(iterationcount:).md)
  Gauss-Seidel solver for a cloth simulation.
- [static func jacobi(iterationCount: Int) -> ClothSimulationComponent.Solver](clothsimulationcomponent/solver-swift.struct/jacobi(iterationcount:).md)
  Jacobi solver for a cloth simulation.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var solver: ClothSimulationComponent.Solver](clothsimulationcomponent/solver-swift.property.md)
  The solver used by this simulation, configured at initialization and immutable thereafter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/solver-swift.struct)*