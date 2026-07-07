# insert(moving:at:)

**Framework**: Swift  
**Kind**: method

Moves the elements of a fully initialized buffer into this array, starting at the specified position, and leaving the buffer uninitialized.

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
mutating func insert(moving items: UnsafeMutableBufferPointer<Element>, at index: Int)
```

#### Discussion

If the array does not have sufficient capacity to hold all elements, then this reallocates storage to extend its capacity, using a geometric growth rate.

> **Note**: O(`self.count` + `items.count`)

## Parameters

- `items`: A fully initialized buffer whose contents to move into the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/insert(moving:at:)-4f2qc)*