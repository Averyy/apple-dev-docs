# insert(contentsOf:at:)

**Framework**: System  
**Kind**: method

Inserts the elements of a sequence into the collection at the specified position.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
mutating func insert<C>(contentsOf newElements: C, at i: Self.Index) where C : Collection, Self.Element == C.Element
```

#### Discussion

The new elements are inserted before the element currently at the specified index. If you pass the collection’s `endIndex` property as the `index` parameter, the new elements are appended to the collection.

Here’s an example of inserting a range of integers into an array of the same type:

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.insert(contentsOf: 100...103, at: 3)
print(numbers)
// Prints "[1, 2, 3, 100, 101, 102, 103, 4, 5]"
```

Calling this method may invalidate any existing indices for use with this collection.

> **Note**: O( + ), where  is length of this collection and  is the length of `newElements`. If `i == endIndex`, this method is equivalent to `append(contentsOf:)`.

O( + ), where  is length of this collection and  is the length of `newElements`. If `i == endIndex`, this method is equivalent to `append(contentsOf:)`.

## Parameters

- `newElements`: The new elements to insert into the collection.
- `i`: The position at which to insert the new elements.    must be a valid index of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/componentview/insert(contentsof:at:))*