# MLRecommender.ModelParameters

**Framework**: Create ML  
**Kind**: struct

Parameters that affect the process of training a recommender model.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct ModelParameters
```

## Topics

### Creating parameters
- [init(algorithm: MLRecommender.ModelAlgorithmType, threshold: Double, maxCount: Int, nearestItemsDataFrame: DataFrame?, maxSimilarityIterations: Int)](mlrecommender/modelparameters-swift.struct/init(algorithm:threshold:maxcount:nearestitemsdataframe:maxsimilarityiterations:).md)
  Creates a new set of recommender configuration parameters.
- [init(algorithm: MLRecommender.ModelAlgorithmType, threshold: Double, maxCount: Int, nearestItems: MLDataTable?, maxSimilarityIterations: Int)](mlrecommender/modelparameters-swift.struct/init(algorithm:threshold:maxcount:nearestitems:maxsimilarityiterations:).md)
  Creates a new set of recommender configuration parameters.
- [MLRecommender.ModelAlgorithmType](mlrecommender/modelalgorithmtype.md)
  The algorithms a recommender can use to make recommendations.
### Configuring the parameters
- [var algorithm: MLRecommender.ModelAlgorithmType](mlrecommender/modelparameters-swift.struct/algorithm.md)
  The algorithm the recommender uses to make recommendations.
- [var maxCount: Int](mlrecommender/modelparameters-swift.struct/maxcount.md)
  The largest number of similar items the model stores for each item.
- [var maxSimilarityIterations: Int](mlrecommender/modelparameters-swift.struct/maxsimilarityiterations.md)
  The largest number of iterations the recommender uses to build its lookup table.
- [var threshold: Double](mlrecommender/modelparameters-swift.struct/threshold.md)
  The item confidence value cutoff, below which the recommender omits those items from its recommendations.
- [var nearestItems: MLDataTable?](mlrecommender/modelparameters-swift.struct/nearestitems.md)
  A data table that lists each item’s nearest items.
- [var nearestItemsDataFrame: DataFrame?](mlrecommender/modelparameters-swift.struct/nearestitemsdataframe.md)
  A data frame that lists each item’s nearest items.

## See Also

- [init(trainingData:userColumn:itemColumn:ratingColumn:parameters:)](mlrecommender/init(trainingdata:usercolumn:itemcolumn:ratingcolumn:parameters:).md)
  Creates an instance given a table and the names of the item and user columns contained therein.
- [let modelParameters: MLRecommender.ModelParameters](mlrecommender/modelparameters-swift.property.md)
  The configuration parameters that the recommender used for training during initialization.
- [var userIdentifierColumn: String](mlrecommender/useridentifiercolumn.md)
  The name of the column you selected at initialization to define the user identifiers.
- [var itemIdentifierColumn: String](mlrecommender/itemidentifiercolumn.md)
  The name of the column you selected at initialization to define the item identifiers.
- [var ratingColumn: String?](mlrecommender/ratingcolumn.md)
  The name of the column you selected at initialization to define the ratings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/modelparameters-swift.struct)*