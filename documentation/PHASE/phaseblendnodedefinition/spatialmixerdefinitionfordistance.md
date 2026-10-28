# spatialMixerDefinitionForDistance

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

An object that combines spatial audio layers.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var spatialMixerDefinitionForDistance: PHASESpatialMixerDefinition? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) PHASESpatialMixerDefinition * spatialMixerDefinitionForDistance;
```

## Discussion

The framework sets this property to the [`init(spatialMixerDefinition:)`](./init%28spatialmixerdefinition%29.md) argument.

## See Also

### Accessing Blend Properties
- [var blendParameterDefinition: PHASENumberMetaParameterDefinition?](./blendparameterdefinition.md)
  The meta parameter definition that caps the blend range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseblendnodedefinition/spatialmixerdefinitionfordistance)*