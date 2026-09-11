# formIndex(before:)

**Framework**: Swift  
**Kind**: method

Replaces the given index with its predecessor.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func formIndex(before index: inout Int)
```

#### Discussion

> **Note**: To improve performance, this method does not validate that the given index is valid before decrementing it. Index validation is deferred until the resulting index is used to access an element. This optimization may be removed in future versions; do not rely on it.

> **Note**: O(1)

## Parameters

- `index`: A valid index of the array. `i` must be greater than `startIndex`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/formindex(before:))*