# blendParameterDefinition

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

The meta parameter definition that caps the blend range.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var blendParameterDefinition: PHASENumberMetaParameterDefinition? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) PHASENumberMetaParameterDefinition * blendParameterDefinition;
```

#### Discussion

The framework sets the value of this property to the [`init(blendMetaParameterDefinition:)`](./init%28blendmetaparameterdefinition%29.md) argument.

## See Also

### Accessing Blend Properties
- [var spatialMixerDefinitionForDistance: PHASESpatialMixerDefinition?](./spatialmixerdefinitionfordistance.md)
  An object that combines spatial audio layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseblendnodedefinition/blendparameterdefinition)*