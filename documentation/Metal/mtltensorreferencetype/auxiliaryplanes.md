# auxiliaryPlanes

**Framework**: Metal  
**Kind**: property

The auxiliary planes that this tensor reference requires.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var auxiliaryPlanes: [MTLTensorAuxiliaryPlaneType] { get }
```

#### Discussion

Returns an array of [`MTLTensorAuxiliaryPlaneType`](mtltensorauxiliaryplanetype.md) objects describing each auxiliary plane the shader expects. Empty if the tensor has no auxiliary planes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorreferencetype/auxiliaryplanes)*