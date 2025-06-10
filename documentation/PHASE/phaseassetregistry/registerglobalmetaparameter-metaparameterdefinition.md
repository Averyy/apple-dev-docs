# registerGlobalMetaParameter(metaParameterDefinition:)

**Framework**: PHASE  
**Kind**: method

Registers a global metaparameter with the asset registry.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func registerGlobalMetaParameter(metaParameterDefinition: PHASEMetaParameterDefinition) throws -> PHASEGlobalMetaParameterAsset
```

#### Return Value

A global metaparameter object. If an error occurs, the function returns `nil`.

#### Discussion

Global metaparameters attach to any number of sound event assets. When an app adjusts a global metaparameter at runtime, the change propagates immediately to all the attached sound events.

> **Note**:  Although you register a global metaparameter definition ([`PHASEMetaParameterDefinition`](phasemetaparameterdefinition.md)) with this function, you receive a global metaparameter instance ([`PHASEMetaParameter`](phasemetaparameter.md)) when you access the parameter by its [`identifier`](phasemetaparameter/identifier.md) using the [`globalMetaParameters`](phaseassetregistry/globalmetaparameters.md) dictionary.

## Parameters

- `metaParameterDefinition`: A single parameter that controls the value of multiple parameters.

## See Also

- [var globalMetaParameters: [String : PHASEMetaParameter]](phaseassetregistry/globalmetaparameters.md)
  A dictionary of metaparameters that all sound event assets share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseassetregistry/registerglobalmetaparameter(metaparameterdefinition:))*