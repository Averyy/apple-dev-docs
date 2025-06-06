# MLRecommender

**Framework**: Create ML  
**Kind**: struct

A model you train to make recommendations based on item similarity, grouping, and, optionally, item ratings.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct MLRecommender
```

#### Overview

Use an [`MLRecommender`](mlrecommender.md) to train a machine learning model that you include in your app to make recommendations for the user, while keeping their data on-device.

You create a recommender model by training it with tabular data that includes columns for the recommendation items and the groups the items belong to. You also have the option to include an item rating column, which gives higher-rated items more weight than those with lesser or negative ratings. The recommender uses the training information to find similarity patterns by looking at items that occur in groups or have similar ratings within groups.

After you train a recommender, you save it as a Core ML model file with the `.mlmodel` extension. Import this model file into your Xcode project by dragging it into the Project navigator. At runtime, use the recommender to make item suggestions to the user based on the patterns in training data and the user’s item history. For example, a hiking app can recommend trails based on the trails a user has previously hiked and their ratings of those trails.

## Topics

### Creating and training a recommender
- [init(trainingData: DataFrame, userColumn: String, itemColumn: String, ratingColumn: String?, parameters: MLRecommender.ModelParameters) throws](mlrecommender/init(trainingdata:usercolumn:itemcolumn:ratingcolumn:parameters:)-1mecd.md)
  Creates an instance given a table and the names of the item and user columns contained therein.
- [init(trainingData: MLDataTable, userColumn: String, itemColumn: String, ratingColumn: String?, parameters: MLRecommender.ModelParameters) throws](mlrecommender/init(trainingdata:usercolumn:itemcolumn:ratingcolumn:parameters:)-20dcf.md)
  Creates an instance given a table and the names of the item and user columns contained therein.
- [MLRecommender.ModelParameters](mlrecommender/modelparameters-swift.struct.md)
  Parameters that affect the process of training a recommender model.
- [let modelParameters: MLRecommender.ModelParameters](mlrecommender/modelparameters-swift.property.md)
  The configuration parameters that the recommender used for training during initialization.
- [var userIdentifierColumn: String](mlrecommender/useridentifiercolumn.md)
  The name of the column you selected at initialization to define the user identifiers.
- [var itemIdentifierColumn: String](mlrecommender/itemidentifiercolumn.md)
  The name of the column you selected at initialization to define the item identifiers.
- [var ratingColumn: String?](mlrecommender/ratingcolumn.md)
  The name of the column you selected at initialization to define the ratings.
### Evaluating a recommender
- [func evaluation(on: MLDataTable, userColumn: String, itemColumn: String, ratingColumn: String?, cutoffs: [Int], excludingObserved: Bool) -> MLRecommenderMetrics](mlrecommender/evaluation(on:usercolumn:itemcolumn:ratingcolumn:cutoffs:excludingobserved:)-50o7t.md)
  Computes the metrics for the given testing data.
- [func evaluation(on: DataFrame, userColumn: String, itemColumn: String, ratingColumn: String?, cutoffs: [Int], excludingObserved: Bool) -> MLRecommenderMetrics](mlrecommender/evaluation(on:usercolumn:itemcolumn:ratingcolumn:cutoffs:excludingobserved:)-641uh.md)
  Computes the metrics for the given testing data.
- [struct MLRecommenderMetrics](mlrecommendermetrics.md)
  Metrics you use to evaluate a recommender’s performance.
### Testing a recommender
- [func recommendations<T>(fromUsers: MLDataColumn<T>, maxCount: Int, restrictingToItems: MLDataColumn<T>?, excluding: MLDataTable?, excludingObserved: Bool) throws -> MLDataTable](mlrecommender/recommendations(fromusers:maxcount:restrictingtoitems:excluding:excludingobserved:)-416wd.md)
  Retrieves the highest scored items for the given column of users, based on item similarity and the rating column.
- [func recommendations(fromUsers: [any MLIdentifier], maxCount: Int, restrictingToItems: [any MLIdentifier]?, excluding: MLDataTable?, excludingObserved: Bool) throws -> MLDataTable](mlrecommender/recommendations(fromusers:maxcount:restrictingtoitems:excluding:excludingobserved:)-7an46.md)
  Retrieves the highest scored item for the given array of users, based on item similarity and the rating column.
- [protocol MLIdentifier](mlidentifier.md)
  A type the Create ML framework can use as a machine learning identifier.
- [func getSimilarItems<T>(fromItems: MLDataColumn<T>, maxCount: Int) throws -> MLDataTable](mlrecommender/getsimilaritems(fromitems:maxcount:)-9scon.md)
  Returns the top ranked similar items based on the model’s similarity type.
- [func getSimilarItems(fromItems: [any MLIdentifier], maxCount: Int) throws -> MLDataTable](mlrecommender/getsimilaritems(fromitems:maxcount:)-kq37.md)
  Returns the top ranked similar items based on the model’s similarity type.
### Saving a recommender
- [func write(to: URL, metadata: MLModelMetadata?) throws](mlrecommender/write(to:metadata:).md)
  Exports the recommender as a Core ML model file at the given URL.
- [func write(toFile: String, metadata: MLModelMetadata?) throws](mlrecommender/write(tofile:metadata:).md)
  Exports the recommender as a Core ML model file at the given file path.
### Describing a recommender
- [var model: MLModel](mlrecommender/model.md)
  The Core ML model.
### Enumerations
- [MLRecommender.ModelAlgorithmType](mlrecommender/modelalgorithmtype.md)
  The algorithms a recommender can use to make recommendations.
- [MLRecommender.SimilarityType](mlrecommender/similaritytype.md)
  The metric by which the recommender computes item similarity.

## See Also

- [Creating a Model from Tabular Data](creating_a_model_from_tabular_data.md)
  Train a machine learning model by using Core ML to import and manage tabular data.
- [enum MLClassifier](mlclassifier.md)
  A model you train to classify data into discrete categories.
- [enum MLRegressor](mlregressor.md)
  A model you train to estimate continuous values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender)*