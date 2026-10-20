# PipelineDataError.incompatibleDataFormat(operation:debugDescription:)

**Framework**: Create ML Components  
**Kind**: case  
**Role**: Case

An error that indicates that an input doesn’t have the expected data format.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
case incompatibleDataFormat(operation: String, debugDescription: String)
```

## See Also

### Analyzing the error
- [PipelineDataError.emptyInput(operation:)](./emptyinput%28operation%29.md)
  An error that indicates that the input to fit is empty.
- [case incompatibleConfiguration(operation: String, debugDescription: String)](./incompatibleconfiguration%28operation,debugdescription%29.md)
  An error that indicates that an input is not compatible with an operation’s configuration.
- [PipelineDataError.incompatibleShape(_:debugDescription:)](./incompatibleshape%28_,debugdescription%29.md)
  An error that indicates that an input’s doesn’t have the expected shape for the operation.
- [PipelineDataError.missingAnnotation(operation:)](./missingannotation%28operation%29.md)
  An error that indicates that an expected annotation is missing.
- [PipelineDataError.missingValue(operation:)](./missingvalue%28operation%29.md)
  An error that indicates that an expected value is missing.
- [case unrecognizedCategory(operation: String, category: String)](./unrecognizedcategory%28operation,category%29.md)
  An error that indicates that a new category was encountered after fitting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/pipelinedataerror/incompatibledataformat(operation:debugdescription:))*