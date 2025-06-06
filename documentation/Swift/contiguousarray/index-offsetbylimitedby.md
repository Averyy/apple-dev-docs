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

O(1)

## Parameters

- `i`: A valid index of the array.
- `distance`: The distance to offset  .
- `limit`: A valid index of the collection to use as a limit. If   ,   has no effect if it is less than  .   Likewise, if  ,   has no effect if it is greater   than  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/contiguousarray/index(_:offsetby:limitedby:))*