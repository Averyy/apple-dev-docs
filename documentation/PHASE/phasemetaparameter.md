# PHASEMetaParameter

**Framework**: PHASE  
**Kind**: class  
**Role**: Class

A named parameter with a value that the app can change over time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEMetaParameter
```

```objc
@interface PHASEMetaParameter : NSObject
```

#### Overview

Instances of this class provide an app with dynamic control of a sound’s properties. A metaparameter takes a single value as input and may operate on one or more audio characteristics.

To change the value of a metaparameter at runtime:

- Assign a string to a textual metaparameter’s [`value`](./phasemetaparameter/value.md).
- Adjust the value of a number or mapped metaparameter gradually over a duration by calling [`fade(value:duration:)`](./phasenumbermetaparameter/fade%28value,duration%29.md).

## Topics

### Accessing the Value
- [var value: Any](./phasemetaparameter/value.md)
  A value for the metaparameter.
### Identifying the Parameter
- [var identifier: String](./phasemetaparameter/identifier.md)
  A unique name for the metaparameter.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [PHASENumberMetaParameter](./phasenumbermetaparameter.md)
- [PHASEStringMetaParameter](./phasestringmetaparameter.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Base Metaparameters
- [class PHASEMetaParameterDefinition](./phasemetaparameterdefinition.md)
  A specification for a named parameter with a constant value.
- [class PHASEGlobalMetaParameterAsset](./phaseglobalmetaparameterasset.md)
  A reference to a registered metaparameter that the app can share with multiple sound events or sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasemetaparameter)*