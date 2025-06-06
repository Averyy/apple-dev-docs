# NumericSummary

**Framework**: TabularData  
**Kind**: struct

A summary of a numerical column.

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
struct NumericSummary<Element> where Element : BinaryFloatingPoint
```

## Topics

### Creating a Summary
- [init()](numericsummary/init.md)
  Creates an empty numeric summary with default values.
- [init(someCount: Int, noneCount: Int, mean: Element, standardDeviation: Element, min: Element, max: Element, median: Element, firstQuartile: Element, thirdQuartile: Element)](numericsummary/init(somecount:nonecount:mean:standarddeviation:min:max:median:firstquartile:thirdquartile:).md)
  Creates an empty numeric summary.
### Comparing Summaries
- [static func != (Self, Self) -> Bool](numericsummary/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Inspecting a Summary
- [var debugDescription: String](numericsummary/debugdescription.md)
  A text representation of the summary’s statistics suitable for debugging.
- [var someCount: Int](numericsummary/somecount.md)
  The number of non-missing elements in the column.
- [var noneCount: Int](numericsummary/nonecount.md)
  The number of missing elements in the column.
- [var totalCount: Int](numericsummary/totalcount.md)
  The total number of elements in the column.
### Getting Statistical Values
- [var max: Element](numericsummary/max.md)
  The largest value, excluding missing elements.
- [var mean: Element](numericsummary/mean.md)
  The arithmetic mean of a column’s values that excludes missing elements.
- [var median: Element](numericsummary/median.md)
  The midpoint value that’s above half of the non-missing elements’ values and below the other half’s values.
- [var min: Element](numericsummary/min.md)
  The smallest value, excluding missing elements.
- [var standardDeviation: Element](numericsummary/standarddeviation.md)
  The standard deviation of a column’s values that excludes missing elements.
- [var firstQuartile: Element](numericsummary/firstquartile.md)
  The value that’s above 25% of the non-missing elements’ values.
- [var thirdQuartile: Element](numericsummary/thirdquartile.md)
  The value that’s above 75% of the non-missing elements’ values.
### Operators
- [static func == (NumericSummary<Element>, NumericSummary<Element>) -> Bool](numericsummary/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](numericsummary/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](numericsummary/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](numericsummary/equatable-implementations.md)

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct CategoricalSummary](categoricalsummary.md)
  A categorical summary of a collection’s elements.
- [struct AnyCategoricalSummary](anycategoricalsummary.md)
  A type-erased categorical summary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/numericsummary)*