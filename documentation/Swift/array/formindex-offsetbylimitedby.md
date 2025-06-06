# formIndex(_:offsetBy:limitedBy:)

**Framework**: Swift  
**Kind**: method

Offsets the given index by the specified distance, or so that it equals the given limiting index.

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
func formIndex(_ i: inout Self.Index, offsetBy distance: Int, limitedBy limit: Self.Index) -> Bool
```

#### Return Value

`true` if `i` has been offset by exactly `distance` steps without going beyond `limit`; otherwise, `false`. When the return value is `false`, the value of `i` is equal to `limit`.

#### Discussion

The value passed as `distance` must not offset `i` beyond the bounds of the collection, unless the index passed as `limit` prevents offsetting beyond those bounds.

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the absolute value of `distance`.

O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the absolute value of `distance`.

## Parameters

- `i`: A valid index of the collection.
- `distance`: The distance to offset  .   must not be negative   unless the collection conforms to the    protocol.
- `limit`: A valid index of the collection to use as a limit. If   , a limit that is less than   has no effect.   Likewise, if  , a limit that is greater than   has no   effect.

## See Also

- [var startIndex: Int](array/startindex.md)
  The position of the first element in a nonempty array.
- [var endIndex: Int](array/endindex.md)
  The array’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [func index(after: Int) -> Int](array/index(after:).md)
  Returns the position immediately after the given index.
- [func formIndex(after: inout Int)](array/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(before: Int) -> Int](array/index(before:).md)
  Returns the position immediately before the given index.
- [func formIndex(before: inout Int)](array/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(Int, offsetBy: Int) -> Int](array/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func formIndex(inout Self.Index, offsetBy: Int)](array/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func index(Int, offsetBy: Int, limitedBy: Int) -> Int?](array/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func distance(from: Int, to: Int) -> Int](array/distance(from:to:).md)
  Returns the distance between two indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/formindex(_:offsetby:limitedby:))*