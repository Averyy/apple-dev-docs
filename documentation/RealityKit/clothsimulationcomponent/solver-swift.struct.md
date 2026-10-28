# ClothSimulationComponent.Solver

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The permanent solver configuration of a cloth simulation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Solver
```

## Overview

The solver used for a simulation affects the quality, performance and power cost of the simulation.

## Topics

### Creating a solver
- [static func gaussSeidel(iterationCount: Int) -> ClothSimulationComponent.Solver](./solver-swift.struct/gaussseidel%28iterationcount%29.md)
  Gauss-Seidel solver for a cloth simulation.
- [static func jacobi(iterationCount: Int) -> ClothSimulationComponent.Solver](./solver-swift.struct/jacobi%28iterationcount%29.md)
  Jacobi solver for a cloth simulation.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the solver
- [var solver: ClothSimulationComponent.Solver](./solver-swift.property.md)
  The solver used by this simulation, configured at initialization and immutable thereafter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/solver-swift.struct)*