# resolvingDynamicDimensions(_:)

**Framework**: Core AI  
**Kind**: method

Returns a new descriptor with all dynamic dimensions replaced by concrete values.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func resolvingDynamicDimensions(_ newShape: [Int]) -> NDArrayDescriptor
```

#### Discussion

If the original model contained ndArray arguments with dynamic shapes, then the `NDArrayDescriptor` returned for that argument from the `InferenceFunctionDescriptor` will contain the value `-1` in the dimensions with dynamic sizes.

This method allows you to provide a resolved shape and obtain a new descriptor with that adjusted shape.

```swift
let functionDescriptor = model.functionDescriptor(for: "main")
guard case .ndArray(let ndArrayDescriptor) = functionDescriptor.inputDescriptor(of: "dynamic_shape_input") else {
  // Handle input not found or not ndArray
}

// The 'dynamic_shape_input' argument is a rank 3 ndArray with a dynamic shape for the final dimension.
// ndArrayDescriptor.shape == [128, 128, -1]

// Make a resolved descriptor which fills in the -1 dimension with the concrete value 10
let resolvedDescriptor = ndArrayDescriptor.resolvingDynamicDimensions([128, 128, 10])
```

> **Note**: `newShape` must be the same size as the `shape` of the descriptor it is called on. Also for each dimension, it must hold true that the provided new shape either matches the existing shape, or the existing shape is `-1`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarraydescriptor/resolvingdynamicdimensions(_:))*