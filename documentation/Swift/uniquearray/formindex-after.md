# formIndex(after:)

**Framework**: Swift  
**Kind**: method

Replaces the given index with its successor.

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
func formIndex(after index: inout Int)
```

#### Discussion

> **Note**: To improve performance, this method does not validate that the given index is valid before incrementing it. Index validation is deferred until the resulting index is used to access an element. This optimization may be removed in future versions; do not rely on it.

> **Note**: O(1)

## Parameters

- `index`: A valid index of the array. `i` must be less than `endIndex`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/formindex(after:))*