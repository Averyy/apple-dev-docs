# distance(from:to:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns the distance between two indices.

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
func distance(from start: Int, to end: Int) -> Int
```

## Return Value

The distance between `start` and `end`.

## Parameters

- `start`: A valid index of the collection.
- `end`: Another valid index of the collection. If `end` is equal to `start`, the result is zero.

## See Also

### Manipulating Indices
- [var startIndex: Int](./startindex.md)
  The position of the first element in a nonempty array.
- [var endIndex: Int](./endindex.md)
  The array’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [func index(after: Int) -> Int](./index%28after%29.md)
  Returns the position immediately after the given index.
- [func formIndex(after: inout Int)](./formindex%28after%29.md)
  Replaces the given index with its successor.
- [func index(before: Int) -> Int](./index%28before%29.md)
  Returns the position immediately before the given index.
- [func formIndex(before: inout Int)](./formindex%28before%29.md)
  Replaces the given index with its predecessor.
- [func index(Int, offsetBy: Int) -> Int](./index%28_,offsetby%29.md)
  Returns an index that is the specified distance from the given index.
- [func formIndex(inout Self.Index, offsetBy: Int)](./formindex%28_,offsetby%29.md)
  Offsets the given index by the specified distance.
- [func index(Int, offsetBy: Int, limitedBy: Int) -> Int?](./index%28_,offsetby,limitedby%29.md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](./formindex%28_,offsetby,limitedby%29.md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/distance(from:to:))*