# index(before:)

**Framework**: Swift  
**Kind**: method

Returns the position immediately before the given index.

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
func index(before index: Int) -> Int
```

#### Return Value

The index immediately preceding `i`.

#### Discussion

> **Note**: To improve performance, this method does not validate that the index is valid before decrementing it. Index validation is deferred until the resulting index is used to access an element. This optimization may be removed in future versions; do not rely on it.

> **Note**: O(1)

## Parameters

- `index`: A valid index of the array. `i` must be greater than `startIndex`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/index(before:))*