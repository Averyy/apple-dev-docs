# modelParameters

**Framework**: Create ML  
**Kind**: property

The configuration parameters that the recommender used for training during initialization.

**Availability**:
- macOS 10.15+

## Declaration

```swift
let modelParameters: MLRecommender.ModelParameters
```

## See Also

- [init(trainingData: DataFrame, userColumn: String, itemColumn: String, ratingColumn: String?, parameters: MLRecommender.ModelParameters) throws](mlrecommender/init(trainingdata:usercolumn:itemcolumn:ratingcolumn:parameters:)-1mecd.md)
  Creates an instance given a table and the names of the item and user columns contained therein.
- [init(trainingData: MLDataTable, userColumn: String, itemColumn: String, ratingColumn: String?, parameters: MLRecommender.ModelParameters) throws](mlrecommender/init(trainingdata:usercolumn:itemcolumn:ratingcolumn:parameters:)-20dcf.md)
  Creates an instance given a table and the names of the item and user columns contained therein.
- [MLRecommender.ModelParameters](mlrecommender/modelparameters-swift.struct.md)
  Parameters that affect the process of training a recommender model.
- [var userIdentifierColumn: String](mlrecommender/useridentifiercolumn.md)
  The name of the column you selected at initialization to define the user identifiers.
- [var itemIdentifierColumn: String](mlrecommender/itemidentifiercolumn.md)
  The name of the column you selected at initialization to define the item identifiers.
- [var ratingColumn: String?](mlrecommender/ratingcolumn.md)
  The name of the column you selected at initialization to define the ratings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/modelparameters-swift.property)*