# MERAWProcessingParameter.SubGroup

**Framework**: MediaExtension  
**Kind**: class  
**Role**: Class

An object that describes a sub group parameter of a RAW processor.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class SubGroup
```

```objc
@interface MERAWProcessingSubGroupParameter : MERAWProcessingParameter
```

## Overview

Sub groups are logical groupings of [`MERAWProcessingParameter`](../merawprocessingparameter.md) objects that should be displayed together in an application user interface.

## Topics

### Creating a sub group parameter object
- [init(name: String, description: String, parameters: [MERAWProcessingParameter])](./subgroup/init%28name,description,parameters%29.md)
  Creates a sub group parameter object with the parameters value.
### Properties
- [var subGroupParameters: [MERAWProcessingParameter]](./subgroup/subgroupparameters.md)
  The array of [`MERAWProcessingParameter`](../merawprocessingparameter.md) objects in the sub group.

## Relationships

### Inherits From
- [MERAWProcessingParameter](../merawprocessingparameter.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Processing parameters
- [MERAWProcessingParameter.Boolean](./boolean.md)
  An object that describes a Boolean parameter of a RAW processor.
- [MERAWProcessingParameter.FloatingPoint](./floatingpoint.md)
  An object that describes a floating-point parameter of a RAW processor.
- [MERAWProcessingParameter.Integer](./integer.md)
  An object that describes an integer parameter of a RAW processor.
- [MERAWProcessingParameter.List](./list.md)
  An object that describes a list parameter of a RAW processor.
- [MERAWProcessingParameter.ListElement](./listelement.md)
  An object that describes a list element parameter of a RAW processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/subgroup)*