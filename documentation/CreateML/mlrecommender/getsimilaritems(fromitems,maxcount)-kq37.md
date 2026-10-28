# getSimilarItems(fromItems:maxCount:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Returns the top ranked similar items based on the model’s similarity type.

**Availability**:
- macOS 10.15+ - Deprecated in 14.0

## Declaration

```swift
func getSimilarItems(fromItems: [any MLIdentifier], maxCount: Int = 10) throws -> MLDataTable
```

**Other overloads**:

```swift
func getSimilarItems<T>(fromItems: MLDataColumn<T>, maxCount: Int = 10) throws -> MLDataTable where T : MLDataValueConvertible
```

## Parameters

- `fromItems`: An array of item identifiers.
- `maxCount`: The maximum number of similar items per item in the `fromItems` column. The default is `10`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/getsimilaritems(fromitems:maxcount:)-kq37)*