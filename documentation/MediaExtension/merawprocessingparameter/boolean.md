# MERAWProcessingParameter.Boolean

**Framework**: MediaExtension  
**Kind**: class

An object that describes a Boolean parameter of a RAW processor.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class Boolean
```

## Topics

### Creating a boolean parameter object
- [convenience init(name: String, key: String, description: String, initialValue: Bool, neutralValue: Bool?, cameraValue: Bool?)](merawprocessingparameter/boolean/init(name:key:description:initialvalue:neutralvalue:cameravalue:).md)
  Creates a Boolean parameter object.
### Properties
- [var currentValue: Bool](merawprocessingparameter/boolean/currentvalue.md)
  Get or set the current value for this parameter.
- [var initialValue: Bool](merawprocessingparameter/boolean/initialvalue.md)
  The initial value for this parameter as defined in the sequence metadata.
### Instance Properties
- [var cameraValue: Bool?](merawprocessingparameter/boolean/cameravalue.md)
- [var neutralValue: Bool?](merawprocessingparameter/boolean/neutralvalue.md)

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

- [MERAWProcessingParameter.FloatingPoint](merawprocessingparameter/floatingpoint.md)
  An object that describes a floating-point parameter of a RAW processor.
- [MERAWProcessingParameter.Integer](merawprocessingparameter/integer.md)
  An object that describes an integer parameter of a RAW processor.
- [MERAWProcessingParameter.List](merawprocessingparameter/list.md)
  An object that describes a list parameter of a RAW processor.
- [MERAWProcessingParameter.ListElement](merawprocessingparameter/listelement.md)
  An object that describes a list element parameter of a RAW processor.
- [MERAWProcessingParameter.SubGroup](merawprocessingparameter/subgroup.md)
  An object that describes a sub group parameter of a RAW processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/boolean)*