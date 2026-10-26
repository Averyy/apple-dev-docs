# MERAWProcessingParameter.Integer

**Framework**: MediaExtension  
**Kind**: class  
**Role**: Class

An object that describes an integer parameter of a RAW processor.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class Integer
```

```objc
@interface MERAWProcessingIntegerParameter : MERAWProcessingParameter
```

## Topics

### Creating an integer parameter object
- [convenience init(name: String, key: String, description: String, initialValue: Int, maximum: Int, minimum: Int, neutralValue: Int?, cameraValue: Int?)](./integer/init%28name,key,description,initialvalue,maximum,minimum,neutralvalue,cameravalue%29.md)
  Creates an integer parameter object.
- [- initWithName:key:description:initialValue:maximum:minimum:](../merawprocessingintegerparameter/initwithname_key_description_initialvalue_maximum_minimum_.md)
  Creates a integer parameter object with the initial value.
- [- initWithName:key:description:initialValue:maximum:minimum:cameraValue:](../merawprocessingintegerparameter/initwithname_key_description_initialvalue_maximum_minimum_cameravalue_.md)
  Creates an integer parameter object with the initial and camera values.
- [- initWithName:key:description:initialValue:maximum:minimum:neutralValue:](../merawprocessingintegerparameter/initwithname_key_description_initialvalue_maximum_minimum_neutralvalue_.md)
  Creates an integer parameter object with the initial and neutral values.
- [- initWithName:key:description:initialValue:maximum:minimum:neutralValue:cameraValue:](../merawprocessingintegerparameter/initwithname_key_description_initialvalue_maximum_minimum_neutralvalue_cameravalue_.md)
  Creates an integer parameter object with the initial, neutral, and camera values.
### Properties
- [var currentValue: Int](./integer/currentvalue.md)
  Get or set the current value for this parameter.
- [var initialValue: Int](./integer/initialvalue.md)
  The initial value for this parameter as defined in the sequence metadata.
- [var maximumValue: Int](./integer/maximumvalue.md)
  The maximum value for this parameter.
- [var minimumValue: Int](./integer/minimumvalue.md)
  The minimum value for this parameter.
### Instance Properties
- [var cameraValue: Int?](./integer/cameravalue.md)
- [var neutralValue: Int?](./integer/neutralvalue.md)
### Inspecting a parameter
- [- hasCameraValue:](../merawprocessingintegerparameter/hascameravalue_.md)
  The optional camera value for this parameter.
- [- hasNeutralValue:](../merawprocessingintegerparameter/hasneutralvalue_.md)
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
- [MERAWProcessingParameter.List](./list.md)
  An object that describes a list parameter of a RAW processor.
- [MERAWProcessingParameter.ListElement](./listelement.md)
  An object that describes a list element parameter of a RAW processor.
- [MERAWProcessingParameter.SubGroup](./subgroup.md)
  An object that describes a sub group parameter of a RAW processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/integer)*