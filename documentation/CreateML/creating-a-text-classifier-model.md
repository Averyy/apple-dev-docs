# Creating a text classifier model

**Framework**: Create ML

Train a machine learning model to classify natural language text.

#### Overview

A text classifier is a machine learning model that’s been trained to recognize patterns in natural language text, like the sentiment expressed by a sentence.

![Diagram showing how a text string maps to a label.](https://docs-assets.developer.apple.com/published/8b58fe67739dc2f7f3bb472ed54312b3/creating-a-text-classifer-model-1%402x.png)

You train a text classifier by showing it lots of examples of text you’ve already labeled—for example, movie reviews that you’ve already labeled as positive, negative, or neutral.

![Diagram showing how you train a text classifier with Create ML using training data.](https://docs-assets.developer.apple.com/published/928f87b97f9f6bea77d959ecc545107a/creating-a-text-classifer-model-2%402x.png)

##### Import Your Data

Start by gathering textual data and importing it into an [`MLDataTable`](mldatatable.md) instance. You can create a data table from JSON and CSV formats. Or, if your textual data is in a collection of files, you can sort them into folders, using the folder names as labels, similar to the image data source used in [`Creating an Image Classifier Model`](creating-an-image-classifier-model.md).

As an example, consider a JSON file containing movie reviews that you’ve categorized by sentiment. Each entry contains a pair of keys, the `text` and the `label`. The values of those keys are the input samples used to train your model. The JSON snippet below shows three pairs of sentences with their sentiment labels.

```javascript
// JSON file
[
    {
        "text": "The movie was fantastic!",
        "label": "positive"
    }, {
        "text": "Very boring. Fell asleep.",
        "label": "negative"
    }, {
        "text": "It was just OK.",
        "label": "neutral"
    } ...
]
```

In a macOS playground, create a data frame using the [`TabularData`](https://developer.apple.com/documentation/TabularData) framework.

```swift
import TabularData

let data = try DataFrame(contentsOfJSONFile: URL(fileURLWithPath: "<#/path/to/read/data.json#>"))
```

The resulting data frame has two columns, named  and , derived from the keys in the JSON file. The column names can be anything, as long as they are meaningful to you, because you’ll use them as parameters in other methods.

##### Prepare Your Data for Training and Evaluation

The data you use to train your model needs to be different from the data you use to evaluate your model. Use the [`stratifiedSplit(on:by:randomSeed:)`](https://developer.apple.com/documentation/TabularData/DataFrameProtocol/stratifiedSplit(on:by:randomSeed:)-9iauf) method to split your data into two data frames, one for training and the other for testing. The training data frame contains the majority of your data, and the testing data frame contains the remaining 20 percent.

```swift
let (trainingData, testingData) = data.stratifiedSplit(on: "text", by: 0.8)
```

##### Choose Model Training Parameters

You can use model training parameters to control the learning process. Choose a classifier algorithm type by specifying the [`MLTextClassifier.ModelAlgorithmType`](mltextclassifier/modelalgorithmtype.md) parameter. The [`MLTextClassifier.ModelAlgorithmType.maxEnt(revision:)`](mltextclassifier/modelalgorithmtype/maxent(revision:).md) algorithm trains quickly and performs well for a wide variety of data. It’s a good starting point algorithm while you’re exploring your data and models.

You can choose a transfer learning algorithm, [`MLTextClassifier.ModelAlgorithmType.transferLearning(_:revision:)`](mltextclassifier/modelalgorithmtype/transferlearning(_:revision:).md).  Transfer learning models use a pre-trained model as a feature extractor, you specify the `MLTextClassifier.FeatureExtractorType`. Transfer learning models can take longer to train, but can improve accuracy because the baseline model has already been trained on a large amount of text in a specific language.

If your data contains multiple languages, choose either the maximum entropy algorithm [`MLTextClassifier.ModelAlgorithmType.maxEnt(revision:)`](mltextclassifier/modelalgorithmtype/maxent(revision:).md) or the transfer learning algorithm [`MLTextClassifier.ModelAlgorithmType.transferLearning(_:revision:)`](mltextclassifier/modelalgorithmtype/transferlearning(_:revision:).md) and set its `MLTextClassifier.FeatureExtractorType` to the Bidirectional Encoder Representations from Transformers (BERT) embedding feature extractor [`MLTextClassifier.FeatureExtractorType.bertEmbedding`](mltextclassifier/featureextractortype/bertembedding.md).

If your data contains a single language, use the conditional random fields algorithm [`MLTextClassifier.ModelAlgorithmType.crf(revision:)`](mltextclassifier/modelalgorithmtype/crf(revision:).md) or the transfer learning algorithm [`MLTextClassifier.ModelAlgorithmType.transferLearning(_:revision:)`](mltextclassifier/modelalgorithmtype/transferlearning(_:revision:).md) and set its `MLTextClassifier.FeatureExtractorType` to the Embeddings from Language Models (ELMo) embedding feature extractor [`MLTextClassifier.FeatureExtractorType.elmoEmbedding`](mltextclassifier/featureextractortype/elmoembedding.md).

Use the [`MLTextClassifier.ModelParameters.ValidationData`](mltextclassifier/modelparameters-swift.struct/validationdata-swift.enum.md) parameter to specify the evaluation data that’s held out from training your model. During the training process, use the validation data to estimate your model’s ability to correctly classify new examples. Depending on the validation accuracy, the classifier algorithm might adjust values within the model — or stop the training process, if the accuracy is high enough. Since the split of your data is random, you might get a different result each time you train your model.

```swift
let parameters = MLTextClassifier.ModelParameters(
    validation: .split(strategy: .automatic),
    algorithm: .transferLearning(.bertEmbedding, revision: 1),
    language: .english
)
```

##### Create and Train a Text Classifier

Create an instance of [`MLTextClassifier`](mltextclassifier.md) with your training data frame and the column names.

```swift
let sentimentClassifier = try MLTextClassifier(
    trainingData: trainingData,
    textColumn: "text",
    labelColumn: "label",
    parameters: parameters
)
```

To measure how accurately the model (`sentimentClassifier`) performs on the training and validation data, use the [`classificationError`](mlclassifiermetrics/classificationerror.md) properties of the model’s [`trainingMetrics`](mltextclassifier/trainingmetrics.md) and [`validationMetrics`](mltextclassifier/validationmetrics.md) properties.

```swift
// Calculate training accuracy as a percentage.
let trainingAccuracy = (1.0 - sentimentClassifier.trainingMetrics.classificationError) * 100

// Calculate validation accuracy as a percentage.
let validationAccuracy = (1.0 - sentimentClassifier.validationMetrics.classificationError) * 100
```

##### Evaluate a Classifiers Accuracy

Next, evaluate your trained model’s performance by testing it against sentences it’s never seen before. Pass your testing data frame to the [`evaluation(on:)`](mltextclassifier/evaluation(on:)-8ch4k.md) method, which returns an [`MLClassifierMetrics`](mlclassifiermetrics.md) instance.

```swift
let evaluationMetrics = sentimentClassifier.evaluation(on: testingData, textColumn: "text", labelColumn: "label")
```

To get the evaluation accuracy, use the [`classificationError`](mlclassifiermetrics/classificationerror.md) property of the returned [`MLClassifierMetrics`](mlclassifiermetrics.md) instance.

```swift
// Calculate evaluation accuracy as a percentage.
let evaluationAccuracy = (1.0 - evaluationMetrics.classificationError) * 100
```

If the evaluation performance isn’t good enough, you may need to retrain with more data or make other adjustments. For information about improving model performance, see [`Improving Your Model’s Accuracy`](improving-your-model-s-accuracy.md).

##### Save a Core Ml Model

When your model is performing well enough, you’re ready to save it so you can use it in your app. Use the [`write(to:metadata:)`](mltextclassifier/write(to:metadata:).md) method to write the Core ML model file to disk. Provide any information about the model, like its author, version, or description in an [`MLModelMetadata`](mlmodelmetadata.md) instance.

```swift
let metadata = MLModelMetadata(author: "John Appleseed",
                               shortDescription: "A model trained to classify movie review sentiment",
                               version: "1.0")

try sentimentClassifier.write(to: URL(fileURLWithPath: "<#/path/to/save/SentimentClassifier.mlmodel#>"),
                              metadata: metadata)
```

Specify the file name using the `fileURLWithPath:` parameter, in the above code, `SentimentClassifier.mlmodel`.

##### Add a Core Ml Model to Your App

With your app open in Xcode, drag the `SentimentClassifier.mlmodel` file into the navigation pane. Xcode compiles the model and generates a `SentimentClassifier` class for use in your app. Select the `SentimentClassifier.mlmodel` file in Xcode to view additional information about the model.

Create an [`NLModel`](https://developer.apple.com/documentation/NaturalLanguage/NLModel) in the Natural Language framework from the `SentimentClassifier` to ensure that the tokenization is consistent between training and deployment. Then use [`predictedLabel(for:)`](https://developer.apple.com/documentation/NaturalLanguage/NLModel/predictedLabel(for:)) to generate predictions on new text inputs.

```swift
import NaturalLanguage
import CoreML

let mlModel = try SentimentClassifier(configuration: MLModelConfiguration()).model

let sentimentPredictor = try NLModel(mlModel: mlModel)
sentimentPredictor.predictedLabel(for: "It was the best I've ever seen!")
```

## See Also

- [struct MLTextClassifier](mltextclassifier.md)
  A model you train to classify natural language text.
- [struct MLWordTagger](mlwordtagger.md)
  A word-tagging model you train to classify natural language text at the word level.
- [struct MLGazetteer](mlgazetteer.md)
  A collection of terms and their labels, which augments a tagger that analyzes natural language text.
- [struct MLWordEmbedding](mlwordembedding.md)
  A map of strings in a vector space that enable your app to find similar strings by looking at a string’s neighbors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/creating-a-text-classifier-model)*