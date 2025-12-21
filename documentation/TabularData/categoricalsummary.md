# CategoricalSummary

**Framework**: TabularData  
**Kind**: struct

A categorical summary of a collection’s elements.

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
struct CategoricalSummary<Element> where Element : Hashable
```

#### Overview

Each categorical summary has 5 statistics about a collection:

- `someCount`: The number of non-missing elements.
- `noneCount` The number of missing elements.
- `uniqueCount`: The number of unique elements.
- `totalCount`: The total number of elements.
- `mode`: An array of the most common values.

## Topics

### Creating a Summary
- [init()](categoricalsummary/init.md)
  Creates a categorical summary with default values.
- [init(someCount: Int, noneCount: Int, uniqueCount: Int, mode: [Element])](categoricalsummary/init(somecount:nonecount:uniquecount:mode:).md)
  Creates a categorical summary.
### Inspecting a Summary
- [var debugDescription: String](categoricalsummary/debugdescription.md)
  A text representation of the summary’s statistics suitable for debugging.
- [var mode: [Element]](categoricalsummary/mode.md)
  The most common values in a column, ignoring missing elements.
- [var uniqueCount: Int](categoricalsummary/uniquecount.md)
  The number of elements with distinct values in a column that excludes missing elements.
- [var someCount: Int](categoricalsummary/somecount.md)
  The number of non-missing elements in the column.
- [var noneCount: Int](categoricalsummary/nonecount.md)
  The number of missing elements in the column.
- [var totalCount: Int](categoricalsummary/totalcount.md)
  The total number of elements in the column.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct NumericSummary](numericsummary.md)
  A summary of a numerical column.
- [struct AnyCategoricalSummary](anycategoricalsummary.md)
  A type-erased categorical summary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/categoricalsummary)*