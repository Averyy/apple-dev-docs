# globalMetaParameters

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (atomic, copy, readonly) NSDictionary<NSString *,PHASEMetaParameter *> * globalMetaParameters;
```

## Discussion

When you change a value for a metaparameter in this dictionary, every sound event attached to the metaparameter observes the change. The dictionary key is the [`identifier`](../phasemetaparameter/identifier.md) of the [`PHASEMetaParameterDefinition`](../phasemetaparameterdefinition.md) you pass into [`registerGlobalMetaParameter(metaParameterDefinition:)`](./registerglobalmetaparameter%28metaparameterdefinition%29.md).

> 💡 **Tip**:  To adjust a value for a single sound event, access the metaparameter through the [`metaParameters`](../phasesoundevent/metaparameters.md) property instead.

## See Also

### Registering Global Metaparameters
- [func registerGlobalMetaParameter(metaParameterDefinition: PHASEMetaParameterDefinition) throws -> PHASEGlobalMetaParameterAsset](./registerglobalmetaparameter%28metaparameterdefinition%29.md)
  Registers a global metaparameter with the asset registry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseassetregistry/globalmetaparameters)*