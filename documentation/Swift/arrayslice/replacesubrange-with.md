# replaceSubrange(_:with:)

**Framework**: Swift  
**Kind**: method

Replaces a range of elements with the elements in the specified collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func replaceSubrange<C>(_ subrange: Range<Int>, with newElements: C) where Element == C.Element, C : Collection
```

#### Discussion

This method has the effect of removing the specified range of elements from the array and inserting the new elements at the same location. The number of new elements need not match the number of elements being removed.

In this example, three elements in the middle of an array of integers are replaced by the five elements of a `Repeated<Int>` instance.

```swift
 var nums = [10, 20, 30, 40, 50]
 nums.replaceSubrange(1...3, with: repeatElement(1, count: 5))
 print(nums)
 // Prints "[10, 1, 1, 1, 1, 1, 50]"
```

If you pass a zero-length range as the `subrange` parameter, this method inserts the elements of `newElements` at `subrange.startIndex`. Calling the `insert(contentsOf:at:)` method instead is preferred.

Likewise, if you pass a zero-length collection as the `newElements` parameter, this method removes the elements in the given subrange without replacement. Calling the `removeSubrange(_:)` method instead is preferred.

> **Note**: O( + ), where  is length of the array and  is the length of `newElements`. If the call to this method simply appends the contents of `newElements` to the array, this method is equivalent to `append(contentsOf:)`.

## Parameters

- `subrange`: The subrange of the array to replace. The start and end of   a subrange must be valid indices of the array.
- `newElements`: The new elements to add to the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/arrayslice/replacesubrange(_:with:))*