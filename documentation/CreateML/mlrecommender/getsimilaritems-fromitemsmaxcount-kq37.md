# getSimilarItems(fromItems:maxCount:)

**Framework**: Create ML  
**Kind**: method

Returns the top ranked similar items based on the model’s similarity type.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func getSimilarItems(fromItems: [any MLIdentifier], maxCount: Int = 10) throws -> MLDataTable
```

## Parameters

- `fromItems`: An array of item identifiers.
- `maxCount`: The maximum number of similar items per item in the    column. The default is  .

## See Also

- [func recommendations<T>(fromUsers: MLDataColumn<T>, maxCount: Int, restrictingToItems: MLDataColumn<T>?, excluding: MLDataTable?, excludingObserved: Bool) throws -> MLDataTable](mlrecommender/recommendations(fromusers:maxcount:restrictingtoitems:excluding:excludingobserved:)-416wd.md)
  Retrieves the highest scored items for the given column of users, based on item similarity and the rating column.
- [func recommendations(fromUsers: [any MLIdentifier], maxCount: Int, restrictingToItems: [any MLIdentifier]?, excluding: MLDataTable?, excludingObserved: Bool) throws -> MLDataTable](mlrecommender/recommendations(fromusers:maxcount:restrictingtoitems:excluding:excludingobserved:)-7an46.md)
  Retrieves the highest scored item for the given array of users, based on item similarity and the rating column.
- [protocol MLIdentifier](mlidentifier.md)
  A type the Create ML framework can use as a machine learning identifier.
- [func getSimilarItems<T>(fromItems: MLDataColumn<T>, maxCount: Int) throws -> MLDataTable](mlrecommender/getsimilaritems(fromitems:maxcount:)-9scon.md)
  Returns the top ranked similar items based on the model’s similarity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/getsimilaritems(fromitems:maxcount:)-kq37)*