# init(blendMetaParameterDefinition:identifier:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

Creates a named blend node with a maxiumum blend range value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(blendMetaParameterDefinition: PHASENumberMetaParameterDefinition, identifier: String)
```

```objc
- (instancetype) initWithBlendMetaParameterDefinition:(PHASENumberMetaParameterDefinition *) blendMetaParameterDefinition identifier:(NSString *) identifier;
```

## Parameters

- `blendMetaParameterDefinition`: A maximum value for the blend range. The sound event’s blend meta parameter across a range from `0` to this value produces an active cross-fade along the child nodes.
- `identifier`: A unique name for the blend node.

## See Also

### Creating a Blend Node
- [init(blendMetaParameterDefinition: PHASENumberMetaParameterDefinition)](./init%28blendmetaparameterdefinition%29.md)
  Creates a blend node with a maxiumum blend range value.
- [init(spatialMixerDefinition: PHASESpatialMixerDefinition)](./init%28spatialmixerdefinition%29.md)
  Creates a blend node for spatial audio output.
- [convenience init(spatialMixerDefinition: PHASESpatialMixerDefinition, identifier: String)](./init%28spatialmixerdefinition,identifier%29.md)
  Creates a named blend node for spatial audio output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseblendnodedefinition/init(blendmetaparameterdefinition:identifier:))*