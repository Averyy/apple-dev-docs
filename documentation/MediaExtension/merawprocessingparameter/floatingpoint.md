# MERAWProcessingParameter.FloatingPoint

**Framework**: MediaExtension  
**Kind**: class

An object that describes a floating-point parameter of a RAW processor.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class FloatingPoint
```

## Topics

### Creating a floating-point parameter object
- [convenience init(name: String, key: String, description: String, initialValue: Float, maximum: Float, minimum: Float, neutralValue: Float?, cameraValue: Float?)](merawprocessingparameter/floatingpoint/init(name:key:description:initialvalue:maximum:minimum:neutralvalue:cameravalue:).md)
  Creates a floating-point parameter object.
### Properties
- [var currentValue: Float](merawprocessingparameter/floatingpoint/currentvalue.md)
  Get or set the current value for this parameter.
- [var initialValue: Float](merawprocessingparameter/floatingpoint/initialvalue.md)
  The initial value for this parameter as defined in the sequence metadata.
- [var maximumValue: Float](merawprocessingparameter/floatingpoint/maximumvalue.md)
  The maximum value for this parameter.
- [var minimumValue: Float](merawprocessingparameter/floatingpoint/minimumvalue.md)
  The minimum value for this parameter.
### Instance Properties
- [var cameraValue: Float?](merawprocessingparameter/floatingpoint/cameravalue.md)
- [var neutralValue: Float?](merawprocessingparameter/floatingpoint/neutralvalue.md)

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
- [MERAWProcessingParameter.Integer](merawprocessingparameter/integer.md)
  An object that describes an integer parameter of a RAW processor.
- [MERAWProcessingParameter.List](merawprocessingparameter/list.md)
  An object that describes a list parameter of a RAW processor.
- [MERAWProcessingParameter.ListElement](merawprocessingparameter/listelement.md)
  An object that describes a list element parameter of a RAW processor.
- [MERAWProcessingParameter.SubGroup](merawprocessingparameter/subgroup.md)
  An object that describes a sub group parameter of a RAW processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/floatingpoint)*