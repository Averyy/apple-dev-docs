# MERAWProcessingParameter.SubGroup

**Framework**: MediaExtension  
**Kind**: class

An object that describes a sub group parameter of a RAW processor.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class SubGroup
```

#### Overview

Sub groups are logical groupings of [`MERAWProcessingParameter`](merawprocessingparameter.md) objects that should be displayed together in an application user interface.

## Topics

### Creating a sub group parameter object
- [init(name: String, description: String, parameters: [MERAWProcessingParameter])](merawprocessingparameter/subgroup/init(name:description:parameters:).md)
  Creates a sub group parameter object with the parameters value.
### Properties
- [var subGroupParameters: [MERAWProcessingParameter]](merawprocessingparameter/subgroup/subgroupparameters.md)
  The array of [`MERAWProcessingParameter`](merawprocessingparameter.md) objects in the sub group.

## Relationships

### Inherits From
- [MERAWProcessingParameter](merawprocessingparameter.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [MERAWProcessingParameter.Boolean](merawprocessingparameter/boolean.md)
  An object that describes a Boolean parameter of a RAW processor.
- [MERAWProcessingParameter.FloatingPoint](merawprocessingparameter/floatingpoint.md)
  An object that describes a floating-point parameter of a RAW processor.
- [MERAWProcessingParameter.Integer](merawprocessingparameter/integer.md)
  An object that describes an integer parameter of a RAW processor.
- [MERAWProcessingParameter.List](merawprocessingparameter/list.md)
  An object that describes a list parameter of a RAW processor.
- [MERAWProcessingParameter.ListElement](merawprocessingparameter/listelement.md)
  An object that describes a list element parameter of a RAW processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/subgroup)*