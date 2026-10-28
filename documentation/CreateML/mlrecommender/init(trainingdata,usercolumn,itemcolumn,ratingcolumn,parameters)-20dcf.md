# init(trainingData:userColumn:itemColumn:ratingColumn:parameters:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates an instance given a table and the names of the item and user columns contained therein.

**Availability**:
- macOS 10.15+ - Deprecated in 13.0

> **Deprecated**: Use DataFrame instead of MLDataTable when initializing.

## Declaration

```swift
init(trainingData: MLDataTable, userColumn: String, itemColumn: String, ratingColumn: String? = nil, parameters: MLRecommender.ModelParameters = ModelParameters(nearestItems: nil)) throws
```

**Other overloads**:

```swift
init(trainingData: DataFrame, userColumn: String, itemColumn: String, ratingColumn: String? = nil, parameters: MLRecommender.ModelParameters = ModelParameters(nearestItems: nil)) throws
```

## Parameters

- `trainingData`: A MLDataTable containing training data.
- `userColumn`: Name of the Int or String typed column in the training data containing user identifiers.
- `itemColumn`: Name of the Int or String typed column in the training data containing item identifiers.
- `ratingColumn`: Name of an Int or Double typed column optionally in the training data containing scores or ratings. The default is nil, which corresponds to no rating column.
- `parameters`: Model training parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/init(trainingdata:usercolumn:itemcolumn:ratingcolumn:parameters:)-20dcf)*