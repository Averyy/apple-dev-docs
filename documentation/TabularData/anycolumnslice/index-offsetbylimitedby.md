# index(_:offsetBy:limitedBy:)

**Framework**: Tabulardata  
**Kind**: method

Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.

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
func index(_ i: Self.Index, offsetBy distance: Int, limitedBy limit: Self.Index) -> Self.Index?
```

#### Return Value

An index offset by `distance` from the index `i`, unless that index would be beyond `limit` in the direction of movement. In that case, the method returns `nil`.

#### Discussion

The following example obtains an index advanced four positions from an array’s starting index and then prints the element at that position. The operation doesn’t require going beyond the limiting `numbers.endIndex` value, so it succeeds.

```None
let numbers = [10, 20, 30, 40, 50]
let i = numbers.index(numbers.startIndex, offsetBy: 4)
print(numbers[i])
// Prints "50"
```

The next example attempts to retrieve an index ten positions from `numbers.startIndex`, but fails, because that distance is beyond the index passed as `limit`.

```None
let j = numbers.index(numbers.startIndex,
                      offsetBy: 10,
                      limitedBy: numbers.endIndex)
print(j)
// Prints "nil"
```

The value passed as `distance` must not offset `i` beyond the bounds of the collection, unless the index passed as `limit` prevents offsetting beyond those bounds.

> **Note**: O(1)

## Parameters

- `i`: A valid index of the array.
- `distance`: The distance to offset  .
- `limit`: A valid index of the collection to use as a limit. If   ,   should be greater than   to have any   effect. Likewise, if  ,   should be less than    to have any effect.

## See Also

- [var startIndex: Int](anycolumnslice/startindex.md)
  The index of the initial element in the column slice.
- [var endIndex: Int](anycolumnslice/endindex.md)
  The index of the final element in the column slice.
- [func index(before: Int) -> Int](anycolumnslice/index(before:).md)
  Returns the index immediately before an element index.
- [func index(after: Int) -> Int](anycolumnslice/index(after:).md)
  Returns the index immediately after an element index.
- [func formIndex(before: inout Self.Index)](anycolumnslice/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func formIndex(after: inout Self.Index)](anycolumnslice/formindex(after:).md)
  Replaces the given index with its successor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumnslice/index(_:offsetby:limitedby:))*