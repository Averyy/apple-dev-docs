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
func index(_ i: Self.Index, offsetBy distance: Self.Index.Stride) -> Self.Index
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

> **Note**: O(1)

## Parameters

- `i`: A valid index of the collection.
- `distance`: The distance to offset `i`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint64/words-swift.struct/index(_:offsetby:))*