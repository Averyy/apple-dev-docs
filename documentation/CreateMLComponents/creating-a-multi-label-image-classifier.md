# Creating a multi-label image classifier

**Framework**: Create ML Components

Train a machine learning model to assign multiple labels to an image.

#### Overview

A single-label image classifier takes an input image and assigns one label, which helps identify the most relevant subject in the image. However, there’s often additional information and context in an image that identifying the most relevant subject doesn’t consider. A multi-label image classifier takes an input image and assigns multiple labels. A multi-label classifier is better at describing an image where there are multiple subjects, or when the environment is relevant.

Training a multi-label image classifier is similar to training a single-label image classifier. You collect and label images, build an estimator pipeline, train and evaluate the model, and export the model to use with [`Vision`](https://developer.apple.com/documentation/Vision). For more information about single-label image classifiers, see [`Creating an Image Classifier Model`](https://developer.apple.com/documentation/CreateML/creating-an-image-classifier-model).

##### Prepare Your Training Data

First, collect images and assign labels. Put all images in a folder and create a JSON file in the same folder. For example if you have two images, then your folder contains three files: `image1.jpg`, `image2.jpg`, and `annotations.json`. The JSON file contains the labels for each image. The following example includes possible labels for two images: `image1.jpg` is an image of a potted aloe plant on a window sill and `image2.jpg` is an image of a potted cactus with a person standing next to it.

```json
[
    {
        "filename": "image1.jpg",
        "annotations": ["window_sill", "aloe", "pot"]
    },
    {
        "filename": "image2.jpg",
        "annotations": ["cactus", "pot", "person"]
    }
]
```

Create a [`Decodable`](https://developer.apple.com/documentation/Swift/Decodable) structure and populate it with the file names and labels from your JSON file. Then, convert them to an [`AnnotatedFeature`](annotatedfeature.md) structure.

```swift
// Define an annotation.
struct AnnotatedFile: Decodable {
    var filename: String
    var annotations: Set<String>
}

// Specify the input directory.
let directoryURL = URL(filePath: "/path/to/files", directoryHint: .isDirectory)

// Decode the annotations.
let decoder = JSONDecoder()
let data = try Data(contentsOf: directory.appending(component: "annotations.json"))
let annotatedFiles = try decoder.decode([AnnotatedFile].self, from: data)

// Convert the annotations to an array of `AnnotatedFeature`.
let annotatedFeatures = annotatedFiles.map {
    AnnotatedFeature(
        feature: directory.appending(component: $0.filename),
        annotation: $0.annotations
    )
}
```

##### Build a Multi Label Estimator Pipeline

After preparing your training data, you can create your estimator pipeline. When using Create ML Components, you compose estimators and transformers into pipelines that you can train to produce models. As with a single-label image classifier, use an image reader and a feature extractor. But the last component is a [`FullyConnectedNetworkMultiLabelClassifier`](fullyconnectednetworkmultilabelclassifier.md) instead of a [`FullyConnectedNetworkClassifier`](fullyconnectednetworkclassifier.md).

```swift
// List all the labels.
let labels = ["aloe", "cactus", "person", "pot", "window_sill"]

// Compose the estimator.
let estimator = ImageReader()
    .appending(ImageFeaturePrint())
    .appending(FullyConnectedNetworkMultiLabelClassifier<Float, String>(labels: labels))
```

##### Train and Evaluate the Model

When you validate as you train, you can stop training when the validation metrics stop improving. So set aside some of the images for validation. Then, call the [`fitted(to:validateOn:eventHandler:)`](supervisedestimator/fitted(to:validateon:eventhandler:).md) method to train.

```swift
let (training, validation) = annotatedFeatures.annotatedFiles.randomSplit(by: 0.8)
let model = try await estimator.fitted(
    to: training,
    validateOn: validation
)
```

After training the model, evaluate it using test images. The mean-average precision (MAP) is a good measure for a multi-label classifier.

```swift
let predicted = try await model.prediction(from: testAnnotatedFiles)
let metrics = try MultiLabelClassificationMetrics(
    classifications: predicted.map(\.prediction),
    groundTruth: predicted.map(\.annotation),
    strategy: .balancedPrecisionAndRecall,
    labels: labels
)
print(metrics.meanAveragePrecision)
```

##### Export the Model to Use with Vision

After you train the model, you can export it as a [`Core ML`](https://developer.apple.com/documentation/CoreML) model.

```swift
// Export to Core ML
let modelURL = URL(filePath: "/path/to/model")
try model.export(to: modelURL)
```

Then, use [`Vision`](https://developer.apple.com/documentation/Vision) to classify images in your app.

```swift
import Vision
import CoreML

let handler = VNImageRequestHandler(url: URL(filePath: "image.jpg"))
let visionModel = try VNCoreMLModel(for: compiledModel)
let request = VNCoreMLRequest(model: visionModel)
try handler.perform([request])
if let observations = request.results as? [VNClassificationObservation] {
    // Filter observations using a target precision and recall.
    let filteredObservations = observations.filter {
        $0.hasMinimumPrecision(0.3, forRecall: 0.7)
    }
    // Use observations.
}
```

The observations include all labels and their probabilities. This includes labels for which the model predicted a low probability. Including all observations results in high recall but low precision, in other words, your model prioritizes predicting additional labels. To balance the precision and recall, include only the labels that have a high probability. To do this you can choose a probability threshold for each label, or use one of the methods from [`Vision`](https://developer.apple.com/documentation/Vision). The [`hasMinimumPrecision(_:forRecall:)`](https://developer.apple.com/documentation/Vision/VNClassificationObservation/hasMinimumPrecision(_:forRecall:)) and [`hasMinimumRecall(_:forPrecision:)`](https://developer.apple.com/documentation/Vision/VNClassificationObservation/hasMinimumRecall(_:forPrecision:)) methods allow you to choose only observations that strike a specific balance between precision and recall.

## See Also

- [Augmenting images to expand your training data](augmenting-images-to-expand-your-training-data.md)
  Improve your model by using transformed versions of your training images.
- [struct ImageReader](imagereader.md)
  An image file reader.
- [protocol ImageFeatureExtractor](imagefeatureextractor.md)
  A transformer that takes an image and outputs image features.
- [struct ImageCropper](imagecropper.md)
  An image crop transformer.
- [struct ImageScaler](imagescaler.md)
  An image scaling transformer.
- [struct ImageFeaturePrint](imagefeatureprint.md)
  ImageFeaturePrint image feature extractor.
- [struct ImageBlur](imageblur.md)
  An image blurring transformer.
- [struct ImageColorTransformer](imagecolortransformer.md)
  An image color transformer.
- [struct ImageExposureAdjuster](imageexposureadjuster.md)
  An image exposure adjusting transformer.
- [struct ImageFlipper](imageflipper.md)
  An image flipper transformer.
- [struct ImageRotator](imagerotator.md)
  An image rotating transformer.
- [struct RandomImageNoiseGenerator](randomimagenoisegenerator.md)
  A transformer that adds random noise to an image.
- [struct MLModelImageFeatureExtractor](mlmodelimagefeatureextractor.md)
  An image feature extractor provided by an MLModel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/creating-a-multi-label-image-classifier)*