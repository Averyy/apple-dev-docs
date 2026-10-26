# MERAWProcessingParameter.List

**Framework**: MediaExtension  
**Kind**: class  
**Role**: Class

An object that describes a list parameter of a RAW processor.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class List
```

```objc
@interface MERAWProcessingListParameter : MERAWProcessingParameter
```

## Topics

### Creating a list parameter object
- [convenience init(name: String, key: String, description: String, list: [MERAWProcessingParameter.ListElement], initialValue: Int, neutralValue: Int?, cameraValue: Int?)](./list/init%28name,key,description,list,initialvalue,neutralvalue,cameravalue%29.md)
  Creates a list parameter object.
- [- initWithName:key:description:list:initialValue:](../merawprocessinglistparameter/initwithname_key_description_list_initialvalue_.md)
  Creates a list parameter object with the initial value.
- [- initWithName:key:description:list:initialValue:cameraValue:](../merawprocessinglistparameter/initwithname_key_description_list_initialvalue_cameravalue_.md)
  Creates a list parameter object with the initial and camera values.
- [- initWithName:key:description:list:initialValue:neutralValue:](../merawprocessinglistparameter/initwithname_key_description_list_initialvalue_neutralvalue_.md)
  Creates a list parameter object with the initial and neutral values.
- [- initWithName:key:description:list:initialValue:neutralValue:cameraValue:](../merawprocessinglistparameter/initwithname_key_description_list_initialvalue_neutralvalue_cameravalue_.md)
  Creates a list parameter object with the initial, neutral, and camera values.
### Properties
- [var currentValue: Int](./list/currentvalue.md)
  Get or set the current value for this parameter.
- [var initialValue: Int](./list/initialvalue.md)
  The initial value for this parameter as defined in the sequence metadata.
- [var listElements: [MERAWProcessingParameter.ListElement]](./list/listelements.md)
  The ordered array of `MERAWProcessingListElementParameter` which make up this list.
### Instance Properties
- [var cameraValue: Int?](./list/cameravalue.md)
- [var neutralValue: Int?](./list/neutralvalue.md)
### Inspecting a parameter
- [- hasCameraValue:](../merawprocessinglistparameter/hascameravalue_.md)
  The optional camera value for this parameter.
- [- hasNeutralValue:](../merawprocessinglistparameter/hasneutralvalue_.md)
  The optional neutral value for this parameter.

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
- [MERAWProcessingParameter.ListElement](./listelement.md)
  An object that describes a list element parameter of a RAW processor.
- [MERAWProcessingParameter.SubGroup](./subgroup.md)
  An object that describes a sub group parameter of a RAW processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/list)*