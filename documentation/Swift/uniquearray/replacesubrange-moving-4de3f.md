# replaceSubrange(_:moving:)

**Framework**: Swift  
**Kind**: method

Replaces the specified range of elements by moving the elements of a fully initialized buffer into their place. On return, the buffer is left in an uninitialized state.

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
mutating func replaceSubrange(_ subrange: Range<Int>, moving newElements: UnsafeMutableBufferPointer<Element>)
```

#### Discussion

This method has the effect of removing the specified range of elements from the array and inserting the new elements starting at the same location. The number of new elements need not match the number of elements being removed.

If the array does not have sufficient capacity to perform the replacement, then this reallocates the array’s storage to extend its capacity, using a geometric growth rate.

If you pass a zero-length range as the `subrange` parameter, this method inserts the elements of `newElements` at `subrange.lowerBound`. Calling the `insert(copying:at:)` method instead is preferred in this case.

Likewise, if you pass a zero-length buffer as the `newElements` parameter, this method removes the elements in the given subrange without replacement. Calling the `removeSubrange(_:)` method instead is preferred in this case.

> **Note**: O(`self.count` + `newElements.count`)

## Parameters

- `subrange`: The subrange of the array to replace. The bounds of the range must be valid indices in the array.
- `newElements`: A fully initialized buffer whose contents to move into the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/replacesubrange(_:moving:)-4de3f)*