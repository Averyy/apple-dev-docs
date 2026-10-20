# ratingColumn

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The name of the column you selected at initialization to define the ratings.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var ratingColumn: String?
```

#### Discussion

Changing the value of this property doesn’t retrain the model or affect its behavior.

## See Also

### Creating and training a recommender
- [init(trainingData:userColumn:itemColumn:ratingColumn:parameters:)](./init%28trainingdata,usercolumn,itemcolumn,ratingcolumn,parameters%29.md)
  Creates an instance given a table and the names of the item and user columns contained therein.
- [MLRecommender.ModelParameters](./modelparameters-swift.struct.md)
  Parameters that affect the process of training a recommender model.
- [let modelParameters: MLRecommender.ModelParameters](./modelparameters-swift.property.md)
  The configuration parameters that the recommender used for training during initialization.
- [var userIdentifierColumn: String](./useridentifiercolumn.md)
  The name of the column you selected at initialization to define the user identifiers.
- [var itemIdentifierColumn: String](./itemidentifiercolumn.md)
  The name of the column you selected at initialization to define the item identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/ratingcolumn)*