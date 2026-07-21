# auxiliaryPlanes

**Framework**: Metal  
**Kind**: property

The auxiliary plane configurations for this tensor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var auxiliaryPlanes: MTLTensorAuxiliaryPlaneDescriptorMap? { get set }
```

#### Discussion

Set this property with a populated [`MTLTensorAuxiliaryPlaneDescriptorMap`](mtltensorauxiliaryplanedescriptormap.md) to create a multi-plane tensor. When `nil`, the tensor has only a data plane.

Multi-plane tensors do not support [`machineLearning`](mtltensorusage/machinelearning.md). Use [`compute`](mtltensorusage/compute.md) or [`render`](mtltensorusage/render.md).

Multi-plane tensors do not support data types larger than one byte as the data plane type.

Multi-plane tensors do not support rank zero.

The default value is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensordescriptor/auxiliaryplanes)*