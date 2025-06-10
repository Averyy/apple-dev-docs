# index(_:offsetBy:limitedBy:)

**Framework**: MusicKit  
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
func index(_ i: MusicItemCollection<MusicItemType>.Index, offsetBy distance: Int, limitedBy limit: MusicItemCollection<MusicItemType>.Index) -> MusicItemCollection<MusicItemType>.Index?
```

#### Return Value

An index offset by `distance` from the index `i`, unless that index would be beyond `limit` in the direction of movement. In that case, the method returns `nil`.

#### Discussion

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

> **Note**: O(1)

## Parameters

- `i`: A valid index of the collection.
- `distance`: The distance to offset  .   must not be negative   unless the collection conforms to the    protocol.
- `limit`: A valid index of the collection to use as a limit. If   , a limit that is less than   has no effect.   Likewise, if  , a limit that is greater than   has no   effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicitemcollection/index(_:offsetby:limitedby:))*