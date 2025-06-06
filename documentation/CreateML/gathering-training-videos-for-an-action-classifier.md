# Gathering Training Videos for an Action Classifier

**Framework**: Create ML

Collect quality example videos that effectively train action classifiers.

#### Overview

Create a robust action classifier by collecting high-quality videos that clearly show a person performing each action you want the classifier to recognize. In addition, gather videos of unrelated actions the classifier might witness. Use these to create a  of irrelevant actions, so the classifier distinguishes between these two types.

For general information about how to create an action classifier, see [`Creating an Action Classifier Model`](creating-an-action-classifier-model.md).

##### Collect Videos for Each Action

Action classifiers learn from example videos of a human performing an action. Create ML uses the [`Vision`](https://developer.apple.com/documentation/Vision) framework to locate key body parts, called , in each video frame. Action classifiers learn how to recognize a human body’s movements by tracking these landmarks frame by frame. Keep the landmarks clearly visible by applying the following guidelines as you record example videos, or when assessing videos from other sources.

- Keep the camera still.
- Record one person at a time.
- Capture the person’s entire body.
- Ensure the environment has sufficient lighting.
- Ensure the person’s clothing isn’t loose or flowing.
- Ensure the person’s clothing sufficiently contrasts with the environment’s background.
- Remove foreground objects that might obscure the person as they perform the action.
- If the person performs multiple instances of a single action in a recording, minimize the time between repetitions.

You typically want an action classifier to work with any human that uses your app. Teach your model to account for natural variations by including videos of variations in the action you want the classifier to recognize, such as how the person holds their head or places their arms.

If you want your app to recognize actions more generally or from various camera angles, add more example videos that capture the action from multiple directions.

##### Collect Videos for a Negative Class

A negative class is a category of one or more actions that aren’t important to the action classifier. Negative classes help the classifier distinguish between the actions you want it to recognize and potential nonactions it might encounter in your app.

Create a negative class by gathering example videos of all unrelated nonactions the classifier might observe. For example, a negative class for an exercise-action classifier might include examples of individuals walking in and out frame. Including this negative class ensures that the action classifier is less likely to confuse walking for an exercise, such as a lunge.

Make additional negative classes for nonactions that take different spans of time, or for static versus dynamic nonactions. For example, the exercise classifier might have another negative class of static actions that include examples of individuals standing still or sitting in a chair.

## See Also

- [Building an Action Classifier Data Source](building-an-action-classifier-data-source.md)
  Arrange your training videos in multiple folders with labels that describe actions, or in a single folder with an annotation file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/gathering-training-videos-for-an-action-classifier)*