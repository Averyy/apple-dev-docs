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

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(*k*), where *k* is the absolute value of `distance`.

## Parameters

- `i`: A valid index of the collection.
- `distance`: The distance to offset `i`. `distance` must not be negative unless the collection conforms to the `BidirectionalCollection` protocol.
- `limit`: A valid index of the collection to use as a limit. If `distance > 0`, a limit that is less than `i` has no effect. Likewise, if `distance < 0`, a limit that is greater than `i` has no effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazysequence/formindex(_:offsetby:limitedby:))*