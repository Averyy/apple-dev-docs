# UnlitMaterial.Program.Descriptor

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that specifies all parameters necessary to initialize `UnlitMaterial` programs

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct Descriptor
```

## Topics

### Initializers
- [init()](./descriptor-swift.struct/init%28%29.md)
### Instance Properties
- [var applyPostProcessToneMap: Bool](./descriptor-swift.struct/applypostprocesstonemap.md)
  A Boolean value that determines whether RealityKit will tonemap the output of this material.
- [var blendMode: MaterialParameterTypes.BlendMode?](./descriptor-swift.struct/blendmode.md)
  Modes that describe how materials using the created `UnlitMaterial.Program` will be blended with content behind them.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/unlitmaterial/program-swift.class/descriptor-swift.struct)*