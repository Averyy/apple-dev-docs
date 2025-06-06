# recommendations(fromUsers:maxCount:restrictingToItems:excluding:excludingObserved:)

**Framework**: Create ML  
**Kind**: method

Retrieves the highest scored items for the given column of users, based on item similarity and the rating column.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func recommendations<T>(fromUsers: MLDataColumn<T>, maxCount: Int = 10, restrictingToItems: MLDataColumn<T>? = nil, excluding userItemObservations: MLDataTable? = nil, excludingObserved: Bool = true) throws -> MLDataTable where T : MLDataValueConvertible, T : MLIdentifier
```

#### Return Value

An [`MLDataTable`](mldatatable.md) containing columns with user identifiers, item identifiers, scores and ranks (numbered between `1` and the `maxCount`).

## Parameters

- `fromUsers`: A column of user identifiers.
- `maxCount`: The maximum number of recommendations per user. The default is  .
- `restrictingToItems`: An array of item identifiers that defines the only values the recommender can use this   set of recommendations. By default, the parameter is  , meaning there are no restrictions.
- `userItemObservations`: The column names for the user identifiers and item identifiers must be the same as those provided in the   training data.
- `excludingObserved`: The default is  .

## See Also

- [func recommendations(fromUsers: [any MLIdentifier], maxCount: Int, restrictingToItems: [any MLIdentifier]?, excluding: MLDataTable?, excludingObserved: Bool) throws -> MLDataTable](mlrecommender/recommendations(fromusers:maxcount:restrictingtoitems:excluding:excludingobserved:)-7an46.md)
  Retrieves the highest scored item for the given array of users, based on item similarity and the rating column.
- [protocol MLIdentifier](mlidentifier.md)
  A type the Create ML framework can use as a machine learning identifier.
- [func getSimilarItems<T>(fromItems: MLDataColumn<T>, maxCount: Int) throws -> MLDataTable](mlrecommender/getsimilaritems(fromitems:maxcount:)-9scon.md)
  Returns the top ranked similar items based on the model’s similarity type.
- [func getSimilarItems(fromItems: [any MLIdentifier], maxCount: Int) throws -> MLDataTable](mlrecommender/getsimilaritems(fromitems:maxcount:)-kq37.md)
  Returns the top ranked similar items based on the model’s similarity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/recommendations(fromusers:maxcount:restrictingtoitems:excluding:excludingobserved:)-416wd)*