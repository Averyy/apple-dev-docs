# init(labeledData:textColumn:labelColumn:parameters:)

**Framework**: Create ML  
**Kind**: init

Creates a gazetteer from a table of labels and terms.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(labeledData: MLDataTable, textColumn: String, labelColumn: String, parameters: MLGazetteer.ModelParameters = ModelParameters()) throws
```

## Parameters

- `labeledData`: A table of labels and terms.
- `textColumn`: The name of the column containing the terms.
- `labelColumn`: The name of the column containing the labels.
- `parameters`: The model parameters.

## See Also

- [init(dictionary: [String : [String]], parameters: MLGazetteer.ModelParameters) throws](mlgazetteer/init(dictionary:parameters:).md)
  Creates a gazetteer from a dictionary of labels and terms.
- [MLGazetteer.ModelParameters](mlgazetteer/modelparameters-swift.struct.md)
  The model configuration parameters.
- [let modelParameters: MLGazetteer.ModelParameters](mlgazetteer/modelparameters-swift.property.md)
  The model configuration parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlgazetteer/init(labeleddata:textcolumn:labelcolumn:parameters:))*