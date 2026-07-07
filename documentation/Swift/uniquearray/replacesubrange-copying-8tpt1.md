# replaceSubrange(_:copying:)

**Framework**: Swift  
**Kind**: method

Replaces the specified subrange of elements by copying the elements of the given buffer pointer, which must be fully initialized.

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
mutating func replaceSubrange(_ subrange: Range<Int>, copying newElements: UnsafeMutableBufferPointer<Element>)
```

#### Discussion

This method has the effect of removing the specified range of elements from the array and inserting the new elements starting at the same location. The number of new elements need not match the number of elements being removed.

If the capacity of the array isn’t sufficient to perform the replacement, then this reallocates the array’s storage to extend its capacity, using a geometric growth rate.

If you pass a zero-length range as the `subrange` parameter, this method inserts the elements of `newElements` at `subrange.lowerBound`. Calling the `insert(copying:at:)` method instead is preferred in this case.

Likewise, if you pass a zero-length buffer as the `newElements` parameter, this method removes the elements in the given subrange without replacement. Calling the `removeSubrange(_:)` method instead is preferred in this case.

> **Note**: O(*n* + *m*), where *n* is count of this array and *m* is the count of `newElements`.

## Parameters

- `subrange`: The subrange of the array to replace. The bounds of the range must be valid indices in the array.
- `newElements`: The new elements to copy into the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/replacesubrange(_:copying:)-8tpt1)*