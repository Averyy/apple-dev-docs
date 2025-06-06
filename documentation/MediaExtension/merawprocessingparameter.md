# MERAWProcessingParameter

**Framework**: MediaExtension  
**Kind**: class

An object for the RAW processor to describe each processing parameter the processor exposes.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class MERAWProcessingParameter
```

#### Discussion

This protocol provides an interface for Video Toolbox to query descriptions of the different parameters that can be used to influence RAW processor operation.  A distinct [`MERAWProcessingParameter`](merawprocessingparameter.md) is created for each parameter supported by the RAW processor, and the set of supported parameters is returned by the [`processingParameters`](merawprocessor/processingparameters.md) interface.

## Topics

### Inspecting a processing parameter
- [var enabled: Bool](merawprocessingparameter/enabled.md)
  A Boolean value that indicates whether the extension enables the parameter.
- [var key: String](merawprocessingparameter/key.md)
  A unique key string identifying the parameter.
- [var longDescription: String](merawprocessingparameter/longdescription.md)
  A localized description of the parameter, suitable for displaying in a tool tip or similar explanatory UI.
- [var name: String](merawprocessingparameter/name.md)
  A localized human-readable name for the parameter, suitable for displaying in application UI.
### Processing parameters
- [MERAWProcessingParameter.Boolean](merawprocessingparameter/boolean.md)
  An object that describes a Boolean parameter of a RAW processor.
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
### Class methods
- [class func boolean(name: String, key: String, description: String, initialValue: Bool, neutralValue: Bool?, cameraValue: Bool?) -> MERAWProcessingParameter.Boolean](merawprocessingparameter/boolean(name:key:description:initialvalue:neutralvalue:cameravalue:).md)
- [class func integer(name: String, key: String, description: String, initialValue: Int, maximum: Int, minimum: Int, neutralValue: Int?, cameraValue: Int?) -> MERAWProcessingParameter.Integer](merawprocessingparameter/integer(name:key:description:initialvalue:maximum:minimum:neutralvalue:cameravalue:).md)
- [class func list(name: String, key: String, description: String, list: [MERAWProcessingParameter.ListElement], initialValue: Int, neutralValue: Int?, cameraValue: Int?) -> MERAWProcessingParameter.List](merawprocessingparameter/list(name:key:description:list:initialvalue:neutralvalue:cameravalue:).md)
- [class func listElement(name: String, description: String, elementID: Int) -> MERAWProcessingParameter.ListElement](merawprocessingparameter/listelement(name:description:elementid:).md)
- [class func subGroup(name: String, description: String, parameters: [MERAWProcessingParameter]) -> MERAWProcessingParameter.SubGroup](merawprocessingparameter/subgroup(name:description:parameters:).md)
- [class func float(name: String, key: String, description: String, initialValue: Float, maximum: Float, minimum: Float, neutralValue: Float?, cameraValue: Float?) -> MERAWProcessingParameter.FloatingPoint](merawprocessingparameter/float(name:key:description:initialvalue:maximum:minimum:neutralvalue:cameravalue:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [MERAWProcessingParameter.Boolean](merawprocessingparameter/boolean.md)
- [MERAWProcessingParameter.FloatingPoint](merawprocessingparameter/floatingpoint.md)
- [MERAWProcessingParameter.Integer](merawprocessingparameter/integer.md)
- [MERAWProcessingParameter.List](merawprocessingparameter/list.md)
- [MERAWProcessingParameter.ListElement](merawprocessingparameter/listelement.md)
- [MERAWProcessingParameter.SubGroup](merawprocessingparameter/subgroup.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MERAWProcessor](merawprocessor.md)
  A protocol that defines the requirements for a RAW processor.
- [protocol MERAWProcessorExtension](merawprocessorextension.md)
  A protocol that defines a factory to create RAW processors for a codec type that the extension implements.
- [class MERAWProcessorPixelBufferManager](merawprocessorpixelbuffermanager.md)
  Describes pixel buffer requirements and creates new pixel buffers.
- [enum MERAWProcessorNotification](merawprocessornotification.md)
  Notifications that indicate a RAW processor state change.
- [RAW processor property list dictionary](raw-processor-property-list-dictionary.md)
  Include a property list dictionary to describe a RAW processor.
- [RAW processor entitlement](raw-processor-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension RAW processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter)*