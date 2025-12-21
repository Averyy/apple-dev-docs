# MLWordTagger

**Framework**: Create ML  
**Kind**: struct

A word-tagging model you train to classify natural language text at the word level.

**Availability**:
- macOS 10.14+

## Declaration

```swift
struct MLWordTagger
```

## Mentions

- [Creating a word tagger model](creating-a-word-tagger-model.md)

#### Overview

Use an [`MLWordTagger`](mlwordtagger.md) to create a custom word tagger to identify content that’s relevant for your app, like product names and points of interest.

To use your custom word tagger in the [`Natural Language`](https://developer.apple.com/documentation/NaturalLanguage) framework, save it to a model file and import it into an [`NLModel`](https://developer.apple.com/documentation/NaturalLanguage/NLModel). Then add your custom [`NLModel`](https://developer.apple.com/documentation/NaturalLanguage/NLModel) to an [`NLTagger`](https://developer.apple.com/documentation/NaturalLanguage/NLTagger) with its [`setModels(_:forTagScheme:)`](https://developer.apple.com/documentation/NaturalLanguage/NLTagger/setModels(_:forTagScheme:)) method.

## Topics

### Creating and training a word tagger
- [init(trainingData: [(tokens: [MLWordTagger.Token], labels: [String])], parameters: MLWordTagger.ModelParameters) throws](mlwordtagger/init(trainingdata:parameters:).md)
  Creates a word tagger.
- [init(trainingData:tokenColumn:labelColumn:parameters:)](mlwordtagger/init(trainingdata:tokencolumn:labelcolumn:parameters:).md)
  Creates a word tagger.
- [MLWordTagger.Token](mlwordtagger/token.md)
  The token type of a word tagger, which is a string.
- [MLWordTagger.ModelParameters](mlwordtagger/modelparameters-swift.struct.md)
  Parameters that specify model training parameters and validation data.
- [let modelParameters: MLWordTagger.ModelParameters](mlwordtagger/modelparameters-swift.property.md)
  The configuration parameters that the word tagger used for training during initialization.
### Evaluating a word tagger
- [func evaluation(on:tokenColumn:labelColumn:)](mlwordtagger/evaluation(on:tokencolumn:labelcolumn:).md)
  Computes evaluation metrics.
- [func evaluation(on: [(tokens: [MLWordTagger.Token], labels: [String])]) -> MLWordTaggerMetrics](mlwordtagger/evaluation(on:).md)
  Computes evaluation metrics.
- [let trainingMetrics: MLWordTaggerMetrics](mlwordtagger/trainingmetrics.md)
  Measurements of the tagger’s performance on the training data set.
- [let validationMetrics: MLWordTaggerMetrics](mlwordtagger/validationmetrics.md)
  Measurements of the tagger’s performance on the validation data set.
- [struct MLWordTaggerMetrics](mlwordtaggermetrics.md)
  Metrics you use to evaluate a word tagger’s performance.
### Testing a word tagger
- [func prediction(from:)](mlwordtagger/prediction(from:).md)
  Predicts a tag for the input string.
- [func predictions(from:)](mlwordtagger/predictions(from:).md)
  Predicts sequences of labels, token locations, and token lengths from the input strings.
- [func predictionWithConfidence(from:)](mlwordtagger/predictionwithconfidence(from:).md)
  Predicts tags and confidence scores for the input string. Predicts tags and confidence scores for the input string.
### Saving a word tagger
- [func write(to: URL, metadata: MLModelMetadata?) throws](mlwordtagger/write(to:metadata:).md)
  Exports the word tagger as a Core ML model file at the specified URL.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlwordtagger/write(tofile:metadata:).md)
  Exports the word tagger as a Core ML model file at the specified file path.
### Describing a word tagger
- [var model: MLModel](mlwordtagger/model.md)
  The underlying Core ML model of the word tagger.
- [var description: String](mlwordtagger/description.md)
  A text representation of the word tagger.
- [var debugDescription: String](mlwordtagger/debugdescription.md)
  A text representation of the word tagger that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlwordtagger/playgrounddescription.md)
  A description of the word tagger in a playground.
### Supporting types
- [MLWordTagger.FeatureExtractorType](mlwordtagger/featureextractortype.md)
  The feature extractors that are available to train a word tagger using with the transfer-learning algorithm option.
- [MLWordTagger.ModelAlgorithmType](mlwordtagger/modelalgorithmtype.md)
  The algorithm type.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlwordtagger/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlwordtagger/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlwordtagger/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Creating a text classifier model](creating-a-text-classifier-model.md)
  Train a machine learning model to classify natural language text.
- [Creating a word tagger model](creating-a-word-tagger-model.md)
  Train a machine learning model to tag individual words in natural language text.
- [struct MLTextClassifier](mltextclassifier.md)
  A model you train to classify natural language text.
- [struct MLGazetteer](mlgazetteer.md)
  A collection of terms and their labels, which augments a tagger that analyzes natural language text.
- [struct MLWordEmbedding](mlwordembedding.md)
  A map of strings in a vector space that enable your app to find similar strings by looking at a string’s neighbors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger)*