# reserveCapacity(_:)

**Framework**: Swift  
**Kind**: method

Ensure that the array has capacity to store the specified number of elements, by growing its storage buffer if necessary.

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
mutating func reserveCapacity(_ n: Int)
```

#### Discussion

If `capacity < n`, then this operation reallocates the unique array’s storage to grow it; on return, the array’s capacity becomes `n`. Otherwise the array is left as is.

> **Note**: O(`count`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/reservecapacity(_:))*