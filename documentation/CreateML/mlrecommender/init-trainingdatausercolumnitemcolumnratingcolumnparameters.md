# init(trainingData:userColumn:itemColumn:ratingColumn:parameters:)

**Framework**: Create ML  
**Kind**: init

Creates an instance given a table and the names of the item and user columns contained therein.

**Availability**:
- macOS 13.0+

## Declaration

```swift
init(trainingData: DataFrame, userColumn: String, itemColumn: String, ratingColumn: String? = nil, parameters: MLRecommender.ModelParameters = ModelParameters(nearestItems: nil)) throws
```

## Parameters

- `trainingData`: A data frame containing training data.
- `userColumn`: Name of the Int or String typed column in the training data containing user identifiers.
- `itemColumn`: Name of the Int or String typed column in the training data containing item identifiers.
- `ratingColumn`: Name of an Int or Double typed column optionally in the training data containing scores or   ratings. The default is nil, which corresponds to no rating column.
- `parameters`: Model training parameters.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/init(trainingdata:usercolumn:itemcolumn:ratingcolumn:parameters:))*