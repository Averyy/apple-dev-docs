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

- [Creating a Text Classifier Model](creating-a-classification-model-for-natural-language.md)
- [Creating a text classifier model](creating-a-text-classifier-model.md)

#### Overview

Use a text classifier to train a machine learning model you can include in your app to classify natural language text. The model learns to associate labels with features of the input text, which can be sentences, paragraphs, or even entire documents.

After you train a text classifier, you save it to a Core ML model file. You then use an instance of the [`NLModel`](https://developer.apple.com/documentation/NaturalLanguage/NLModel) class from the [`Natural Language`](https://developer.apple.com/documentation/NaturalLanguage) framework to read the model file into your app.

## Topics

### Creating and training a text classifier
- [init(trainingData: [String : [String]], parameters: MLTextClassifier.ModelParameters) throws](mltextclassifier/init(trainingdata:parameters:)-9uj3q.md)
  Creates a text classifier.
- [init(trainingData: DataFrame, textColumn: String, labelColumn: String, parameters: MLTextClassifier.ModelParameters) throws](mltextclassifier/init(trainingdata:textcolumn:labelcolumn:parameters:)-6keqn.md)
  Creates a text classifier.
- [init(trainingData: MLTextClassifier.DataSource, parameters: MLTextClassifier.ModelParameters) throws](mltextclassifier/init(trainingdata:parameters:)-8n8vs.md)
  Creates a text classifier.
- [MLTextClassifier.DataSource](mltextclassifier/datasource.md)
  A data source for a text classifier.
- [MLTextClassifier.ModelParameters](mltextclassifier/modelparameters-swift.struct.md)
  Parameters that specify model training parameters and validation data.
- [let modelParameters: MLTextClassifier.ModelParameters](mltextclassifier/modelparameters-swift.property.md)
  The configuration parameters that the text classifier used for training during initialization.
- [init(trainingData: MLDataTable, textColumn: String, labelColumn: String, parameters: MLTextClassifier.ModelParameters) throws](mltextclassifier/init(trainingdata:textcolumn:labelcolumn:parameters:)-7lp6w.md)
  Creates a text classifier.
### Assessing model accuracy
- [let trainingMetrics: MLClassifierMetrics](mltextclassifier/trainingmetrics.md)
  Measurements of the classifier’s performance on the training data set.
- [let validationMetrics: MLClassifierMetrics](mltextclassifier/validationmetrics.md)
  Measurements of the classifier’s performance on the validation data set.
### Evaluating a text classifier
- [func evaluation(on: MLTextClassifier.DataSource) -> MLClassifierMetrics](mltextclassifier/evaluation(on:)-8ch4k.md)
  Computes evaluation metrics.
- [func evaluation(on: DataFrame, textColumn: String, labelColumn: String) -> MLClassifierMetrics](mltextclassifier/evaluation(on:textcolumn:labelcolumn:)-2ibj8.md)
  Computes evaluation metrics.
- [func evaluation(on: [String : [String]]) -> MLClassifierMetrics](mltextclassifier/evaluation(on:)-3h6eu.md)
  Computes evaluation metrics.
- [func evaluation(on: MLDataTable, textColumn: String, labelColumn: String) -> MLClassifierMetrics](mltextclassifier/evaluation(on:textcolumn:labelcolumn:)-6emxa.md)
  Computes evaluation metrics.
### Testing a text classifier
- [func prediction(from: String) throws -> String](mltextclassifier/prediction(from:).md)
  Classifies a string with a label.
- [func predictions(from: [String]) throws -> [String]](mltextclassifier/predictions(from:)-1u3f2.md)
  Classifies an array of strings with labels.
- [func predictionWithConfidence(from: String) throws -> [String : Double]](mltextclassifier/predictionwithconfidence(from:).md)
  Predicts multiple possible labels and their confidence scores for the specified string.
- [func predictionsWithConfidence(from: [String]) throws -> [[String : Double]]](mltextclassifier/predictionswithconfidence(from:)-uezi.md)
  Predicts multiple possible labels and their confidence scores for each string in the specified array.
- [func predictions(from: MLDataColumn<String>) throws -> MLDataColumn<String>](mltextclassifier/predictions(from:)-40gtb.md)
  Classifies a data column with labels.
- [func predictionsWithConfidence(from: MLDataColumn<String>) throws -> MLDataColumn<[String : Double]>](mltextclassifier/predictionswithconfidence(from:)-1w9zo.md)
  Predicts multiple possible labels and their confidence scores for each string in the specified data column.
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
### Enumerations
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

## See Also

- [Creating a text classifier model](creating-a-text-classifier-model.md)
  Train a machine learning model to classify natural language text.
- [Creating a word tagger model](../NaturalLanguage/creating-a-word-tagger-model.md)
  Train a machine learning model to tag individual words in natural language text.
- [struct MLWordTagger](mlwordtagger.md)
  A word-tagging model you train to classify natural language text at the word level.
- [struct MLGazetteer](mlgazetteer.md)
  A collection of terms and their labels, which augments a tagger that analyzes natural language text.
- [struct MLWordEmbedding](mlwordembedding.md)
  A map of strings in a vector space that enable your app to find similar strings by looking at a string’s neighbors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier)*