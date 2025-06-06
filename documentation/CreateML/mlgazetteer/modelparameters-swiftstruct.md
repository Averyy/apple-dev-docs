# MLGazetteer.ModelParameters

**Framework**: Create ML  
**Kind**: struct

The model configuration parameters.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct ModelParameters
```

## Topics

### Creating parameters
- [init(language: NLLanguage?)](mlgazetteer/modelparameters-swift.struct/init(language:).md)
  Creates model parameters.
### Accessing parameters
- [var language: NLLanguage?](mlgazetteer/modelparameters-swift.struct/language.md)
  The language setting.
### Describing parameters
- [var description: String](mlgazetteer/modelparameters-swift.struct/description.md)
  A text representation of the gazetteer settings.
- [var debugDescription: String](mlgazetteer/modelparameters-swift.struct/debugdescription.md)
  A text representation of the gazetteer settings that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlgazetteer/modelparameters-swift.struct/playgrounddescription.md)
  A description of the gazetteer settings shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlgazetteer/modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlgazetteer/modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlgazetteer/modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init(dictionary: [String : [String]], parameters: MLGazetteer.ModelParameters) throws](mlgazetteer/init(dictionary:parameters:).md)
  Creates a gazetteer from a dictionary of labels and terms.
- [init(labeledData: MLDataTable, textColumn: String, labelColumn: String, parameters: MLGazetteer.ModelParameters) throws](mlgazetteer/init(labeleddata:textcolumn:labelcolumn:parameters:).md)
  Creates a gazetteer from a table of labels and terms.
- [let modelParameters: MLGazetteer.ModelParameters](mlgazetteer/modelparameters-swift.property.md)
  The model configuration parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlgazetteer/modelparameters-swift.struct)*