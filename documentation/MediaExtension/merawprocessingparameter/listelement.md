# MERAWProcessingParameter.ListElement

**Framework**: MediaExtension  
**Kind**: class  
**Role**: Class

An object that describes a list element parameter of a RAW processor.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class ListElement
```

```objc
@interface MERAWProcessingListElementParameter : MERAWProcessingParameter
```

#### Overview

The `MERAWProcessingParameterListElement` protocol provides an interface for `VideoToolbox` to query descriptions of the different elements in a parameter list for a list element in a `MERAWProcessingParameter`.  A distinct `MERAWProcessingParameterListElement` is created for each list element.

## Topics

### Creating a list element parameter object
- [init(name: String, description: String, elementID: Int)](./listelement/init%28name,description,elementid%29.md)
  Creates a list element parameter object with the element id value.
### Properties
- [var listElementID: Int](./listelement/listelementid.md)
  A unique number in the list which represents this list option.

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
- [MERAWProcessingParameter.SubGroup](./subgroup.md)
  An object that describes a sub group parameter of a RAW processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/listelement)*