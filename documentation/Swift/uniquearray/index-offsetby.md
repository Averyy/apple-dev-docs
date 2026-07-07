# index(_:offsetBy:)

**Framework**: Swift  
**Kind**: method

Returns an index that is the specified distance from the given index.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func index(_ index: Int, offsetBy n: Int) -> Int
```

#### Return Value

An index offset by distance from `index`. If `n` is positive, this is the same value as the result of `n` calls to `index(after:)`. If `n` is negative, this is the same value as the result of `abs(n)` calls to `index(before:)`.

#### Discussion

The value passed as `n` must not offset `index` beyond the bounds of the array.

> **Note**: To improve performance, this method does not validate that the given index is valid before offseting it. Index validation is deferred until the resulting index is used to access an element. This optimization may be removed in future versions; do not rely on it.

> **Note**: O(1)

## Parameters

- `index`: A valid index of the array.
- `n`: The distance by which to offset `index`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/index(_:offsetby:))*