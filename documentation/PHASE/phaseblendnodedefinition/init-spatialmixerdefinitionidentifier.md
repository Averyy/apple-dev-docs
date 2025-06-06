# init(spatialMixerDefinition:identifier:)

**Framework**: PHASE  
**Kind**: init

Creates a named blend node for spatial audio output.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(spatialMixerDefinition: PHASESpatialMixerDefinition, identifier: String)
```

## Parameters

- `spatialMixerDefinition`: An object that combines spatial audio layers.
- `identifier`: A unique name for the node.

## See Also

- [init(blendMetaParameterDefinition: PHASENumberMetaParameterDefinition)](phaseblendnodedefinition/init(blendmetaparameterdefinition:).md)
  Creates a blend node with a maxiumum blend range value.
- [convenience init(blendMetaParameterDefinition: PHASENumberMetaParameterDefinition, identifier: String)](phaseblendnodedefinition/init(blendmetaparameterdefinition:identifier:).md)
  Creates a named blend node with a maxiumum blend range value.
- [init(spatialMixerDefinition: PHASESpatialMixerDefinition)](phaseblendnodedefinition/init(spatialmixerdefinition:).md)
  Creates a blend node for spatial audio output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseblendnodedefinition/init(spatialmixerdefinition:identifier:))*