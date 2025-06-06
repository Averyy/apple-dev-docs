# MERAWProcessingParameter.ListElement

**Framework**: MediaExtension  
**Kind**: class

An object that describes a list element parameter of a RAW processor.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class ListElement
```

#### Overview

The `MERAWProcessingParameterListElement` protocol provides an interface for `VideoToolbox` to query descriptions of the different elements in a parameter list for a list element in a `MERAWProcessingParameter`.  A distinct `MERAWProcessingParameterListElement` is created for each list element.

## Topics

### Creating a list element parameter object
- [init(name: String, description: String, elementID: Int)](merawprocessingparameter/listelement/init(name:description:elementid:).md)
  Creates a list element parameter object with the element id value.
### Properties
- [var listElementID: Int](merawprocessingparameter/listelement/listelementid.md)
  A unique number in the list which represents this list option.

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
- [MERAWProcessingParameter.SubGroup](merawprocessingparameter/subgroup.md)
  An object that describes a sub group parameter of a RAW processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/listelement)*