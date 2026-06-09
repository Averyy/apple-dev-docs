# auxiliaryPlanes

**Framework**: Metal  
**Kind**: property

The auxiliary planes that this tensor reference requires.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var auxiliaryPlanes: [MTLTensorAuxiliaryPlaneType] { get }
```

#### Discussion

Returns an array of [`MTLTensorAuxiliaryPlaneType`](mtltensorauxiliaryplanetype.md) objects describing each auxiliary plane the shader expects. Empty if the tensor has no auxiliary planes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorreferencetype/auxiliaryplanes)*