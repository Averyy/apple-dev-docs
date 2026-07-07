# insert(copying:at:)

**Framework**: Swift  
**Kind**: method

Copies the elements of a span into this array at the specified position.

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
mutating func insert(copying newElements: Span<Element>, at index: Int)
```

#### Discussion

The new elements are inserted before the element currently at the specified index. If you pass the array’s `endIndex` as the `index` parameter, then the new elements are appended to the end of the array.

All existing elements at or following the specified position are moved to make room for the new item.

If the array does not have sufficient capacity to hold enough elements, then this reallocates the array’s storage to extend its capacity, using a geometric growth rate.

> **Note**: O(`self.count` + `newElements.count`)

## Parameters

- `newElements`: The new elements to insert into the array.
- `index`: The position at which to insert the new elements. It must be a valid index of the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/insert(copying:at:)-2g824)*