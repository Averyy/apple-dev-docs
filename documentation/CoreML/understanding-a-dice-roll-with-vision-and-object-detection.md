# Understanding a Dice Roll with Vision and Object Detection

**Framework**: Core ML

Detect dice position and values shown in a camera frame, and determine the end of a roll by leveraging a dice detection model.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Xcode 12.0+
- iPad 13.0+

#### Overview

This sample app uses an object detection model trained with [`Create ML`](https://developer.apple.com/documentation/CreateML) to recognize the tops of dice and their values when the dice roll onto a flat surface.

After you run the object detection model on camera frames through [`Vision`](https://developer.apple.com/documentation/Vision), the model interprets the result to identify when a roll has ended and what values the dice show.

> **Note**: This sample code project is associated with WWDC 2019 session [`228: Creating Great Apps Using Core ML and ARKit`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc19/228/).

##### Configure the Sample Code Project

Before you run the sample code project in Xcode, note the following:

- You must run this sample code project on a physical device that uses iOS 13 or later. The project doesn’t work with Simulator.
- The model works best on white dice with black pips. It may perform differently on dice that use other colors.

##### Add Inputs to the Request

In Vision, beginning in iOS 13, you can provide inputs other than images to a model by attaching an [`MLFeatureProvider`](MLFeatureProvider.md) object to your model. This is useful in the case of object detection when you want to specify different thresholds than the defaults.

As shown below, a feature provider can provide values for the `iouThreshold` and `confidenceThreshold` inputs to your object detection model.

To use this threshold provider with your [`VNCoreMLModel`](https://developer.apple.com/documentation/Vision/VNCoreMLModel), assign it to the [`featureProvider`](https://developer.apple.com/documentation/Vision/VNCoreMLModel/featureProvider) property of your [`VNCoreMLModel`](https://developer.apple.com/documentation/Vision/VNCoreMLModel) as seen in the following example.

##### Set Up a Vision Request to Handle Camera Frames

For simplicity, you can use camera frames coming from an [`ARSession`](https://developer.apple.com/documentation/ARKit/ARSession).

To run your detector on these frames, first set up a [`VNCoreMLRequest`](https://developer.apple.com/documentation/Vision/VNCoreMLRequest) request with your model, as shown in the example below.

##### Pass Camera Frames to the Object Detector to Predict Dice Locations

Pass the frames from the camera to the [`VNCoreMLRequest`](https://developer.apple.com/documentation/Vision/VNCoreMLRequest) so it can make predictions using a [`VNImageRequestHandler`](https://developer.apple.com/documentation/Vision/VNImageRequestHandler) object. The [`VNImageRequestHandler`](https://developer.apple.com/documentation/Vision/VNImageRequestHandler) object handles image resizing and preprocessing as well as post-processing of your model’s outputs for every prediction.

To pass camera frames to your model, you first need to find the image orientation that corresponds to your device’s physical orientation. If the device’s orientation changes, the aspect ratio of the images can also change. Because you need to scale the bounding boxes for the detected objects back to your original image, you need to keep track of its size.

Finally, you invoke the [`VNImageRequestHandler`](https://developer.apple.com/documentation/Vision/VNImageRequestHandler) with the image from the camera and information about the current orientation to make a prediction using your object detector.

Now that the app handles providing  data to your model, it’s time to interpret your model’s .

##### Draw Bounding Boxes to Understand Your Models Behavior

You can get a better understanding of how well your detector performs by drawing bounding boxes around each object and its text label. The dice detection model detects the tops of dice and labels them according to the number of pips shown on each die’s top side.

To draw bounding boxes, see [`Recognizing Objects in Live Capture`](https://developer.apple.com/documentation/Vision/recognizing-objects-in-live-capture).

##### Determine When a Roll Has Ended

When playing a dice game, users want to know the result of a roll. The app determines that the roll has ended by waiting for the dice’s positions and values to stabilize.

You can define the requirements of an ended roll as a comparison between two consecutive camera frames with the following conditions:

- The number of detected dice must be the same.
- For each detected die: - The bounding box must have not moved.
- The identified class must match.

Based on these constraints, you can make a function that tells the app whether a roll has ended based on the current and the previous [`VNRecognizedObjectObservation`](https://developer.apple.com/documentation/Vision/VNRecognizedObjectObservation) objects.

Now for every prediction (meaning every new camera frame) you can check whether the roll has ended.

##### Display the Dice Values

Once the roll has ended, you can display the information on the screen or trigger some other behavior in the setting of a game.

This sample app shows the list of recognized values on screen, sorted from left-most to right-most [`VNRecognizedObjectObservation`](https://developer.apple.com/documentation/Vision/VNRecognizedObjectObservation). It sorts the values based on where the dice are on the surface according to each observation’s bounding box coordinates. The app does this by sorting the observations by their bounding box’s `centerX` property in ascending order.

## See Also

- [Using Core ML for semantic image segmentation](using-core-ml-for-semantic-image-segmentation.md)
  Identify multiple objects in an image by using the DEtection TRansformer image-segmentation model.
- [Classifying Images with Vision and Core ML](classifying-images-with-vision-and-core-ml.md)
  Crop and scale photos using the Vision framework and classify them with a Core ML model.
- [Detecting human body poses in an image](detecting-human-body-poses-in-an-image.md)
  Locate people and the stance of their bodies by analyzing an image with a PoseNet model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/understanding-a-dice-roll-with-vision-and-object-detection)*