# recommendations(fromUsers:maxCount:restrictingToItems:excluding:excludingObserved:)

**Framework**: Create ML  
**Kind**: method

Retrieves the highest scored item for the given array of users, based on item similarity and the rating column.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func recommendations(fromUsers: [any MLIdentifier], maxCount: Int = 10, restrictingToItems: [any MLIdentifier]? = nil, excluding userItemObservations: MLDataTable? = nil, excludingObserved: Bool = true) throws -> MLDataTable
```

#### Return Value

An [`MLDataTable`](mldatatable.md) containing columns with user identifiers, item identifiers, scores and ranks (numbered between `1` and the `maxCount`).

## Parameters

- `fromUsers`: An array of user identifiers.
- `maxCount`: The maximum number of recommendations per user. The default is  .
- `restrictingToItems`: An array of item identifiers that defines the only values the recommender can use this   set of recommendations. By default, the parameter is  , meaning there are no restrictions.
- `userItemObservations`: A data table of user-item observations to exclude from recommendations. The default   is  , meaning no observations are excluded. The column names for the user identifiers and item   identifiers must be the same as those provided in the training data.
- `excludingObserved`: Set this value to   to omit training data from the recommendations, or   to   include them. The default is  .

## See Also

- [protocol MLIdentifier](mlidentifier.md)
  A type the Create ML framework can use as a machine learning identifier.
- [func getSimilarItems(fromItems:maxCount:)](mlrecommender/getsimilaritems(fromitems:maxcount:).md)
  Returns the top ranked similar items based on the model’s similarity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/recommendations(fromusers:maxcount:restrictingtoitems:excluding:excludingobserved:))*