# insert(moving:at:)

**Framework**: Swift  
**Kind**: method

Moves the elements of an output span into this array, starting at the specified position, and leaving the span empty.

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
mutating func insert(moving items: inout OutputSpan<Element>, at index: Int)
```

#### Discussion

All existing elements at or following the specified position are moved to make room for the new items.

If the array does not have sufficient capacity to hold the new elements, then this reallocates storage to extend its capacity, using a geometric growth rate.

> **Note**: O(`self.count` + `items.count`)

## Parameters

- `items`: An output span whose contents to move into the array.
- `index`: The position at which to insert the new items. `index` must be a valid index in the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/insert(moving:at:)-6d5t1)*