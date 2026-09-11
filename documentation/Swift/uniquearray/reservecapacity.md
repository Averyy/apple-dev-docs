# reserveCapacity(_:)

**Framework**: Swift  
**Kind**: method

Ensure that the array has capacity to store the specified number of elements, by growing its storage buffer if necessary.

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
mutating func reserveCapacity(_ n: Int)
```

#### Discussion

If `capacity < n`, then this operation reallocates the unique array’s storage to grow it; on return, the array’s capacity becomes `n`. Otherwise the array is left as is.

> **Note**: O(`count`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/reservecapacity(_:))*