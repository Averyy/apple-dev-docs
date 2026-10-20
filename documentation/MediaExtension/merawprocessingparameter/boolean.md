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
### Properties
- [var currentValue: Bool](./boolean/currentvalue.md)
  Get or set the current value for this parameter.
- [var initialValue: Bool](./boolean/initialvalue.md)
  The initial value for this parameter as defined in the sequence metadata.
### Instance Properties
- [var cameraValue: Bool?](./boolean/cameravalue.md)
- [var neutralValue: Bool?](./boolean/neutralvalue.md)

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