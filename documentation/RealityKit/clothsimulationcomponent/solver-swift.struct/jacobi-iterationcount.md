# jacobi(iterationCount:)

**Framework**: RealityKit  
**Kind**: method

Jacobi solver for a cloth simulation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func jacobi(iterationCount: Int = 1) -> ClothSimulationComponent.Solver
```

#### Return Value

A Jacobi solver configuration.

#### Discussion

The Jacobi solver can be faster and more power efficient than Gauss-Seidel, especially if the number of particles in your simulation is low. However, the Jacobi solver has a slower convergence than Gauss-Seidel, so when used with the same number of iterations we can expect bigger errors in the simulation.

Before considering changing the solver to improve performance or power consumption, we recommend playing around with other parameters in your scene. For example:

- Reducing the number of vertices, and making sure triangles are as regular as possible in edge length across all bodies in the simulation.
- If possible, replace cloth mesh colliders with implicit colliders like spheres, boxes, etc.
- Set the Laplacian damping of all bodies to zero.
- Set [`crossTetherStiffness`](clothbodymaterial/crosstetherstiffness.md) and [`bendStiffness`](clothbodymaterial/bendstiffness.md) to zero for all the bodies.

But if you need to improve performance and you think you can tolerate even a bit more stretching in your bodies, you can experiment with Jacobi. Always take actual performance measurements when doing performance-related changes, as the impact of different approaches may vary greatly depending on your specific scene.

## Parameters

- `iterationCount`: The number of solver iterations to perform per time step.

## See Also

- [static func gaussSeidel(iterationCount: Int) -> ClothSimulationComponent.Solver](clothsimulationcomponent/solver-swift.struct/gaussseidel(iterationcount:).md)
  Gauss-Seidel solver for a cloth simulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/clothsimulationcomponent/solver-swift.struct/jacobi(iterationcount:))*