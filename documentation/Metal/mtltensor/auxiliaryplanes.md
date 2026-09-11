# auxiliaryPlanes

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The auxiliary planes of this tensor.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var auxiliaryPlanes: [any MTLTensorAuxiliaryPlane] { get }
```

#### Discussion

Returns an array of [`MTLTensorAuxiliaryPlane`](mtltensorauxiliaryplane.md) objects describing each auxiliary plane configured on this tensor. For single-plane tensors, this array is empty.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensor/auxiliaryplanes)*