# index(_:offsetBy:limitedBy:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

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
func index(_ i: String.Index, offsetBy distance: Int, limitedBy limit: String.Index) -> String.Index?
```

## Return Value

An index offset by `distance` from the index `i`, unless that index would be beyond `limit` in the direction of movement. In that case, the method returns `nil`.

## Discussion

The following example obtains an index advanced four positions from a string’s starting index and then prints the character at that position. The operation doesn’t require going beyond the limiting `s.endIndex` value, so it succeeds.

```swift
let s = "Swift"
if let i = s.index(s.startIndex, offsetBy: 4, limitedBy: s.endIndex) {
    print(s[i])
}
// Prints "t"
```

The next example attempts to retrieve an index six positions from `s.startIndex` but fails, because that distance is beyond the index passed as `limit`.

```swift
let j = s.index(s.startIndex, offsetBy: 6, limitedBy: s.endIndex)
print(j)
// Prints "nil"
```

The value passed as `distance` must not offset `i` beyond the bounds of the collection, unless the index passed as `limit` prevents offsetting beyond those bounds.

> **Complexity**: O(*n*), where *n* is the absolute value of `distance`.

## Parameters

- `i`: A valid index of the collection.
- `distance`: The distance to offset `i`.
- `limit`: A valid index of the collection to use as a limit. If `distance > 0`, a limit that is less than `i` has no effect. Likewise, if `distance < 0`, a limit that is greater than `i` has no effect.

## See Also

### Manipulating Indices
- [var startIndex: String.Index](./startindex.md)
  The position of the first character in a nonempty string.
- [var endIndex: String.Index](./endindex.md)
  A string’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [func index(after: String.Index) -> String.Index](./index%28after%29.md)
  Returns the position immediately after the given index.
- [func formIndex(after: inout Self.Index)](./formindex%28after%29.md)
  Replaces the given index with its successor.
- [func index(before: String.Index) -> String.Index](./index%28before%29.md)
  Returns the position immediately before the given index.
- [func formIndex(before: inout Self.Index)](./formindex%28before%29.md)
  Replaces the given index with its predecessor.
- [func index(String.Index, offsetBy: Int) -> String.Index](./index%28_,offsetby%29.md)
  Returns an index that is the specified distance from the given index.
- [func formIndex(inout Self.Index, offsetBy: Int)](./formindex%28_,offsetby%29.md)
  Offsets the given index by the specified distance.
- [func formIndex(inout Self.Index, offsetBy: Int, limitedBy: Self.Index) -> Bool](./formindex%28_,offsetby,limitedby%29.md)
  Offsets the given index by the specified distance, or so that it equals the given limiting index.
- [func distance(from: String.Index, to: String.Index) -> Int](./distance%28from,to%29.md)
  Returns the distance between two indices.
- [var indices: DefaultIndices<Self>](./indices-swift.property.md)
  The indices that are valid for subscripting the collection, in ascending order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/index(_:offsetby:limitedby:))*