# init(spatialMixerDefinition:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

Creates a blend node for spatial audio output.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(spatialMixerDefinition: PHASESpatialMixerDefinition)
```

```objc
- (instancetype) initDistanceBlendWithSpatialMixerDefinition:(PHASESpatialMixerDefinition *) spatialMixerDefinition;
```

## Parameters

- `spatialMixerDefinition`: An object that combines spatial audio layers.

## See Also

### Creating a Blend Node
- [init(blendMetaParameterDefinition: PHASENumberMetaParameterDefinition)](./init%28blendmetaparameterdefinition%29.md)
  Creates a blend node with a maxiumum blend range value.
- [convenience init(blendMetaParameterDefinition: PHASENumberMetaParameterDefinition, identifier: String)](./init%28blendmetaparameterdefinition,identifier%29.md)
  Creates a named blend node with a maxiumum blend range value.
- [convenience init(spatialMixerDefinition: PHASESpatialMixerDefinition, identifier: String)](./init%28spatialmixerdefinition,identifier%29.md)
  Creates a named blend node for spatial audio output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseblendnodedefinition/init(spatialmixerdefinition:))*