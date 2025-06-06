# PipelineDataError.unrecognizedCategory(operation:category:)

**Framework**: Create ML Components  
**Kind**: case

An error that indicates that a new category was encountered after fitting.

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
case unrecognizedCategory(operation: String, category: String)
```

## See Also

- [PipelineDataError.emptyInput(operation:)](pipelinedataerror/emptyinput(operation:).md)
  An error that indicates that the input to fit is empty.
- [case incompatibleConfiguration(operation: String, debugDescription: String)](pipelinedataerror/incompatibleconfiguration(operation:debugdescription:).md)
  An error that indicates that an input is not compatible with an operation’s configuration.
- [case incompatibleDataFormat(operation: String, debugDescription: String)](pipelinedataerror/incompatibledataformat(operation:debugdescription:).md)
  An error that indicates that an input doesn’t have the expected data format.
- [PipelineDataError.incompatibleShape(_:debugDescription:)](pipelinedataerror/incompatibleshape(_:debugdescription:).md)
  An error that indicates that an input’s doesn’t have the expected shape for the operation.
- [PipelineDataError.missingAnnotation(operation:)](pipelinedataerror/missingannotation(operation:).md)
  An error that indicates that an expected annotation is missing.
- [PipelineDataError.missingValue(operation:)](pipelinedataerror/missingvalue(operation:).md)
  An error that indicates that an expected value is missing.
- [var errorDescription: String?](pipelinedataerror/errordescription.md)
  A localized message describing what error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/pipelinedataerror/unrecognizedcategory(operation:category:))*