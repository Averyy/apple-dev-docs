# suffix(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns a subsequence, up to the given maximum length, containing the final elements of the collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func suffix(_ maxLength: Int) -> Self.SubSequence
```

## Return Value

A subsequence terminating at the end of the collection with at most `maxLength` elements.

## Discussion

If the maximum length exceeds the number of elements in the collection, the result contains the entire collection.

```swift
let numbers = [1, 2, 3, 4, 5]
print(numbers.suffix(2))
// Prints "[4, 5]"
print(numbers.suffix(10))
// Prints "[1, 2, 3, 4, 5]"
```

> **Complexity**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(*k*), where *k* is equal to `maxLength`.

## Parameters

- `maxLength`: The maximum number of elements to return. `maxLength` must be greater than or equal to zero.

## See Also

### Getting Substrings
- [subscript(Range<String.Index>) -> Substring](./subscript%28_%29-2so14.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript<R>(R) -> Self.SubSequence](./subscript%28_%29-4h7s3.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(UnboundedRange) -> Self.SubSequence](./subscript%28_%29-4al9c.md)
- [func prefix(Int) -> Self.SubSequence](./prefix%28_%29.md)
  Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.
- [func prefix(through: Self.Index) -> Self.SubSequence](./prefix%28through%29.md)
  Returns a subsequence from the start of the collection through the specified position.
- [func prefix(upTo: Self.Index) -> Self.SubSequence](./prefix%28upto%29.md)
  Returns a subsequence from the start of the collection up to, but not including, the specified position.
- [func prefix(while: (Self.Element) throws -> Bool) rethrows -> Self.SubSequence](./prefix%28while%29.md)
  Returns a subsequence containing the initial elements until `predicate` returns `false` and skipping the remaining elements.
- [func suffix(from: Self.Index) -> Self.SubSequence](./suffix%28from%29.md)
  Returns a subsequence from the specified position to the end of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/suffix(_:))*