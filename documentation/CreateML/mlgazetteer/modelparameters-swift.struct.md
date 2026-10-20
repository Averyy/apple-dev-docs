# MLGazetteer.ModelParameters

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

The model configuration parameters.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct ModelParameters
```

## Topics

### Creating parameters
- [init(language: NLLanguage?)](./modelparameters-swift.struct/init%28language%29.md)
  Creates model parameters.
### Accessing parameters
- [var language: NLLanguage?](./modelparameters-swift.struct/language.md)
  The language setting.
### Describing parameters
- [var description: String](./modelparameters-swift.struct/description.md)
  A text representation of the gazetteer settings.
- [var debugDescription: String](./modelparameters-swift.struct/debugdescription.md)
  A text representation of the gazetteer settings that’s suitable for output during debugging.
- [var playgroundDescription: Any](./modelparameters-swift.struct/playgrounddescription.md)
  A description of the gazetteer settings shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./modelparameters-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](./modelparameters-swift.struct/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](./modelparameters-swift.struct/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomPlaygroundDisplayConvertible](../../Swift/customplaygrounddisplayconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a gazetteer
- [init(dictionary: [String : [String]], parameters: MLGazetteer.ModelParameters) throws](./init%28dictionary,parameters%29.md)
  Creates a gazetteer from a dictionary of labels and terms.
- [init(labeledData: MLDataTable, textColumn: String, labelColumn: String, parameters: MLGazetteer.ModelParameters) throws](./init%28labeleddata,textcolumn,labelcolumn,parameters%29.md)
  Creates a gazetteer from a table of labels and terms.
- [let modelParameters: MLGazetteer.ModelParameters](./modelparameters-swift.property.md)
  The model configuration parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlgazetteer/modelparameters-swift.struct)*