# MLRecommender.ModelParameters

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

Parameters that affect the process of training a recommender model.

**Availability**:
- macOS 10.15+

## Declaration

```swift
struct ModelParameters
```

## Topics

### Creating parameters
- [init(algorithm: MLRecommender.ModelAlgorithmType, threshold: Double, maxCount: Int, nearestItemsDataFrame: DataFrame?, maxSimilarityIterations: Int)](./modelparameters-swift.struct/init%28algorithm,threshold,maxcount,nearestitemsdataframe,maxsimilarityiterations%29.md)
  Creates a new set of recommender configuration parameters.
- [init(algorithm: MLRecommender.ModelAlgorithmType, threshold: Double, maxCount: Int, nearestItems: MLDataTable?, maxSimilarityIterations: Int)](./modelparameters-swift.struct/init%28algorithm,threshold,maxcount,nearestitems,maxsimilarityiterations%29.md)
  Creates a new set of recommender configuration parameters.
- [MLRecommender.ModelAlgorithmType](./modelalgorithmtype.md)
  The algorithms a recommender can use to make recommendations.
### Configuring the parameters
- [var algorithm: MLRecommender.ModelAlgorithmType](./modelparameters-swift.struct/algorithm.md)
  The algorithm the recommender uses to make recommendations.
- [var maxCount: Int](./modelparameters-swift.struct/maxcount.md)
  The largest number of similar items the model stores for each item.
- [var maxSimilarityIterations: Int](./modelparameters-swift.struct/maxsimilarityiterations.md)
  The largest number of iterations the recommender uses to build its lookup table.
- [var threshold: Double](./modelparameters-swift.struct/threshold.md)
  The item confidence value cutoff, below which the recommender omits those items from its recommendations.
- [var nearestItems: MLDataTable?](./modelparameters-swift.struct/nearestitems.md)
  A data table that lists each item’s nearest items.
- [var nearestItemsDataFrame: DataFrame?](./modelparameters-swift.struct/nearestitemsdataframe.md)
  A data frame that lists each item’s nearest items.

## See Also

### Creating and training a recommender
- [init(trainingData:userColumn:itemColumn:ratingColumn:parameters:)](./init%28trainingdata,usercolumn,itemcolumn,ratingcolumn,parameters%29.md)
  Creates an instance given a table and the names of the item and user columns contained therein.
- [let modelParameters: MLRecommender.ModelParameters](./modelparameters-swift.property.md)
  The configuration parameters that the recommender used for training during initialization.
- [var userIdentifierColumn: String](./useridentifiercolumn.md)
  The name of the column you selected at initialization to define the user identifiers.
- [var itemIdentifierColumn: String](./itemidentifiercolumn.md)
  The name of the column you selected at initialization to define the item identifiers.
- [var ratingColumn: String?](./ratingcolumn.md)
  The name of the column you selected at initialization to define the ratings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/modelparameters-swift.struct)*