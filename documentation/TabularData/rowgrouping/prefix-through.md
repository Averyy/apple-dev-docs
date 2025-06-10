# prefix(through:)

**Framework**: TabularData  
**Kind**: method

Returns a subsequence from the start of the collection through the specified position.

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
func prefix(through position: Self.Index) -> Self.SubSequence
```

#### Return Value

A subsequence up to, and including, the given position.

#### Discussion

The resulting subsequence  the element at the position specified by the `through` parameter. The following example searches for the index of the number `40` in an array of integers, and then prints the prefix of the array up to, and including, that index:

```None
let numbers = [10, 20, 30, 40, 50, 60]
if let i = numbers.firstIndex(of: 40) {
    print(numbers.prefix(through: i))
}
// Prints "[10, 20, 30, 40]"
```

Using the `prefix(through:)` method is equivalent to using a partial closed range as the collection’s subscript. The subscript notation is preferred over `prefix(through:)`.

```None
if let i = numbers.firstIndex(of: 40) {
    print(numbers[...i])
}
// Prints "[10, 20, 30, 40]"
```

> **Note**: O(1)

## Parameters

- `position`: The index of the last element to include in the   resulting subsequence.   must be a valid index of the collection   that is not equal to the   property.

## See Also

- [func drop(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](rowgrouping/drop(while:).md)
  Returns a subsequence by skipping elements while `predicate` returns `true` and returning the remaining elements.
- [func dropFirst(Int) -> Self.SubSequence](rowgrouping/dropfirst(_:).md)
  Returns a subsequence containing all but the given number of initial elements.
- [func prefix(Int) -> Self.SubSequence](rowgrouping/prefix(_:).md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](rowgrouping/prefix(upto:).md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](rowgrouping/prefix(while:).md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func suffix(Int) -> Self.SubSequence](rowgrouping/suffix(_:).md)
  Returns a subsequence, up to the given maximum length, containing the final elements of the collection.
- [func suffix(from: Self.Index) -> Self.SubSequence](rowgrouping/suffix(from:).md)
  Returns a subsequence from the specified position to the end of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/rowgrouping/prefix(through:))*