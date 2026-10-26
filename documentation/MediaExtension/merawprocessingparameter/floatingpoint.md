# MERAWProcessingParameter.FloatingPoint

**Framework**: MediaExtension  
**Kind**: class  
**Role**: Class

An object that describes a floating-point parameter of a RAW processor.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class FloatingPoint
```

```objc
@interface MERAWProcessingFloatParameter : MERAWProcessingParameter
```

## Topics

### Creating a floating-point parameter object
- [convenience init(name: String, key: String, description: String, initialValue: Float, maximum: Float, minimum: Float, neutralValue: Float?, cameraValue: Float?)](./floatingpoint/init%28name,key,description,initialvalue,maximum,minimum,neutralvalue,cameravalue%29.md)
  Creates a floating-point parameter object.
- [- initWithName:key:description:initialValue:maximum:minimum:](../merawprocessingfloatparameter/initwithname_key_description_initialvalue_maximum_minimum_.md)
  Creates a floating-point parameter object with the initial value.
- [- initWithName:key:description:initialValue:maximum:minimum:cameraValue:](../merawprocessingfloatparameter/initwithname_key_description_initialvalue_maximum_minimum_cameravalue_.md)
  Creates a floating-point parameter object with the initial and camera values.
- [- initWithName:key:description:initialValue:maximum:minimum:neutralValue:](../merawprocessingfloatparameter/initwithname_key_description_initialvalue_maximum_minimum_neutralvalue_.md)
  Creates a floating-point parameter object with the initial and neutral values.
- [- initWithName:key:description:initialValue:maximum:minimum:neutralValue:cameraValue:](../merawprocessingfloatparameter/initwithname_key_description_initialvalue_maximum_minimum_neutralvalue_cameravalue_.md)
  Creates a floating-point parameter object with the initial, neutral, and camera values.
### Properties
- [var currentValue: Float](./floatingpoint/currentvalue.md)
  Get or set the current value for this parameter.
- [var initialValue: Float](./floatingpoint/initialvalue.md)
  The initial value for this parameter as defined in the sequence metadata.
- [var maximumValue: Float](./floatingpoint/maximumvalue.md)
  The maximum value for this parameter.
- [var minimumValue: Float](./floatingpoint/minimumvalue.md)
  The minimum value for this parameter.
### Instance Properties
- [var cameraValue: Float?](./floatingpoint/cameravalue.md)
- [var neutralValue: Float?](./floatingpoint/neutralvalue.md)
### Inspecting a parameter
- [- hasCameraValue:](../merawprocessingfloatparameter/hascameravalue_.md)
  The optional camera value for this parameter.
- [- hasNeutralValue:](../merawprocessingfloatparameter/hasneutralvalue_.md)
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
- [MERAWProcessingParameter.Integer](./integer.md)
  An object that describes an integer parameter of a RAW processor.
- [MERAWProcessingParameter.List](./list.md)
  An object that describes a list parameter of a RAW processor.
- [MERAWProcessingParameter.ListElement](./listelement.md)
  An object that describes a list element parameter of a RAW processor.
- [MERAWProcessingParameter.SubGroup](./subgroup.md)
  An object that describes a sub group parameter of a RAW processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/floatingpoint)*