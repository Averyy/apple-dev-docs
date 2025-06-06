# AnyCategoricalSummary

**Framework**: TabularData  
**Kind**: struct

A type-erased categorical summary.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct AnyCategoricalSummary
```

#### Overview

Categorical summary includes 5 statistics:

- someCount: The number of non-missing elements.
- noneCount: The number of missing elements.
- totalCount: The sum of missing and non-missing elements.
- uniqueCount: The number of unique elements.
- mode: The most common elements.

## Topics

### Getting Statistical Information
- [var noneCount: Int](anycategoricalsummary/nonecount.md)
  The number of missing elements in the column.
- [var someCount: Int](anycategoricalsummary/somecount.md)
  The number of non-missing elements in the column.
- [var totalCount: Int](anycategoricalsummary/totalcount.md)
  The total number of elements in the column.
- [var uniqueCount: Int](anycategoricalsummary/uniquecount.md)
  The number of unique elements.
### Getting Mode Information
- [var mode: [Any]](anycategoricalsummary/mode.md)
  The most common values in a column.
- [var modeType: any Any.Type](anycategoricalsummary/modetype.md)
  The underlying type of [`mode`](anycategoricalsummary/mode.md).
### Operators
- [static func == (AnyCategoricalSummary, AnyCategoricalSummary) -> Bool](anycategoricalsummary/==(_:_:).md)
  Returns a Boolean value that indicates whether the categorical summaries are equal.
### Initializers
- [init(CategoricalSummary<AnyHashable>)](anycategoricalsummary/init(_:)-7p9bv.md)
  Creates a type-erased categorical summary from a typed categorical summary.
- [init<T>(CategoricalSummary<T>)](anycategoricalsummary/init(_:)-8innt.md)
  Creates a type-erased categorical summary from a typed categorical summary.
### Default Implementations
- [Equatable Implementations](anycategoricalsummary/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct NumericSummary](numericsummary.md)
  A summary of a numerical column.
- [struct CategoricalSummary](categoricalsummary.md)
  A categorical summary of a collection’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycategoricalsummary)*