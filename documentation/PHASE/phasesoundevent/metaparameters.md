# metaParameters

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

The object’s meta parameters.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var metaParameters: [String : PHASEMetaParameter] { get }
```

```objc
@property (copy, readonly) NSDictionary<NSString *,PHASEMetaParameter *> * metaParameters;
```

#### Discussion

Each meta parameter contained in this dictionary affects only the sound event instance when you change the parameter’s value at runtime. As a read-only dictionary, the framework sets the contents based on the parameter you pass into a node definition initializer, for example, [`init(switchMetaParameterDefinition:)`](../phaseswitchnodedefinition/init%28switchmetaparameterdefinition%29.md). The dictionary key is the [`identifier`](../phasemetaparameter/identifier.md) of the source [`PHASEMetaParameterDefinition`](../phasemetaparameterdefinition.md).

> 💡 **Tip**:  To propagate a metaparameter change to multiple sound events instead of just one, register the metaparameter globally by calling [`registerGlobalMetaParameter(metaParameterDefinition:)`](../phaseassetregistry/registerglobalmetaparameter%28metaparameterdefinition%29.md). To change its value, access the metaparameter through the asset registry’s [`globalMetaParameters`](../phaseassetregistry/globalmetaparameters.md) dictionary instead.

## See Also

### Configuring Mixers and Metaparameters
- [var mixers: [String : PHASEMixer]](./mixers.md)
  Nodes in the event tree that control the volume of their child nodes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/metaparameters)*