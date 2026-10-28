# index(after:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the position immediately after the given index.

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
func index(after i: Self.Index) -> Self.Index
```

## Return Value

The index value immediately after `i`.

## Discussion

The successor of an index must be well defined. For an index `i` into a collection `c`, calling `c.index(after: i)` returns the same index every time.

## Parameters

- `i`: A valid index of the collection. `i` must be less than `endIndex`.

## Default Implementations

### BidirectionalCollection Implementations
- [func index(after: Self.Index) -> Self.Index](../bidirectionalcollection/index%28after%29-4zlq6.md)
  Returns the position immediately after the given index.

## See Also

### Manipulating Indices
- [var startIndex: Self.Index](./startindex.md)
  The position of the first element in a nonempty collection.
- [var endIndex: Self.Index](./endindex.md)
  The collection’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [var indices: Self.Indices](./indices-9kkbf.md)
  The indices that are valid for subscripting the collection, in ascending order.
- [func formIndex(inout Self.Index, offsetBy: Int)](./formindex%28_,offsetby%29-393pr.md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](./formindex%28_,offsetby,limitedby%29-6jwra.md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/collection/index(after:))*