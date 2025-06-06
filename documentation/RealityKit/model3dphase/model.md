# model

**Framework**: RealityKit  
**Kind**: property

The loaded model, if any.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var model: ResolvedModel3D? { get }
```

#### Discussion

If this value isn’t `nil`, the model load operation has finished, and you can use the model to update the view. You can use the model directly, or you can modify it in some way. For example, you can add a `ResolvedModel3D/resizable()` modifier to make the model resizable.

## See Also

- [var error: (any Error)?](model3dphase/error.md)
  The error that occurred when attempting to load a model, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/model3dphase/model)*