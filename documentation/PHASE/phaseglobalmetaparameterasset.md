# PHASEGlobalMetaParameterAsset

**Framework**: PHASE  
**Kind**: class  
**Role**: Class

A reference to a registered metaparameter that the app can share with multiple sound events or sources.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEGlobalMetaParameterAsset
```

```objc
@interface PHASEGlobalMetaParameterAsset : PHASEAsset
```

#### Overview

The engine’s [`registerGlobalMetaParameter(metaParameterDefinition:)`](./phaseassetregistry/registerglobalmetaparameter%28metaparameterdefinition%29.md) function returns an instance of this class for a parameter you register. Then, you access the actual metaparameter by using this class’s [`identifier`](./phaseasset/identifier.md) as the key for metaparameter dictionary, for example, a sound event’s [`metaParameters`](./phasesoundevent/metaparameters.md) or the asset registry’s [`globalMetaParameters`](./phaseassetregistry/globalmetaparameters.md).

As an opaque derived object, this class adds no properties to the subclass.

## Relationships

### Inherits From
- [PHASEAsset](./phaseasset.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Base Metaparameters
- [class PHASEMetaParameter](./phasemetaparameter.md)
  A named parameter with a value that the app can change over time.
- [class PHASEMetaParameterDefinition](./phasemetaparameterdefinition.md)
  A specification for a named parameter with a constant value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseglobalmetaparameterasset)*