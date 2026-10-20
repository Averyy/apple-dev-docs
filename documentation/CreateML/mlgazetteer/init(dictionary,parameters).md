# init(dictionary:parameters:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a gazetteer from a dictionary of labels and terms.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(dictionary: [String : [String]], parameters: MLGazetteer.ModelParameters = ModelParameters()) throws
```

## Parameters

- `dictionary`: A dictionary of labels and terms.
- `parameters`: The model parameters.

## See Also

### Creating a gazetteer
- [init(labeledData: MLDataTable, textColumn: String, labelColumn: String, parameters: MLGazetteer.ModelParameters) throws](./init%28labeleddata,textcolumn,labelcolumn,parameters%29.md)
  Creates a gazetteer from a table of labels and terms.
- [MLGazetteer.ModelParameters](./modelparameters-swift.struct.md)
  The model configuration parameters.
- [let modelParameters: MLGazetteer.ModelParameters](./modelparameters-swift.property.md)
  The model configuration parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlgazetteer/init(dictionary:parameters:))*