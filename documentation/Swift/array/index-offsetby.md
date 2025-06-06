# index(_:offsetBy:)

**Framework**: Swift  
**Kind**: method

Returns an index that is the specified distance from the given index.

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
func index(_ i: Int, offsetBy distance: Int) -> Int
```

#### Return Value

An index offset by `distance` from the index `i`. If `distance` is positive, this is the same value as the result of `distance` calls to `index(after:)`. If `distance` is negative, this is the same value as the result of `abs(distance)` calls to `index(before:)`.

#### Discussion

The following example obtains an index advanced four positions from an array’s starting index and then prints the element at that position.

```swift
let numbers = [10, 20, 30, 40, 50]
let i = numbers.index(numbers.startIndex, offsetBy: 4)
print(numbers[i])
// Prints "50"
```

The value passed as `distance` must not offset `i` beyond the bounds of the collection.

## Parameters

- `i`: A valid index of the array.
- `distance`: The distance to offset  .

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
- [func formIndex(inout Self.Index, offsetBy: Int)](array/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func index(Int, offsetBy: Int, limitedBy: Int) -> Int?](array/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](array/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func distance(from: Int, to: Int) -> Int](array/distance(from:to:).md)
  Returns the distance between two indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/index(_:offsetby:))*