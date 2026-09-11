# setCapacity(_:)

**Framework**: Swift  
**Kind**: method

Grow or shrink the capacity of a unique array instance without discarding its contents.

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
mutating func setCapacity(_ newCapacity: Int)
```

#### Discussion

This operation replaces the array’s storage buffer with a newly allocated buffer of the specified capacity, moving all existing elements to its new storage. The old storage is then deallocated.

> **Note**: O(`count`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/setcapacity(_:))*