# Improving Your Model’s Accuracy

**Framework**: Create ML

Use metrics to tune the performance of your machine learning model.

#### Overview

Evaluating and improving your model starts with looking at its performance across different data sets. Metrics from each dataset inform which changes have the most impact on your model’s accuracy.

No single metric can tell you everything about your model’s performance. To improve your model, you compare the metrics ([`MLClassifierMetrics`](mlclassifiermetrics.md) or [`MLRegressorMetrics`](mlregressormetrics.md) depending on your model type) among your training, validation, and testing data sets. For example, the accuracy discussed in the [`Creating an Image Classifier Model`](creating-an-image-classifier-model.md) article is derived from the [`classificationError`](mlclassifiermetrics/classificationerror.md) metric for each data set.

You can also access these values programmatically after creating a model and loading your testing data:

```swift
print("Training Metrics\n", model.trainingMetrics)
print("Validation Metrics\n", model.validationMetrics)

let evaluationMetrics = model.evaluation(on: testData)
print("Evaluation Metrics\n", evaluationMetrics)
```

In this case, you see output for several different metrics, including [`classificationError`](mlclassifiermetrics/classificationerror.md), [`precisionRecall`](mlclassifiermetrics/precisionrecall.md), and [`confusion`](mlclassifiermetrics/confusion.md) for classifiers and [`maximumError`](mlregressormetrics/maximumerror.md) and [`rootMeanSquaredError`](mlregressormetrics/rootmeansquarederror.md) for regressors. Use these values from each data set to determine where your model needs to improve.

##### Improve Your Models Training Accuracy

If the training accuracy of your model is low, it’s an indication that your current model configuration can’t capture the complexity of your data.

Try adjusting the training parameters. When working with image data, double the maximum number of iterations in the `MLImageClassifierBuilder` playground UI (the default value is 10).

![Screenshot showing the maximum number of iterations set to 20 in the MLImageClassifierBuilder playground UI.](https://docs-assets.developer.apple.com/published/d5d3381985df49dadf5207e31a918ee5/improving-your-model-s-accuracy-1%402x.png)

For natural language data, try a different underlying algorithm (see [`MLTextClassifier.ModelAlgorithmType`](mltextclassifier/modelalgorithmtype.md)). For more general tasks, use a different underlying model than the type determined by [`MLClassifier`](mlclassifier.md) (see ) or [`MLRegressor`](mlregressor.md) (see ).

##### Improve Your Models Validation Accuracy

If your model’s accuracy on the validation set is low or fluctuates between low and high each time you train the model, you need more data. You can generate more input data from the examples you already collected, a technique known as . For image data, you can combine operations like cropping, rotation, blurring, and exposure adjustment to make one image into many examples.

![A figure showing a single image of an elephant becoming many images by applying augmentations such as crop, rotate, blur, and expose to the image.](https://docs-assets.developer.apple.com/published/8ebb9a01db59e838cba566133acf4ffe/improving-your-model-s-accuracy-2%402x.png)

It’s also possible for you to have lots of data and validation accuracy that is still significantly lower than your training accuracy. In this case, your model is _overfitting, _meaning that it’s learning too many specific details about your training set that don’t generally apply to other examples. In this case, you need to reduce the number of training iterations to prevent the model from learning too much about your training data.

##### Improve Your Models Evaluation Accuracy

If your model’s accuracy on your testing data is lower than your training or validation accuracy, it usually indicates that there are meaningful differences between the kind of data you trained the model on and the testing data you’re providing for evaluation.

For example, suppose you train your [`MLImageClassifier`](mlimageclassifier.md) on many images of indoor cats, but then test only on images of outdoor cats. Because of the differences in lighting, exposure, and background, it’s unlikely that your testing data will yield good results. Differences between images that seem obvious to humans can be difficult for a model to resolve without sufficient training data.

To correct for this, provide more diverse data in your training set. In general, more examples lead to higher performance, but it’s also important to show your model examples that are as varied your testing data.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/improving-your-model-s-accuracy)*