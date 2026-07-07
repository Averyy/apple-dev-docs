# append(moving:)

**Framework**: Swift  
**Kind**: method

Moves the elements of a buffer to the end of this array, leaving the buffer uninitialized.

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
mutating func append(moving items: UnsafeMutableBufferPointer<Element>)
```

#### Discussion

If the array does not have sufficient capacity to hold all items in the buffer, then this reallocates the array’s storage to grow its capacity, using a geometric growth rate.

> **Note**: O(`count` + `items.count`)

## Parameters

- `items`: A fully initialized buffer whose contents to move into the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/append(moving:)-71oaj)*