# endIndex

**Framework**: Swift  
**Kind**: property

The array’s “past the end” position—that is, the position one greater than the last valid subscript argument.

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
var endIndex: Int { get }
```

#### Discussion

When you need a range that includes the last element of an array, use the half-open range operator (`..<`) with `endIndex`. The `..<` operator creates a range that doesn’t include the upper bound, so it’s always safe to use with `endIndex`. For example:

```swift
let numbers = [10, 20, 30, 40, 50]
if let i = numbers.firstIndex(of: 30) {
    print(numbers[i ..< numbers.endIndex])
}
// Prints "[30, 40, 50]"
```

If the array is empty, `endIndex` is equal to `startIndex`.

## See Also

- [var startIndex: Int](array/startindex.md)
  The position of the first element in a nonempty array.
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
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](array/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func distance(from: Int, to: Int) -> Int](array/distance(from:to:).md)
  Returns the distance between two indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/endindex)*