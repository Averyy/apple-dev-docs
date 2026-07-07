# removeLast(_:)

**Framework**: Swift  
**Kind**: method

Removes and discards the specified number of elements from the end of the array.

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
mutating func removeLast(_ k: Int)
```

#### Discussion

Attempting to remove more elements than exist in the array triggers a runtime error.

> **Note**: O(`k`)

## Parameters

- `k`: The number of elements to remove from the array. `k` must be greater than or equal to zero and must not exceed the count of the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/removelast(_:))*