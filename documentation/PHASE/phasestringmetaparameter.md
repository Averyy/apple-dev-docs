# PHASEStringMetaParameter

**Framework**: PHASE  
**Kind**: class

A metaparameter with a text definition that can change over time.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class PHASEStringMetaParameter
```

#### Overview

This class contains text that updates, like a “weather” metaparameter that the app changes from “rainy” to “sunny.”

To create an instance of this class, first create a [`PHASEStringMetaParameterDefinition`](phasestringmetaparameterdefinition.md), and either:

- Register it with the engine by calling [`registerGlobalMetaParameter(metaParameterDefinition:)`](phaseassetregistry/registerglobalmetaparameter(metaparameterdefinition:).md), then access the instance of this class in the engine’s [`globalMetaParameters`](phaseassetregistry/globalmetaparameters.md) dictionary.
- Pass it to the [`PHASESwitchNodeDefinition`](phaseswitchnodedefinition.md) initializer, [`init(switchMetaParameterDefinition:)`](phaseswitchnodedefinition/init(switchmetaparameterdefinition:).md), and then access the instance of this class in a sound event’s [`metaParameters`](phasesoundevent/metaparameters.md) dictionary.

## Relationships

### Inherits From
- [PHASEMetaParameter](phasemetaparameter.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PHASEStringMetaParameterDefinition](phasestringmetaparameterdefinition.md)
  A specification for a metaparameter defined by text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasestringmetaparameter)*