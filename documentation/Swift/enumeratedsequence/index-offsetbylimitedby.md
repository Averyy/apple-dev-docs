# index(_:offsetBy:limitedBy:)

**Framework**: Swift  
**Kind**: method

Returns an index that is the specified distance from the given index, unless that distance is beyond a given limiting index.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func index(_ i: EnumeratedSequence<Base>.Index, offsetBy distance: Int, limitedBy limit: EnumeratedSequence<Base>.Index) -> EnumeratedSequence<Base>.Index?
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

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the absolute value of `distance`.

## Parameters

- `i`: A valid index of the collection.
- `distance`: The distance to offset  .   must not be negative   unless the collection conforms to the    protocol.
- `limit`: A valid index of the collection to use as a limit. If   , a limit that is less than   has no effect.   Likewise, if  , a limit that is greater than   has no   effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/enumeratedsequence/index(_:offsetby:limitedby:))*