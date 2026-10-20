# modelParameters

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The configuration parameters that the recommender used for training during initialization.

**Availability**:
- macOS 10.15+

## Declaration

```swift
let modelParameters: MLRecommender.ModelParameters
```

## See Also

### Creating and training a recommender
- [init(trainingData:userColumn:itemColumn:ratingColumn:parameters:)](./init%28trainingdata,usercolumn,itemcolumn,ratingcolumn,parameters%29.md)
  Creates an instance given a table and the names of the item and user columns contained therein.
- [MLRecommender.ModelParameters](./modelparameters-swift.struct.md)
  Parameters that affect the process of training a recommender model.
- [var userIdentifierColumn: String](./useridentifiercolumn.md)
  The name of the column you selected at initialization to define the user identifiers.
- [var itemIdentifierColumn: String](./itemidentifiercolumn.md)
  The name of the column you selected at initialization to define the item identifiers.
- [var ratingColumn: String?](./ratingcolumn.md)
  The name of the column you selected at initialization to define the ratings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/modelparameters-swift.property)*