# itemIdentifierColumn

**Framework**: Create ML  
**Kind**: property

The name of the column you selected at initialization to define the item identifiers.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var itemIdentifierColumn: String
```

#### Discussion

Changing the value of this property doesn’t retrain the model or affect its behavior.

## See Also

- [init(trainingData:userColumn:itemColumn:ratingColumn:parameters:)](mlrecommender/init(trainingdata:usercolumn:itemcolumn:ratingcolumn:parameters:).md)
  Creates an instance given a table and the names of the item and user columns contained therein.
- [MLRecommender.ModelParameters](mlrecommender/modelparameters-swift.struct.md)
  Parameters that affect the process of training a recommender model.
- [let modelParameters: MLRecommender.ModelParameters](mlrecommender/modelparameters-swift.property.md)
  The configuration parameters that the recommender used for training during initialization.
- [var userIdentifierColumn: String](mlrecommender/useridentifiercolumn.md)
  The name of the column you selected at initialization to define the user identifiers.
- [var ratingColumn: String?](mlrecommender/ratingcolumn.md)
  The name of the column you selected at initialization to define the ratings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/itemidentifiercolumn)*