# insert(_:at:)

**Framework**: Swift  
**Kind**: method

Inserts a new element into the array at the specified position.

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
mutating func insert(_ item: consuming Element, at index: Int)
```

#### Discussion

If the array does not have sufficient capacity to hold any more elements, then this reallocates storage to extend its capacity, using a geometric growth rate.

The new element is inserted before the element currently at the specified index. If you pass the array’s `endIndex` as the `index` parameter, then the new element is appended to the container.

All existing elements at or following the specified position are moved to make room for the new item.

> **Note**: O(`self.count`)

## Parameters

- `item`: The new element to insert into the array.
- `index`: The position at which to insert the new element. `index` must be a valid index in the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/insert(_:at:))*