# PHASEGlobalMetaParameterAsset

**Framework**: PHASE  
**Kind**: class

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

#### Overview

The engine’s [`registerGlobalMetaParameter(metaParameterDefinition:)`](phaseassetregistry/registerglobalmetaparameter(metaparameterdefinition:).md) function returns an instance of this class for a parameter you register. Then, you access the actual metaparameter by using this class’s [`identifier`](phaseasset/identifier.md) as the key for metaparameter dictionary, for example, a sound event’s [`metaParameters`](phasesoundevent/metaparameters.md) or the asset registry’s [`globalMetaParameters`](phaseassetregistry/globalmetaparameters.md).

As an opaque derived object, this class adds no properties to the subclass.

## Relationships

### Inherits From
- [PHASEAsset](phaseasset.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASEMetaParameter](phasemetaparameter.md)
  A named parameter with a value that the app can change over time.
- [class PHASEMetaParameterDefinition](phasemetaparameterdefinition.md)
  A specification for a named parameter with a constant value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseglobalmetaparameterasset)*