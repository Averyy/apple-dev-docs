# index(after:)

**Framework**: Swift  
**Kind**: method

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
func index(after i: String.Index) -> String.Index
```

#### Return Value

The index value immediately after `i`.

## Parameters

- `i`: A valid index of the collection.   must be less than   .

## See Also

- [var startIndex: String.Index](string/startindex.md)
  The position of the first character in a nonempty string.
- [var endIndex: String.Index](string/endindex.md)
  A string’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [func formIndex(after: inout Self.Index)](string/formindex(after:).md)
  Replaces the given index with its successor.
- [func index(before: String.Index) -> String.Index](string/index(before:).md)
  Returns the position immediately before the given index.
- [func formIndex(before: inout Self.Index)](string/formindex(before:).md)
  Replaces the given index with its predecessor.
- [func index(String.Index, offsetBy: Int) -> String.Index](string/index(_:offsetby:).md)
  Returns an index that is the specified distance from the given index.
- [func index(String.Index, offsetBy: Int, limitedBy: String.Index) -> String.Index?](string/index(_:offsetby:limitedby:).md)
  Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.
- [func formIndex(inout Self.Index, offsetBy: Int)](string/formindex(_:offsetby:).md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](string/formindex(_:offsetby:limitedby:).md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func distance(from: String.Index, to: String.Index) -> Int](string/distance(from:to:).md)
  Returns the distance between two indices.
- [var indices: DefaultIndices<Self>](string/indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/index(after:))*