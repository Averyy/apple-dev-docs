# append(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Adds a new element at the end of the array.

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
mutating func append(_ newElement: Element)
```

#### Discussion

Use this method to append a single element to the end of a mutable array.

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.append(100)
print(numbers)
// Prints "[1, 2, 3, 4, 5, 100]"
```

Because arrays increase their allocated capacity using an exponential strategy, appending a single element to an array is an O(1) operation when averaged over many calls to the `append(_:)` method. When an array has additional capacity and is not sharing its storage with another instance, appending an element is O(1). When an array needs to reallocate storage before appending or its storage is shared with another copy, appending is O(*n*), where *n* is the length of the array.

> **Complexity**: O(1) on average, over many calls to `append(_:)` on the same array.

## Parameters

- `newElement`: The element to append to the array.

## See Also

### Adding Elements
- [func insert(Element, at: Int)](./insert%28_,at%29.md)
  Inserts a new element at the specified position.
- [func insert<C>(contentsOf: C, at: Self.Index)](./insert%28contentsof,at%29.md)
  Inserts the elements of a sequence into the collection at the specified position.
- [func replaceSubrange<C>(Range<Int>, with: C)](./replacesubrange%28_,with%29.md)
  Replaces a range of elements with the elements in the specified collection.
- [func replaceSubrange<C, R>(R, with: C)](./replacesubrange%28_,with%29-7293p.md)
  Replaces the specified subrange of elements with the given collection.
- [func reserveCapacity(Int)](./reservecapacity%28_%29.md)
  Reserves enough space to store the specified number of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/append(_:))*