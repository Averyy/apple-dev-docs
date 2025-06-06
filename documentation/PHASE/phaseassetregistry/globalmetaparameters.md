# globalMetaParameters

**Framework**: PHASE  
**Kind**: property

A dictionary of metaparameters that all sound event assets share.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var globalMetaParameters: [String : PHASEMetaParameter] { get }
```

#### Discussion

When you change a value for a metaparameter in this dictionary, every sound event attached to the metaparameter observes the change. The dictionary key is the [`identifier`](phasemetaparameter/identifier.md) of the [`PHASEMetaParameterDefinition`](phasemetaparameterdefinition.md) you pass into [`registerGlobalMetaParameter(metaParameterDefinition:)`](phaseassetregistry/registerglobalmetaparameter(metaparameterdefinition:).md).

> 💡 **Tip**:  To adjust a value for a single sound event, access the metaparameter through the [`metaParameters`](phasesoundevent/metaparameters.md) property instead.

 To adjust a value for a single sound event, access the metaparameter through the [`metaParameters`](phasesoundevent/metaparameters.md) property instead.

## See Also

- [func registerGlobalMetaParameter(metaParameterDefinition: PHASEMetaParameterDefinition) throws -> PHASEGlobalMetaParameterAsset](phaseassetregistry/registerglobalmetaparameter(metaparameterdefinition:).md)
  Registers a global metaparameter with the asset registry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseassetregistry/globalmetaparameters)*