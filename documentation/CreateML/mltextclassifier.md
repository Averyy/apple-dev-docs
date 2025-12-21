# MLTextClassifier

**Framework**: Create ML  
**Kind**: struct

A model you train to classify natural language text.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
struct MLTextClassifier
```

## Mentions

- [Creating a text classifier model](creating-a-text-classifier-model.md)

#### Overview

Use a text classifier to train a machine learning model you can include in your app to classify natural language text. The model learns to associate labels with features of the input text, which can be sentences, paragraphs, or even entire documents.

After you train a text classifier, you save it to a Core ML model file. You then use an instance of the [`NLModel`](https://developer.apple.com/documentation/NaturalLanguage/NLModel) class from the [`Natural Language`](https://developer.apple.com/documentation/NaturalLanguage) framework to read the model file into your app.

## Topics

### Creating and training a text classifier
- [init(trainingData:parameters:)](mltextclassifier/init(trainingdata:parameters:).md)
  Creates a text classifier.
- [init(trainingData:textColumn:labelColumn:parameters:)](mltextclassifier/init(trainingdata:textcolumn:labelcolumn:parameters:).md)
  Creates a text classifier.
- [MLTextClassifier.DataSource](mltextclassifier/datasource.md)
  A data source for a text classifier.
- [MLTextClassifier.ModelParameters](mltextclassifier/modelparameters-swift.struct.md)
  Parameters that specify model training parameters and validation data.
- [let modelParameters: MLTextClassifier.ModelParameters](mltextclassifier/modelparameters-swift.property.md)
  The configuration parameters that the text classifier used for training during initialization.
### Evaluating a text classifier
- [func evaluation(on:)](mltextclassifier/evaluation(on:).md)
  Computes evaluation metrics.
- [func evaluation(on:textColumn:labelColumn:)](mltextclassifier/evaluation(on:textcolumn:labelcolumn:).md)
  Computes evaluation metrics.
- [let trainingMetrics: MLClassifierMetrics](mltextclassifier/trainingmetrics.md)
  Measurements of the classifier’s performance on the training data set.
- [let validationMetrics: MLClassifierMetrics](mltextclassifier/validationmetrics.md)
  Measurements of the classifier’s performance on the validation data set.
### Testing a text classifier
- [func prediction(from: String) throws -> String](mltextclassifier/prediction(from:).md)
  Classifies a string with a label.
- [func predictions(from:)](mltextclassifier/predictions(from:).md)
  Classifies an array of strings with labels.
- [func predictionWithConfidence(from: String) throws -> [String : Double]](mltextclassifier/predictionwithconfidence(from:).md)
  Predicts multiple possible labels and their confidence scores for the specified string.
- [func predictionsWithConfidence(from:)](mltextclassifier/predictionswithconfidence(from:).md)
  Predicts multiple possible labels and their confidence scores for each string in the specified array.
### Saving a text classifier
- [func write(to: URL, metadata: MLModelMetadata?) throws](mltextclassifier/write(to:metadata:).md)
  Exports the text classifier as a Core ML model file at the specified URL.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mltextclassifier/write(tofile:metadata:).md)
  Exports the text classifier as a Core ML model file at the specified file path.
### Describing a text classifier
- [var model: MLModel](mltextclassifier/model.md)
  The underlying Core ML model of the text classifier.
- [var description: String](mltextclassifier/description.md)
  A text representation of the text classifier.
- [var debugDescription: String](mltextclassifier/debugdescription.md)
  A text representation of the text classifier that’s suitable for output during debugging.
- [var playgroundDescription: Any](mltextclassifier/playgrounddescription.md)
  A description of the text classifier in a playground.
### Supporting types
- [MLTextClassifier.FeatureExtractorType](mltextclassifier/featureextractortype.md)
  The text feature extractor type.
- [MLTextClassifier.ModelAlgorithmType](mltextclassifier/modelalgorithmtype.md)
  The type of algorithm that a text classifier uses.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mltextclassifier/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mltextclassifier/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mltextclassifier/customstringconvertible-implementations.md)

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
- [struct MLWordTagger](mlwordtagger.md)
  A word-tagging model you train to classify natural language text at the word level.
- [struct MLGazetteer](mlgazetteer.md)
  A collection of terms and their labels, which augments a tagger that analyzes natural language text.
- [struct MLWordEmbedding](mlwordembedding.md)
  A map of strings in a vector space that enable your app to find similar strings by looking at a string’s neighbors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier)*