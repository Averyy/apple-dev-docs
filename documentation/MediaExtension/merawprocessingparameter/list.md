# MERAWProcessingParameter.List

**Framework**: MediaExtension  
**Kind**: class

An object that describes a list parameter of a RAW processor.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class List
```

## Topics

### Creating a list parameter object
- [convenience init(name: String, key: String, description: String, list: [MERAWProcessingParameter.ListElement], initialValue: Int, neutralValue: Int?, cameraValue: Int?)](merawprocessingparameter/list/init(name:key:description:list:initialvalue:neutralvalue:cameravalue:).md)
  Creates a list parameter object.
### Properties
- [var currentValue: Int](merawprocessingparameter/list/currentvalue.md)
  Get or set the current value for this parameter.
- [var initialValue: Int](merawprocessingparameter/list/initialvalue.md)
  The initial value for this parameter as defined in the sequence metadata.
- [var listElements: [MERAWProcessingParameter.ListElement]](merawprocessingparameter/list/listelements.md)
  The ordered array of `MERAWProcessingListElementParameter` which make up this list.
### Instance Properties
- [var cameraValue: Int?](merawprocessingparameter/list/cameravalue.md)
- [var neutralValue: Int?](merawprocessingparameter/list/neutralvalue.md)

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
- [MERAWProcessingParameter.ListElement](merawprocessingparameter/listelement.md)
  An object that describes a list element parameter of a RAW processor.
- [MERAWProcessingParameter.SubGroup](merawprocessingparameter/subgroup.md)
  An object that describes a sub group parameter of a RAW processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/list)*