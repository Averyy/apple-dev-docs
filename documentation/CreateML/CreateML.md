# Create ML

**Framework**: Create ML  
**Kind**: module

Create machine learning models for use in your app.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

#### Overview

Use Create ML with familiar tools like Swift and macOS playgrounds to create and train custom machine learning models on your Mac. You can train models to perform tasks like recognizing images, extracting meaning from text, or finding relationships between numerical values.

![Diagram showing how you use images, text, and other structured data with Create ML to train a Core ML model.](https://docs-assets.developer.apple.com/published/eb03080ad7cc9d6f88eadc90b3bac920/create-ml-1%402x.png)

You train a model to recognize patterns by showing it representative samples. For example, you can train a model to recognize dogs by showing it lots of images of different dogs. After you’ve trained the model, you test it out on data it hasn’t seen before, and evaluate how well it performed the task. When the model is performing well enough, you’re ready to integrate it into your app using [`Core ML`](https://developer.apple.com/documentation/CoreML).

![Diagram showing the Create ML workflow: Gather data, train the model, and evaluate the trained model.](https://docs-assets.developer.apple.com/published/8140ce0ea19e9ada712c516d10436651/create-ml-2%402x.png)

Create ML leverages the machine learning infrastructure built in to Apple products like Photos and Siri. This means your image classification and natural language models are smaller and take much less time to train.

## Topics

### Image Models
- [Creating an Image Classifier Model](creating-an-image-classifier-model.md)
  Train a machine learning model to classify images, and add it to your Core ML app.
- [struct MLImageClassifier](mlimageclassifier.md)
  A model you train to classify images.
- [struct MLObjectDetector](mlobjectdetector.md)
  A model you train to classify one or more objects within an image.
- [struct MLHandPoseClassifier](mlhandposeclassifier.md)
  A task that creates a hand pose classification model by training with images of people’s hands that you provide.
### Video Models
- [Creating an Action Classifier Model](creating-an-action-classifier-model.md)
  Train a machine learning model to recognize a person’s body movements.
- [Detecting Human Actions in a Live Video Feed](detecting_human_actions_in_a_live_video_feed.md)
  Identify body movements by sending a person’s pose data from a series of video frames to an action-classification model.
- [struct MLActionClassifier](mlactionclassifier.md)
  A model you train with videos to classify a person’s body movements.
- [struct MLHandActionClassifier](mlhandactionclassifier.md)
  A task that creates a hand action classification model by training with videos of people’s hand movements that you provide.
- [struct MLStyleTransfer](mlstyletransfer.md)
  A model you train to apply an image’s style to other images or videos.
### Text Models
- [Creating a text classifier model](creating-a-text-classifier-model.md)
  Train a machine learning model to classify natural language text.
- [struct MLTextClassifier](mltextclassifier.md)
  A model you train to classify natural language text.
- [struct MLWordTagger](mlwordtagger.md)
  A word-tagging model you train to classify natural language text at the word level.
- [struct MLGazetteer](mlgazetteer.md)
  A collection of terms and their labels, which augments a tagger that analyzes natural language text.
- [struct MLWordEmbedding](mlwordembedding.md)
  A map of strings in a vector space that enable your app to find similar strings by looking at a string’s neighbors.
### Sound Models
- [struct MLSoundClassifier](mlsoundclassifier.md)
  A machine learning model you train with audio files to recognize and identify sounds on a device.
### Motion Models
- [struct MLActivityClassifier](mlactivityclassifier.md)
  A model you train to classify motion sensor data.
### Tabular Models
- [Creating a Model from Tabular Data](creating_a_model_from_tabular_data.md)
  Train a machine learning model by using Core ML to import and manage tabular data.
- [enum MLClassifier](mlclassifier.md)
  A model you train to classify data into discrete categories.
- [enum MLRegressor](mlregressor.md)
  A model you train to estimate continuous values.
- [struct MLRecommender](mlrecommender.md)
  A model you train to make recommendations based on item similarity, grouping, and, optionally, item ratings.
### Tabular Data
- [struct MLDataTable](mldatatable.md)
  A table of data for training or evaluating a machine learning model.
- [enum MLDataValue](mldatavalue.md)
  The value of a cell in a data table.
- [Data Visualizations](data-visualizations.md)
  Render images of data tables and columns in a playground.
### Model Accuracy
- [Improving Your Model’s Accuracy](improving-your-model-s-accuracy.md)
  Use metrics to tune the performance of your machine learning model.
- [struct MLClassifierMetrics](mlclassifiermetrics.md)
  Metrics you use to evaluate a classifier’s performance.
- [struct MLRegressorMetrics](mlregressormetrics.md)
  Metrics you use to evaluate a regressor’s performance.
- [struct MLWordTaggerMetrics](mlwordtaggermetrics.md)
  Metrics you use to evaluate a word tagger’s performance.
- [struct MLRecommenderMetrics](mlrecommendermetrics.md)
  Metrics you use to evaluate a recommender’s performance.
- [struct MLObjectDetectorMetrics](mlobjectdetectormetrics.md)
  Metrics you use to evaluate an object detector’s performance.
### Model Training Control
- [class MLJob](mljob.md)
  The representation of a model’s asynchronous training session you use to monitor the session’s progress or terminate its execution.
- [class MLTrainingSession](mltrainingsession.md)
  The current state of a model’s asynchronous training session.
- [struct MLTrainingSessionParameters](mltrainingsessionparameters.md)
  The configuration settings for a training session.
- [struct MLCheckpoint](mlcheckpoint.md)
  The state of a model’s asynchronous training session at a specific point in time during the feature extraction or training phase.
### Supporting Types
- [enum MLCreateError](mlcreateerror.md)
  The errors Create ML throws while performing various operations, such as training models, making predictions, writing models to a file system, and so on.
- [struct MLModelMetadata](mlmodelmetadata.md)
  Information about a model that’s stored in a Core ML model file.
- [enum MLSplitStrategy](mlsplitstrategy.md)
  Data partitioning approaches, typically for creating a validation dataset from a training dataset.
### Articles
- [Creating a Text Classifier Model](creating-a-classification-model-for-natural-language.md)
  Train a machine learning model to classify natural language text.
- [Data Visualizations](create-ml-utilties.md)
  Render images of data tables and columns in a playground.
- [Gathering Training Videos for an Action Classifier](recording-or-choosing-training-videos.md)
  Collect quality example videos that effectively train action classifiers.
- [Option Set Support](option-set-support.md)
  Inspect and modify a video augmentation option set with the properties and methods it inherits from standard protocols.
### Enumerations
- [enum MLBoundingBoxAnchor](mlboundingboxanchor.md)
  A location within a bounding box that an annotation’s coordinates use as their reference point.
- [enum MLBoundingBoxCoordinatesOrigin](mlboundingboxcoordinatesorigin.md)
  The location within an image that an annotation’s coordinates use as their origin.
- [enum MLBoundingBoxUnits](mlboundingboxunits.md)
  The units a bounding box annotation uses to define its position and size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CreateML)*