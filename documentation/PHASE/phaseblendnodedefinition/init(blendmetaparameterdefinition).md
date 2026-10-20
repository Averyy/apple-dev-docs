# init(blendMetaParameterDefinition:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

Creates a blend node with a maxiumum blend range value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(blendMetaParameterDefinition: PHASENumberMetaParameterDefinition)
```

```objc
- (instancetype) initWithBlendMetaParameterDefinition:(PHASENumberMetaParameterDefinition *) blendMetaParameterDefinition;
```

## Parameters

- `blendMetaParameterDefinition`: A maximum value for the blend range. The sound event’s blend meta parameter across a range from `0` to this value produces an active cross-fade along the child nodes.

## See Also

### Creating a Blend Node
- [convenience init(blendMetaParameterDefinition: PHASENumberMetaParameterDefinition, identifier: String)](./init%28blendmetaparameterdefinition,identifier%29.md)
  Creates a named blend node with a maxiumum blend range value.
- [init(spatialMixerDefinition: PHASESpatialMixerDefinition)](./init%28spatialmixerdefinition%29.md)
  Creates a blend node for spatial audio output.
- [convenience init(spatialMixerDefinition: PHASESpatialMixerDefinition, identifier: String)](./init%28spatialmixerdefinition,identifier%29.md)
  Creates a named blend node for spatial audio output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseblendnodedefinition/init(blendmetaparameterdefinition:))*