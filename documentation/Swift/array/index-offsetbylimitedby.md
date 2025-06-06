# index(_:offsetBy:limitedBy:)

**Framework**: Swift  
**Kind**: method

Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.

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
func index(_ i: Int, offsetBy distance: Int, limitedBy limit: Int) -> Int?
```

#### Return Value

An index offset by `distance` from the index `i`, unless that index would be beyond `limit` in the direction of movement. In that case, the method returns `nil`.

#### Discussion

The following example obtains an index advanced four positions from an array’s starting index and then prints the element at that position. The operation doesn’t require going beyond the limiting `numbers.endIndex` value, so it succeeds.

```swift
let numbers = [10, 20, 30, 40, 50]
if let i = numbers.index(numbers.startIndex,
                         offsetBy: 4,
                         limitedBy: numbers.endIndex) {
    print(numbers[i])
}
// Prints "50"
```

The next example attempts to retrieve an index ten positions from `numbers.startIndex`, but fails, because that distance is beyond the index passed as `limit`.

```swift
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
- `limit`: A valid index of the collection to use as a limit. If   ,   has no effect if it is less than  .   Likewise, if  ,   has no effect if it is greater   than  .

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
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](array/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func distance(from: Int, to: Int) -> Int](array/distance(from:to:).md)
  Returns the distance between two indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/index(_:offsetby:limitedby:))*