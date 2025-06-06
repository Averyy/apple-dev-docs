# Model3DPhase

**Framework**: RealityKit  
**Kind**: enum

The current phase of the asynchronous model loading operation.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
enum Model3DPhase
```

#### Overview

When you create a [`Model3D`](model3d.md) instance with the [`init(url:transaction:content:)`](model3d/init(url:transaction:content:).md) or `Model3D/init(named:transaction:content:)` initializers, you define the appearance of the view using a `content` closure. [`Model3D`](model3d.md) calls the closure with a phase value at different points during the load operation to indicate the current state. Use the phase to decide what to display. For example, you can display the loaded model if it exists, a view that indicates an error, or a placeholder:

```swift
let url = URL(string: "https://example.com/robot.usdz")!
Model3D(url: url) { phase in
    if let model = phase.model {
        model // Displays the loaded model.
    } else if phase.error != nil {
        Color.red // Indicates an error.
    } else {
        ProgressView()
    }
}
```

## Topics

### Accessing the model
- [var model: ResolvedModel3D?](model3dphase/model.md)
  The loaded model, if any.
- [var error: (any Error)?](model3dphase/error.md)
  The error that occurred when attempting to load a model, if any.
### Obtaining the result
- [Model3DPhase.empty](model3dphase/empty.md)
  No model is loaded.
- [case success(ResolvedModel3D)](model3dphase/success(_:).md)
  A model has succesfully loaded.
- [Model3DPhase.failure(_:)](model3dphase/failure(_:).md)
  An model failed to load with an error.

## See Also

- [struct Model3D](model3d.md)
  A view that asynchronously loads and displays a 3D model.
- [struct ResolvedModel3D](resolvedmodel3d.md)
  A view for displaying static three-dimensional models.
- [struct Model3DPlaceholderContent](model3dplaceholdercontent.md)
  A container view that presents either a 3D model or a placeholder for one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3dphase)*