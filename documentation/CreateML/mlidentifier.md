# MLIdentifier

**Framework**: Create ML  
**Kind**: protocol  
**Role**: Protocol

A type the Create ML framework can use as a machine learning identifier.

**Availability**:
- macOS 10.15+ - Deprecated in 14.0

## Declaration

```swift
protocol MLIdentifier
```

#### Overview

You can use any type that conforms to the [`MLIdentifier`](./mlidentifier.md) protocol, typically [`Int`](../Swift/int.md) or [`String`](../Swift/string.md), to uniquely identify users and items in these [`MLRecommender`](./mlrecommender.md) methods:

[`recommendations(fromUsers:maxCount:restrictingToItems:excluding:excludingObserved:)`](./mlrecommender/recommendations%28fromusers,maxcount,restrictingtoitems,excluding,excludingobserved%29-7an46.md)

- [`getSimilarItems(fromItems:maxCount:)`](./mlrecommender/getsimilaritems%28fromitems,maxcount%29-kq37.md)

## Topics

### Getting an identifier
- [var identifierValue: MLDataValue](./mlidentifier/identifiervalue.md)
  The value of the unique identifier wrapped in a data value.

## See Also

### Testing a recommender
- [func recommendations(fromUsers:maxCount:restrictingToItems:excluding:excludingObserved:)](./mlrecommender/recommendations%28fromusers,maxcount,restrictingtoitems,excluding,excludingobserved%29.md)
  Retrieves the highest scored item for the given array of users, based on item similarity and the rating column.
- [func getSimilarItems(fromItems:maxCount:)](./mlrecommender/getsimilaritems%28fromitems,maxcount%29.md)
  Returns the top ranked similar items based on the model’s similarity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlidentifier)*