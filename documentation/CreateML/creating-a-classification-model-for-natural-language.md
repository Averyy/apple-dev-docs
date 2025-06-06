# Creating a Text Classifier Model

**Framework**: Create ML

Train a machine learning model to classify natural language text.

#### Overview

A text classifier is a machine learning model that’s been trained to recognize patterns in natural language text, like the sentiment expressed by a sentence.

![Diagram showing how a text string maps to a label.](https://docs-assets.developer.apple.com/published/8b58fe67739dc2f7f3bb472ed54312b3/creating-a-classification-model-for-natural-language-1%402x.png)

You train a text classifier by showing it lots of examples of text you’ve already labeled—for example, movie reviews that you’ve already labeled as positive, negative, or neutral.

![Diagram showing how you train a text classifier with Create ML using training data.](https://docs-assets.developer.apple.com/published/928f87b97f9f6bea77d959ecc545107a/creating-a-classification-model-for-natural-language-2%402x.png)

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

In a macOS playground, create the data table using the [`init(contentsOf:options:)`](mldatatable/init(contentsof:options:).md) method of [`MLDataTable`](mldatatable.md).

```swift
import CreateML

let data = try MLDataTable(contentsOf: URL(fileURLWithPath: "<#/path/to/read/data.json#>"))
```

The resulting data table has two columns, named  and , derived from the keys in the JSON file. The column names can be anything, as long as they are meaningful to you, because you’ll use them as parameters in other methods.

##### Prepare Your Data for Training and Evaluation

The data you use to train the model needs to be different from the data you use to evaluate the model. Use the [`randomSplit(by:seed:)`](mldatatable/randomsplit(by:seed:).md) method of [`MLDataTable`](mldatatable.md) to split your data into two tables, one for training and the other for testing. The training data table contains the majority of your data, and the testing data contains the remaining 10 to 20 percent.

```swift
let (trainingData, testingData) = data.randomSplit(by: 0.8, seed: 5)
```

##### Create and Train the Text Classifier

Create an instance of [`MLTextClassifier`](mltextclassifier.md) with your training data table and the names of your columns. Training begins right away.

```swift
let sentimentClassifier = try MLTextClassifier(trainingData: trainingData,
                                               textColumn: "text",
                                               labelColumn: "label")
```

During training, Create ML puts aside a small percentage of the training data to use for validating the model’s progress during the training phase. The validation data allows the training process to gauge the model’s performance on examples the model hasn’t been trained on. Depending on the validation accuracy, the training algorithm could adjust values within the model or even stop the training process, if the accuracy is high enough. Because the split is done randomly, you might get a different result each time you train the model.

To see how accurately the model performed on the training and validation data, use the [`classificationError`](mlclassifiermetrics/classificationerror.md) properties of the model’s [`trainingMetrics`](mltextclassifier/trainingmetrics.md) and [`validationMetrics`](mltextclassifier/validationmetrics.md) properties.

```swift
// Training accuracy as a percentage
let trainingAccuracy = (1.0 - sentimentClassifier.trainingMetrics.classificationError) * 100

// Validation accuracy as a percentage
let validationAccuracy = (1.0 - sentimentClassifier.validationMetrics.classificationError) * 100
```

##### Evaluate the Classifiers Accuracy

Next, evaluate your trained model’s performance by testing it against sentences it’s never seen before. Pass your testing data table to the [`evaluation(on:)`](mltextclassifier/evaluation(on:)-8ch4k.md) method, which returns an [`MLClassifierMetrics`](mlclassifiermetrics.md) instance.

```swift
let evaluationMetrics = sentimentClassifier.evaluation(on: testingData)
```

To get the evaluation accuracy, use the [`classificationError`](mlclassifiermetrics/classificationerror.md) property of the returned [`MLClassifierMetrics`](mlclassifiermetrics.md) instance.

```swift
// Evaluation accuracy as a percentage
let evaluationAccuracy = (1.0 - evaluationMetrics.classificationError) * 100
```

If the evaluation performance isn’t good enough, you may need to retrain with more data or make other adjustments. For information about improving model performance, see [`Improving Your Model’s Accuracy`](improving-your-model-s-accuracy.md).

##### Save the Core Ml Model

When your model is performing well enough, you’re ready to save it so you can use it in your app. Use the [`write(to:metadata:)`](mltextclassifier/write(to:metadata:).md) method to write the Core ML model file (`SentimentClassifier.mlmodel`) to disk. Provide any information about the model, like its author, version, or description in an [`MLModelMetadata`](mlmodelmetadata.md) instance.

```swift
let metadata = MLModelMetadata(author: "John Appleseed",
                               shortDescription: "A model trained to classify movie review sentiment",
                               version: "1.0")

try sentimentClassifier.write(to: URL(fileURLWithPath: "<#/path/to/save/SentimentClassifier.mlmodel#>"),
                              metadata: metadata)
```

##### Add the Model to Your App

With your app open in Xcode, drag the `SentimentClassifier.mlmodel` file into the navigation pane. Xcode compiles the model and generates a `SentimentClassifier` class for use in your app. Select the `SentimentClassifier.mlmodel` file in Xcode to view additional information about the model.

Create an [`NLModel`](https://developer.apple.com/documentation/NaturalLanguage/NLModel) in the Natural Language framework from the `SentimentClassifier` to ensure that the tokenization is consistent between training and deployment. Then use [`predictedLabel(for:)`](https://developer.apple.com/documentation/NaturalLanguage/NLModel/predictedLabel(for:)) to generate predictions on new text inputs.

```swift
import NaturalLanguage
import CoreML

let mlModel = try SentimentClassifier(configuration: MLModelConfiguration()).model

let sentimentPredictor = try NLModel(mlModel: mlModel)
sentimentPredictor.predictedLabel(for: "It was the best I've ever seen!")
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/creating-a-classification-model-for-natural-language)*