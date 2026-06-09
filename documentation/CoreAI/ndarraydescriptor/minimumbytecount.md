# minimumByteCount

**Framework**: Core AI  
**Kind**: property

The minimum number of bytes needed for storage with this descriptor’s shape and preferred strides.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var minimumByteCount: Int { get }
```

#### Discussion

The shape/strides/scalarType of this descriptor are used to compute the addressable byte range of the layout, and the size of that range is returned as the minimum size a backing storage would need to be to contain the ndArray.

In most cases it is preferred to make `NDArray` instances which handle creating the allocations for you, but in circumstances where you need to manually handle your allocations, this property can be useful to help you find how large of a storage to allocate.

```swift
let metalDevice: any MTLDevice = ...
let functionDescriptor = model.functionDescriptor(for: "main")
guard case .ndArray(let ndArrayDescriptor) = functionDescriptor.inputDescriptor(of: "dynamic_shape_input") else {
  // Handle input not found or not ndArray
}

// Assuming that the descriptor is known to have static shapes. If it had dynamic shapes it'd be
// required to first call `resolvingDynamicDimensions`.
let byteCount = ndArrayDescriptor.minimumByteCount
let metalBuffer = metalDevice.makeBuffer(length: byteCount)!

// Later at inference time... manual allocations can be provided by making views from them.
let view = NDArray.RawView(
  metalBuffer: metalBuffer,
  byteOffset: 0,
  shape: ndArrayDescriptor.shape,
  scalarType: ndArrayDescriptor.scalarType,
  strides: ndArrayDescriptor.preferredStrides
)
var inputs = InferenceFunction.Inputs()
inputs.insert(view, for: "myInput")
var outputs = inferenceFunction.run(inputs: inputs)
```

`hasDynamicShape` must be false when accessing this property, as the size is unknown if there are dynamic shapes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarraydescriptor/minimumbytecount)*