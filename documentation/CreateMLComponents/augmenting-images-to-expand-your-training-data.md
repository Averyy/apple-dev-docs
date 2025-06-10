# Augmenting images to expand your training data

**Framework**: Create ML Components

Improve your model by using transformed versions of your training images.

#### Overview

Training a good image model requires a variety of training images with different characteristics. If you’re training an image classifier to recognize flowers you can improve classification accuracy by providing flower photos with a variety of lighting conditions, angles, and backgrounds. However, collecting and labeling images is a time-consuming process.

To maximize the potential impact of your data you can use image augmentations. Augmenting images is the process of applying transformations such as flipping, cropping, resizing, adjusting brightness, adding noise, and so on. Image augmentations are not a replacement for a good image data set, but they help maximize the data set’s effectiveness. Each augmentation has the potential to multiply the size of your training data which is helpful when your training sample size is small.

![Diagram that shows an image with arrows pointing to variations of it. Variations include a cropped image, a resized image, a faded image, and an image with added noise.](https://docs-assets.developer.apple.com/published/8a1b64ac2d8e78eb0405e12ac466c976/image_augmentation%402x.png)

Keep in mind that performing augmentations has some drawbacks. You can’t reuse extracted features across training iterations because each iteration produces a new set of augmented images. This increase in training time can be significant. Augmentations have the most impact when your dataset is small relative to the number of parameters in your model.

##### Write an Augmentation

You can use [`Augmenter`](augmenter.md) to create a custom augmentation. The augmenter applies each transformer to each image in sequence. For example, this augmenter randomly flips (with 50% probability) and then randomly crops images:

```swift
let augmenter = Augmenter {
    ApplyRandomly(probability: 0.5) {
        ImageFlipper(orientation: .horizontal)
    }
    RandomImageCropper(scale: 0.8 ..< 0.9, aspectRatio: 1.0)
}
```

To generate a random number each time, use [`UniformRandomFloatingPointParameter`](uniformrandomfloatingpointparameter.md). You can use the random number with any transformer. For instance, to perform a slight rotation using [`ImageRotator`](imagerotator.md):

```swift
let augmenter = Augmenter {
    ApplyRandomly(probability: 0.5) {
        ImageFlipper(orientation: .horizontal)
    }
    UniformRandomFloatingPointParameter(range: -10.0 ... 10.0) { angle in
        ImageRotator(angle: angle * .pi / 180)
    }
    RandomImageCropper(scale: 0.8 ..< 0.9, aspectRatio: 1.0)
}
```

##### Apply Augmentations to Your Training Data

After you create an augmenter, you can use it to augment your training data. You do this with the [`applied(to:)`](augmenter/applied(to:).md) method:

```swift
let augmentedTrainingData = augmenter.applied(to: trainingData)
```

Because augmentations are usually random, it makes sense to do more than one pass over your training data. Each pass results in a different set of images, for instance with different scale factors. You can control the number of passes by using the [`applied(to:upsampledBy:)`](augmenter/applied(to:upsampledby:).md) method. For instance, to get 10 times the number of images:

```swift
let augmentedTrainingData = augmenter.applied(
   to: trainingData,
   upsampledBy: 10
)
```

> **Note**: The result of the augmentations is an asynchronous sequence. The augmenter doesn’t perform augmentations until you request them to avoid the memory overhead.

##### Train an Image Classifier

You can now use your augmented data set to train an image classifier. Because augmentations take images, not URLs, you may need to read your files first.

```swift
let reader = ImageReader().adaptedAsAnnotatedFeatureTransformer(annotationType: String.self)
let trainingImages = try await reader.applied(to: trainingFiles)
let validationImages = try await reader.applied(to: validationFiles)
```

Now that you have annotated images, the next step is to create your pipeline. For an image classifier, create a feature extractor and a classifier.

```swift
let featurePrint = ImageFeaturePrint(revision: 2)
let classifier = FullyConnectedNetworkClassifier<Float, String>(labels: labels, configuration: configuration)
let task = featurePrint.appending(classifier)
```

Next, create the augmenter that transforms the training images.

```swift
let augmenter = Augmenter {
    ApplyRandomly(probability: 0.5) {
        ImageFlipper(orientation: .horizontal)
    }
    UniformRandomFloatingPointParameter(range: -10.0 ... 10.0) { angle in
        ImageRotator(angle: angle * .pi / 180)
    }
    RandomImageCropper(scale: 0.8 ..< 0.9, aspectRatio: 1.0)
}
```

Finally, create a model, apply the augmenter to the training data, and progressively train the model using [`update(_:with:eventHandler:)`](updatablesupervisedestimator/update(_:with:eventhandler:).md). The following example applies the `augmenter` to the `trainingImages` and updates the `model` up to 100 times:

```swift
var model = task.makeTransformer()
for iteration in 0 ..< 100 {
    // Perform one training iteration.
    let augmentedData = augmenter.applied(to: trainingImages.shuffled())
    for try await batch in augmentedData.batches(ofSize: 32, dropsLastPartialBatch: false) {
        try await task.update(&model, with: batch)
    }

    // Compute accuracy on validation data, stop when done.
    // ...
}
```

The example above applies the `augmenter` to shuffled images. Shuffling images creates more variation, which helps prevent over-fitting. The example breaks the data into batches after each augmentation, and updates the model with each `batch`. Using a smaller batch size typically produces a better model, while using a larger batch size can speed up training.

> 💡 **Tip**: A batch size of 32 is often a good starting point.

##### Stop Training

Training your model progressively using the [`update(_:with:eventHandler:)`](updatablesupervisedestimator/update(_:with:eventhandler:).md) method lets you control when to stop training. Stop training when the validation accuracy stops improving, for example:

```swift
var accuracies = [Double](repeating: 0, count 5)
for iteration in 0 ..< 100 {
    // Perform one training iteration.
    // ...

    // Compute the accuracy on the validation data.
    let predictions = try await model.prediction(from: validationImages)
    let validationMetrics = ClassificationMetrics(
        predictions.map(\.prediction.mostLikelyLabel),
        predictions.map(\.annotation)
    )
    let validationAccuracy = validationMetrics.accuracy

    // Save the accuracy in a circular buffer.
    metrics[iteration % accuracies.count] = validationAccuracy

    // Stop when there has been no significant improvement in the last 5 iterations.
    if accuracies.allSatisfy({ $0 >= validationAccuracy - 0.01 }) {
        break
    }
}
```

## See Also

- [struct Augmenter](augmenter.md)
  An augmenter.
- [struct ApplyEachRandomly](applyeachrandomly.md)
  Applies each transformer randomly given a probability.
- [struct ApplyRandomly](applyrandomly.md)
  Randomly applies the transformer with the given probability.
- [struct ChooseRandomly](chooserandomly.md)
  Apply single transformation randomly chosen from a list of transformers.
- [struct RandomImageCropper](randomimagecropper.md)
  Crops an image at a random location.
- [protocol RandomTransformer](randomtransformer.md)
  A transformer that takes an input and a random number generator and produces a randomized output.
- [struct ShuffleRandomly](shufflerandomly.md)
  Apply transformations in a random order.
- [struct UniformRandomFloatingPointParameter](uniformrandomfloatingpointparameter.md)
  Applies the transformer with a randomly generated input parameter.
- [class UniformRandomIntegerParameter](uniformrandomintegerparameter.md)
  Applies the transformer with a randomly generated input parameter.
- [Creating a multi-label image classifier](creating-a-multi-label-image-classifier.md)
  Train a machine learning model to assign multiple labels to an image.
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/augmenting-images-to-expand-your-training-data)*