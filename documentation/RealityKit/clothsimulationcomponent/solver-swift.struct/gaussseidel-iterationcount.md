# gaussSeidel(iterationCount:)

**Framework**: RealityKit  
**Kind**: method

Gauss-Seidel solver for a cloth simulation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func gaussSeidel(iterationCount: Int = 1) -> ClothSimulationComponent.Solver
```

#### Return Value

A Gauss-Seidel solver configuration.

#### Discussion

This is the default solver. It provides the best trade-off between accuracy and performance in most cases.

## Parameters

- `iterationCount`: The number of solver iterations to perform per time step.

## See Also

- [static func jacobi(iterationCount: Int) -> ClothSimulationComponent.Solver](clothsimulationcomponent/solver-swift.struct/jacobi(iterationcount:).md)
  Jacobi solver for a cloth simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/solver-swift.struct/gaussseidel(iterationcount:))*