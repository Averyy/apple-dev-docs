# Creating an Image Classifier Model

**Framework**: Createml

Train a machine learning model to classify images, and add it to your Core ML app.

#### Overview

An  is a machine learning model that recognizes images. When you give it an image, it responds with a category label for that image.

![A flow diagram showing how an image classifier predicts the label, Giraffe, from an image of a giraffe.](https://docs-assets.developer.apple.com/published/7c6d96174f8701c5d2402beed64563cc/creating-an-image-classifier-model-1%402x.png)

You train an image classifier by showing it many examples of images you’ve already labeled. For example, you can train an image classifier to recognize animals by gathering photos of elephants, giraffes, lions, and so on.

![A flow diagram showing images of animals going into Create ML, which then produces an image classifier Core ML model file.](https://docs-assets.developer.apple.com/published/43b7b6573341efcb1184f5998a570435/creating-an-image-classifier-model-2%402x.png)

After the image classifier finishes training, you assess its accuracy and, if it performs well enough, save it as a Core ML model file. You then import the model file into your Xcode project to use the image classifier in your app.

##### Gather Your Data

Use at least 10 images per category, but keep in mind that an image classifier performs better with a more diverse set of images. Consider including images of each category from multiple angles and in different lighting conditions.

Balance the number of images for each category. For example, don’t use 10 images for one category and then 1000 images for another.

The images can be in any format you can open in the Quicktime Player, such as JPEG and PNG. They don’t have to be a particular size, nor do they need to be the same size as each other. However, it’s best to use images that are at least 299 x 299 pixels.

If possible, gather images that best represent what you expect the model to see when you use it in your app. For example, if your app classifies images from a device’s camera in an outdoor setting, gather outdoor images from an identical or similar camera.

> **Note**: By default, the image classifier uses the scene print feature extractor to accelerate the training process and works best with real-world objects. For more information, see [`MLImageClassifier.FeatureExtractorType.scenePrint(revision:)`](mlimageclassifier/featureextractortype/sceneprint(revision:).md).

##### Organize Your Training Data

Prepare a training dataset by sorting the images into subfolders. Give each subfolder a name for the category of images contained within it. For example, you might use the label `Cheetah` for all the images of cheetahs.

![A diagram showing a folder called Training Data with subfolders that are named using the label corresponding to the category of images they contain. For example, all the cheetah images go into a subfolder named, Cheetah.](https://docs-assets.developer.apple.com/published/0a419b23cc4238d4b0a2baee09d2f4ea/creating-an-image-classifier-model-3%402x.png)

##### Organize Your Testing Data

Testing your model with a testing dataset is a quick way to see how well your trained model might perform in the real world.

If your dataset has enough images, say 25 or more per category, create a testing dataset by duplicating the folder structure of the training dataset. Then move about 20 percent of the images from each category into the equivalent category folder in the testing dataset.

##### Create an Image Classifier Project

Use Create ML to create an image classifier project. With Xcode open, Control-click the Xcode icon in the Dock and choose Open Developer Tool > Create ML. Or, from the Xcode menu, choose Open Developer Tool > Create ML.

In Create ML, choose File > New Project to see the list of model templates. Select Image Classification and click Next.

![A screenshot of the Create ML project template window that has the Image Classification template selected. Other templates in the window include Style Transfer, Action Classification, Sound Classification, and Tabular Regression.](https://docs-assets.developer.apple.com/published/bcec307ffcea638a98721a2178b9ee77/creating-an-image-classifier-model-4%402x.png)

Change the project’s default name to a more meaningful one. If applicable, enter additional information for the models that come from this project, such as one or more authors and a short description.

![A screenshot of the new project options window with text fields for Project Name, Author, License, and Description. The first text fields have the values Animal Classifier, Maria Ruiz, and No license provided, respectively. The description text field reads, An image classification machine learning model that recognizes animals.](https://docs-assets.developer.apple.com/published/37e7674a1b5d8a07422cfdc99d6a9a33/creating-an-image-classifier-model-5%402x.png)

##### Configure the Training Session

Drag the folder with your training dataset into the Training Data well in the project window.

![A screenshot of the project window in the Settings tab that shows the user dragging a Finder folder named Training Data onto the Training Data area.](https://docs-assets.developer.apple.com/published/1d0270e05db222c3bdcb256eaf8e3893/creating-an-image-classifier-model-6%402x.png)

If applicable, drag the folder with your testing dataset into the Testing Data well in the project window.

![A screenshot of the project window in the Settings tab that shows the user dragging a Finder folder named Testing Data onto the Testing Data area. ](https://docs-assets.developer.apple.com/published/32ba5e3473a5edc9088be6314f99b79a/creating-an-image-classifier-model-7%402x.png)

You can adjust the following parameters before training your image classifier:

![A screenshot of the project window in the Settings tab that highlights the Parameters section. The Feature Extractor is set to Image Feature Print V2. The Iterations parameter setting is set to 50 and the Augmentations setting has 6 checkboxes named, Add Noise, Blur, Crop, Expose, Flip, and Rotate.](https://docs-assets.developer.apple.com/published/7df3c337506bafe1f56fd2a6671f3e5d/creating-an-image-classifier-model-8%402x.png)

##### Train the Image Classifier

Click the Train button to start the training session. Create ML begins the session by quickly separating some of your training data into a validation dataset. Next, Create ML extracts features, such as edges, corners, textures, and regions of color, from the remaining training images. Create ML uses the images’ features to iteratively train the model and then checks its accuracy with the validation dataset.

![A screenshot of the project window in the Training tab showing a line graph of the model’s accuracy vs. the number of training iterations. The line generally progresses upward toward 100% and after 25 iterations ending at 100% and 97.5% for training and validation accuracy, respectively.](https://docs-assets.developer.apple.com/published/01ed3f16d8fb987b51695b50c63371c4/creating-an-image-classifier-model-9%402x.png)

Create ML shows its progress in a graph, where the black and gray lines represent the model’s accuracy with the training and validation datasets, respectively.

##### Assess the Models Accuracy

When Create ML finishes training the model, it tests the model using the testing dataset. When it’s finished testing the model, Create ML shows the training, validation, and testing accuracy scores in the Evaluation tab. Models typically have higher accuracy scores on the training dataset because it learned from those images. In this example, the image classifier model correctly identified:

- 100 percent of the training images
- 95 percent of the validation images
- 97 percent of the testing images

![A screenshot of the project window in the Evaluation tab showing a table of the testing dataset with columns named, Class, Item Count, Precision, and Recall. The table is sorted by Precision in descending order, and the first row has the values, Giraffe, 9, 100%, and 100%, respectively.](https://docs-assets.developer.apple.com/published/97c4586d7483e9b6020cfb1707ab575a/creating-an-image-classifier-model-10%402x.png)

 is the number of true positives divided by the sum of true positives and false positives.  is the number of true positives divided by the sum of true positives and false negatives.

If the evaluation performance isn’t good enough, you may need to train a new model with a dataset that has more variety. For example, you can gather additional images from new angles or in new environments, or add one or more image augmentation options. For details about evaluating a model, as well as strategies for improving the model’s performance, see [`Improving Your Model’s Accuracy`](improving-your-model-s-accuracy.md).

##### Preview the Model

Click the Preview tab to try out the model with images it hasn’t seen before. To see the model’s predictions, drag image files to the column below the Train button.

![A screenshot of the project window in the Preview tab that predicts an image of an elephant as, elephant, with 100% confidence.](https://docs-assets.developer.apple.com/published/ef1d1eea81eeb237b95a654d86f39f33/creating-an-image-classifier-model-11%402x.png)

##### Save the Model

When you’re satisfied with the model’s performance, save it to the file system (in a Core ML format). From the Output tab, save the model using any of these options:

- Click the Save button to save the model to the file system.
- Click the Export button to open the model in Xcode.
- Click the Share button to send the model to someone else, such as through Mail or Messages.
- Drag the model’s icon anywhere that accepts a file.

![A screenshot of the project window in the Output tab showing a model save dialog after the user clicked the Get-button. The Get-button’s icon is a box with a down arrow leading into it.](https://docs-assets.developer.apple.com/published/7f83e09c032cbc1e776922609f55362a/creating-an-image-classifier-model-12%402x.png)

##### Add the Model to Your App

The last step is to add your trained model to an Xcode project. For example, your image classifier model can replace the model in the [`Classifying Images with Vision and Core ML`](https://developer.apple.com/documentation/coreml/model_integration_samples/classifying_images_with_vision_and_core_ml) sample.

Download the sample and open the project in Xcode. Drag your model file into the navigation pane. Xcode adds the model to your project and shows you the model’s metadata, operating system availability, class labels, and so on.

![A screenshot of the sample code project open in Xcode showing the Animal Classifier model in the editor view.](https://docs-assets.developer.apple.com/published/ebaa8ae6231ff7c7187ac51fe51256c8/creating-an-image-classifier-model-13%402x.png)

To use your model in code, you only need to change one line. The project instantiates the MobileNet model in exactly one place in the `ImagePredictor` class.

```swift
// Create an instance of the image classifier's wrapper class.
let imageClassifierWrapper = try? MobileNet(configuration: defaultConfig)
```

Change this line to use your image classification model class instead:

```swift
// Create an instance of the image classifier's wrapper class.
let imageClassifierWrapper = try? AnimalClassifier(configuration: defaultConfig)
```

These models are interchangeable because both take an image as input, and both output a label string. With your model substitution, the sample app classifies images as before, except now it uses your model and its associated labels.

##### Automate Model Training and Assessment

You can use Create ML to train a useful image classifier with very little code or machine learning expertise, as described in the sections above. However, you can also use an [`MLImageClassifier`](mlimageclassifier.md) instance to script the model training process. The general tasks are the same: prepare data, train a model, assess performance, and save the Core ML model file. The difference is that you do everything programmatically.

For example, you can initialize two [`MLImageClassifier.DataSource`](mlimageclassifier/datasource.md) instances, one for the training dataset and another for the testing dataset. Use the training data source to initialize an image classifier with [`init(trainingData:parameters:)`](mlimageclassifier/init(trainingdata:parameters:)-4r6hr.md). Then use the testing data source with its [`evaluation(on:)`](mlimageclassifier/evaluation(on:)-9p8mi.md) method, and assess the values in the [`MLClassifierMetrics`](mlclassifiermetrics.md) instance it returns.

## See Also

- [struct MLImageClassifier](mlimageclassifier.md)
  A model you train to classify images.
- [struct MLObjectDetector](mlobjectdetector.md)
  A model you train to classify one or more objects within an image.
- [struct MLHandPoseClassifier](mlhandposeclassifier.md)
  A task that creates a hand pose classification model by training with images of people’s hands that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CreateML/creating-an-image-classifier-model)*