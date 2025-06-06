# endIndex

**Framework**: Swift  
**Kind**: property  
**Required**: Yes

The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.

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
var endIndex: Self.Index { get }
```

#### Discussion

When you need a range that includes the last element of a collection, use the half-open range operator (`..<`) with `endIndex`. The `..<` operator creates a range that doesn’t include the upper bound, so it’s always safe to use with `endIndex`. For example:

```swift
let numbers = [10, 20, 30, 40, 50]
if let index = numbers.firstIndex(of: 30) {
    print(numbers[index ..< numbers.endIndex])
}
// Prints "[30, 40, 50]"
```

If the collection is empty, `endIndex` is equal to `startIndex`.

## See Also

- [var startIndex: Self.Index](collection/startindex.md)
  The position of the first element in a nonempty collection.
- [var indices: Self.Indices](collection/indices-9kkbf.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [func index(after: Self.Index) -> Self.Index](collection/index(after:).md)
  Returns the position immediately after the given index.
- [func formIndex(inout Self.Index, offsetBy: Int)](collection/formindex(_:offsetby:)-393pr.md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](collection/formindex(_:offsetby:limitedby:)-6jwra.md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collection/endindex)*