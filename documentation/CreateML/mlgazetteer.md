# MLGazetteer

**Framework**: Create ML  
**Kind**: struct

A collection of terms and their labels, which augments a tagger that analyzes natural language text.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct MLGazetteer
```

#### Overview

Use an [`MLGazetteer`](mlgazetteer.md) to configure a gazetteer and save it to a file, which you then add to your app in Xcode. Your app uses the gazetteer file at runtime to create an instance of [`NLGazetteer`](https://developer.apple.com/documentation/NaturalLanguage/NLGazetteer), which augments an [`NLTagger`](https://developer.apple.com/documentation/NaturalLanguage/NLTagger) to tag specific terms with a label.

You configure a gazetteer with a dictionary, keyed by labels. Each value in the dictionary is an array of terms (words or phrases) for each label. For example, you can store the names of real and fictional planets in a gazetteer.

```swift
let planets = [
    "real planet": ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"],
    "fictional planet" : ["Arrakis", "Hoth", "Vulcan", "Pandora", "Tatooine", "Bajor", "Alderaan", "Romulus"]
]

let parameters = MLGazetteer.ModelParameters(language: .english)
let planetGazetteer = try! MLGazetteer(dictionary: planets, parameters: parameters)
```

Once you’ve configured an [`MLGazetteer`](mlgazetteer.md), save it to an `.mlmodel` file to include in your app.

```swift
try planetGazetteer.write(toFile: "~/Desktop/PlanetGazetteer.mlmodel")
```

A gazetteer file can efficiently store many labels, and many terms for each label.

## Topics

### Creating a gazetteer
- [init(dictionary: [String : [String]], parameters: MLGazetteer.ModelParameters) throws](mlgazetteer/init(dictionary:parameters:).md)
  Creates a gazetteer from a dictionary of labels and terms.
- [init(labeledData: MLDataTable, textColumn: String, labelColumn: String, parameters: MLGazetteer.ModelParameters) throws](mlgazetteer/init(labeleddata:textcolumn:labelcolumn:parameters:).md)
  Creates a gazetteer from a table of labels and terms.
- [MLGazetteer.ModelParameters](mlgazetteer/modelparameters-swift.struct.md)
  The model configuration parameters.
- [let modelParameters: MLGazetteer.ModelParameters](mlgazetteer/modelparameters-swift.property.md)
  The model configuration parameters.
### Testing a gazetteer
- [func prediction(from: String) throws -> String](mlgazetteer/prediction(from:).md)
  Predicts the label for the given term.
- [func predictions(from: [String]) throws -> [String]](mlgazetteer/predictions(from:)-2rej.md)
  Predicts the labels for the given terms.
- [func predictions(from: MLDataColumn<String>) throws -> MLDataColumn<String>](mlgazetteer/predictions(from:)-2jaui.md)
  Predicts the labels for the given terms in the table column.
### Saving a gazetteer
- [func write(to: URL, metadata: MLModelMetadata?) throws](mlgazetteer/write(to:metadata:).md)
  Exports the gazetteer as a Core ML model file at the specified URL.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlgazetteer/write(tofile:metadata:).md)
  Exports the gazetteer as a Core ML model file at the specified file path.
### Describing a gazetteer
- [var model: MLModel](mlgazetteer/model.md)
  The gazetteer contained within a Core ML model file stored in memory.
- [var description: String](mlgazetteer/description.md)
  A text representation of the gazetteer.
- [var debugDescription: String](mlgazetteer/debugdescription.md)
  A text representation of the gazetteer that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlgazetteer/playgrounddescription.md)
  A description of the gazetteer shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlgazetteer/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlgazetteer/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlgazetteer/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)

## See Also

- [Creating a text classifier model](creating-a-text-classifier-model.md)
  Train a machine learning model to classify natural language text.
- [Creating a word tagger model](../NaturalLanguage/creating-a-word-tagger-model.md)
  Train a machine learning model to tag individual words in natural language text.
- [struct MLTextClassifier](mltextclassifier.md)
  A model you train to classify natural language text.
- [struct MLWordTagger](mlwordtagger.md)
  A word-tagging model you train to classify natural language text at the word level.
- [struct MLWordEmbedding](mlwordembedding.md)
  A map of strings in a vector space that enable your app to find similar strings by looking at a string’s neighbors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlgazetteer)*