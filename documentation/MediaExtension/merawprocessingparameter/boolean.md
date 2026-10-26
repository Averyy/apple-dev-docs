# MERAWProcessingParameter.Boolean

**Framework**: MediaExtension  
**Kind**: class  
**Role**: Class

An object that describes a Boolean parameter of a RAW processor.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class Boolean
```

```objc
@interface MERAWProcessingBooleanParameter : MERAWProcessingParameter
```

## Topics

### Creating a boolean parameter object
- [convenience init(name: String, key: String, description: String, initialValue: Bool, neutralValue: Bool?, cameraValue: Bool?)](./boolean/init%28name,key,description,initialvalue,neutralvalue,cameravalue%29.md)
  Creates a Boolean parameter object.
- [- initWithName:key:description:initialValue:](../merawprocessingbooleanparameter/initwithname_key_description_initialvalue_.md)
  Creates a Boolean parameter object with the initial value.
- [- initWithName:key:description:initialValue:cameraValue:](../merawprocessingbooleanparameter/initwithname_key_description_initialvalue_cameravalue_.md)
  Creates a Boolean parameter object with the initial and camera values.
- [- initWithName:key:description:initialValue:neutralValue:](../merawprocessingbooleanparameter/initwithname_key_description_initialvalue_neutralvalue_.md)
  Creates a Boolean parameter object with the initial and neutral values.
- [- initWithName:key:description:initialValue:neutralValue:cameraValue:](../merawprocessingbooleanparameter/initwithname_key_description_initialvalue_neutralvalue_cameravalue_.md)
  Creates a Boolean parameter object with the initial, neutral, and camera values.
### Properties
- [var currentValue: Bool](./boolean/currentvalue.md)
  Get or set the current value for this parameter.
- [var initialValue: Bool](./boolean/initialvalue.md)
  The initial value for this parameter as defined in the sequence metadata.
### Instance Properties
- [var cameraValue: Bool?](./boolean/cameravalue.md)
- [var neutralValue: Bool?](./boolean/neutralvalue.md)
### Inspecting a parameter
- [- hasCameraValue:](../merawprocessingbooleanparameter/hascameravalue_.md)
  The optional camera value for this parameter.
- [- hasNeutralValue:](../merawprocessingbooleanparameter/hasneutralvalue_.md)
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
- [MERAWProcessingParameter.FloatingPoint](./floatingpoint.md)
  An object that describes a floating-point parameter of a RAW processor.
- [MERAWProcessingParameter.Integer](./integer.md)
  An object that describes an integer parameter of a RAW processor.
- [MERAWProcessingParameter.List](./list.md)
  An object that describes a list parameter of a RAW processor.
- [MERAWProcessingParameter.ListElement](./listelement.md)
  An object that describes a list element parameter of a RAW processor.
- [MERAWProcessingParameter.SubGroup](./subgroup.md)
  An object that describes a sub group parameter of a RAW processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/boolean)*