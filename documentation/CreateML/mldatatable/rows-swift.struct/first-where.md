# first(where:)

**Framework**: Create ML  
**Kind**: method

Returns the first element of the sequence that satisfies the given predicate.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func first(where predicate: (Self.Element) throws -> Bool) rethrows -> Self.Element?
```

#### Return Value

The first element of the sequence that satisfies `predicate`, or `nil` if there is no element that satisfies `predicate`.

#### Discussion

The following example uses the `first(where:)` method to find the first negative number in an array of integers:

```None
let numbers = [3, 7, 4, -2, 9, -6, 10, 1]
if let firstNegative = numbers.first(where: { $0 < 0 }) {
    print("The first negative number is \(firstNegative).")
}
// Prints "The first negative number is -2."
```

> **Note**: O(), where  is the length of the sequence.

## Parameters

- `predicate`: A closure that takes an element of the sequence as   its argument and returns a Boolean value indicating whether the   element is a match.

## See Also

- [func contains(Self.Element) -> Bool](mldatatable/rows-swift.struct/contains(_:).md)
  Returns a Boolean value indicating whether the sequence contains the given element.
- [func contains(where: (Self.Element) throws -> Bool) rethrows -> Bool](mldatatable/rows-swift.struct/contains(where:).md)
  Returns a Boolean value indicating whether the sequence contains an element that satisfies the given predicate.
- [func allSatisfy((Self.Element) throws -> Bool) rethrows -> Bool](mldatatable/rows-swift.struct/allsatisfy(_:).md)
  Returns a Boolean value indicating whether every element of a sequence satisfies a given predicate.
- [func firstIndex(of: Self.Element) -> Self.Index?](mldatatable/rows-swift.struct/firstindex(of:).md)
  Returns the first index where the specified value appears in the collection.
- [func firstIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](mldatatable/rows-swift.struct/firstindex(where:).md)
  Returns the first index in which an element of the collection satisfies the given predicate.
- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](mldatatable/rows-swift.struct/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.
- [func lastIndex(of: Self.Element) -> Self.Index?](mldatatable/rows-swift.struct/lastindex(of:).md)
  Returns the last index where the specified value appears in the collection.
- [func lastIndex(where: (Self.Element) throws -> Bool) rethrows -> Self.Index?](mldatatable/rows-swift.struct/lastindex(where:).md)
  Returns the index of the last element in the collection that matches the given predicate.
- [func min(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](mldatatable/rows-swift.struct/min(by:).md)
  Returns the minimum element in the sequence, using the given predicate as the comparison between elements.
- [func max(by: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?](mldatatable/rows-swift.struct/max(by:).md)
  Returns the maximum element in the sequence, using the given predicate as the comparison between elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/rows-swift.struct/first(where:))*