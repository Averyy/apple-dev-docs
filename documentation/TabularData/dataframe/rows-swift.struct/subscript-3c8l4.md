# subscript(_:)

**Framework**: TabularData  
**Kind**: subscript

Accesses a contiguous subrange of the collection’s elements.

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
subscript(bounds: Range<Self.Index>) -> Slice<Self> { get set }
```

#### Overview

The accessed slice uses the same indices for the same elements as the original collection. Always use the slice’s `startIndex` property instead of assuming that its indices start at a particular value.

This example demonstrates getting a slice of an array of strings, finding the index of one of the strings in the slice, and then using that index in the original array.

```None
var streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
let streetsSlice = streets[2 ..< streets.endIndex]
print(streetsSlice)
// Prints "["Channing", "Douglas", "Evarts"]"

let index = streetsSlice.firstIndex(of: "Evarts")    // 4
streets[index!] = "Eustace"
print(streets[index!])
// Prints "Eustace"
```

> **Note**: O(1)

## Parameters

- `bounds`: A range of the collection’s indices. The bounds of   the range must be valid indices of the collection.

## See Also

- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](dataframe/rows-swift.struct/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](dataframe/rows-swift.struct/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func prefix(Int) -> Self.SubSequence](dataframe/rows-swift.struct/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](dataframe/rows-swift.struct/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(through: Self.Index) -> Self.SubSequence](dataframe/rows-swift.struct/prefix(through:).md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](dataframe/rows-swift.struct/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func suffix(Int) -> Self.SubSequence](dataframe/rows-swift.struct/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](dataframe/rows-swift.struct/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.
- [func joined() -> FlattenSequence<Self>](dataframe/rows-swift.struct/joined.md)
  Returns the elements of this sequence of sequences, concatenated.
- [func joined<Separator>(separator: Separator) -> JoinedSequence<Self>](dataframe/rows-swift.struct/joined(separator:).md)
  Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.
- [subscript<R>(R) -> Self.SubSequence](dataframe/rows-swift.struct/subscript(_:)-9e4z3.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript<R>(R) -> Self.SubSequence](dataframe/rows-swift.struct/subscript(_:)-9yafe.md)
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](dataframe/rows-swift.struct/subscript(_:)-43snh.md)
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](dataframe/rows-swift.struct/subscript(_:)-47kxi.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/dataframe/rows-swift.struct/subscript(_:)-3c8l4)*