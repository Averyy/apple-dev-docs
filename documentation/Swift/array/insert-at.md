# insert(_:at:)

**Framework**: Swift  
**Kind**: method

Inserts a new element at the specified position.

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
mutating func insert(_ newElement: Element, at i: Int)
```

#### Discussion

The new element is inserted before the element currently at the specified index. If you pass the array’s `endIndex` property as the `index` parameter, the new element is appended to the array.

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.insert(100, at: 3)
numbers.insert(200, at: numbers.endIndex)

print(numbers)
// Prints "[1, 2, 3, 100, 4, 5, 200]"
```

> **Note**: O(), where  is the length of the array. If `i == endIndex`, this method is equivalent to `append(_:)`.

## Parameters

- `newElement`: The new element to insert into the array.
- `i`: The position at which to insert the new element.    must be a valid index of the array or equal to its    property.

## See Also

- [func append(Element)](array/append(_:).md)
  Adds a new element at the end of the array.
- [func insert<C>(contentsOf: C, at: Self.Index)](array/insert(contentsof:at:).md)
  Inserts the elements of a sequence into the collection at the specified position.
- [func replaceSubrange<C>(Range<Int>, with: C)](array/replacesubrange(_:with:).md)
  Replaces a range of elements with the elements in the specified collection.
- [func replaceSubrange<C, R>(R, with: C)](array/replacesubrange(_:with:)-7293p.md)
  Replaces the specified subrange of elements with the given collection.
- [func reserveCapacity(Int)](array/reservecapacity(_:).md)
  Reserves enough space to store the specified number of elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/insert(_:at:))*