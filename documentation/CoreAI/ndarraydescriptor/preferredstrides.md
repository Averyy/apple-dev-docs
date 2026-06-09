# preferredStrides

**Framework**: Core AI  
**Kind**: property

The strides that avoid data layout transformations during inference.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var preferredStrides: [Int] { get }
```

#### Discussion

During the specialization of an [`AIModel`](aimodel.md), a preferred memory layout for a given ndArray value may be set depending on structure of the model and which compute units it is specialized for. In some cases, this can result in a non-contiguous layout being preferred/required by the backing compute. In such case, you are still able to provide `InferenceFunction.run` normal contiguous ndArray values, however it may incur a copy to the preferred layout. As such, this property provides an opportunity for you to optimize performance by creating your source ndArray value with the preferred striding and avoiding that copy.

> **Note**: Constructing an ndArray with these preferred strides may result in a non-contiguous layout. In such case calling `ndArrayView.contiguousElements` on a view of the ndArray will return `nil`. If you choose to use the preferred strides, you must read/write the resulting ndArray by dynamically respecting whatever strides are returned:

```swift
guard case .ndArray(let inputDescriptor) = inferenceFunctionDescriptor.inputDescriptor(of: "input") else {
  throw UnexpectedInferenceValueType()
}
let preferredStrides = inputDescriptor.preferredStrides
var ndArray = NDArray(shape: [theShape], scalarType: .float32, strides: preferredStrides)
var view = ndArray.mutableView(as: Float.self)
if let contiguousElements = view.contiguousElements {
  // The preferred strides were a normal contiguous layout
} else {
  // The preferred strides were non-contiguous
  view.withUnsafeMutablePointer { data, shape, strides in
    ... logic which respects whatever strides were preferred ...
  }
}
```

> **Note**: Accessing this property on a descriptor for which `hasDynamicShape` is true, is a programming error. If the descriptor has a dynamic shape, you must first call `resolvingDynamicDimensions` to provide a concrete size for each dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarraydescriptor/preferredstrides)*