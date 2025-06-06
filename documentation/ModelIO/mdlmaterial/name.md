# name

**Framework**: Model I/O  
**Kind**: property

A descriptive name for the material.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var name: String { get set }
```

#### Discussion

This name isn’t used in rendering, but it can be useful for debugging and organizing the materials used in a project. When you load materials from an asset file with the [`MDLAsset`](mdlasset.md) class, Model I/O uses names assigned in the asset file where supported by the file format.

## See Also

- [var materialFace: MDLMaterialFace](mdlmaterial/materialface.md)
  The surface of an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmaterial/name)*