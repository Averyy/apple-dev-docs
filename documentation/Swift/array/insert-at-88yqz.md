# insert(_:at:)

**Framework**: Swift  
**Kind**: method

Inserts a new element into the collection at the specified position.

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
mutating func insert(_ newElement: Self.Element, at i: Self.Index)
```

#### Discussion

The new element is inserted before the element currently at the specified index. If you pass the collection’s `endIndex` property as the `index` parameter, the new element is appended to the collection.

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.insert(100, at: 3)
numbers.insert(200, at: numbers.endIndex)

print(numbers)
// Prints "[1, 2, 3, 100, 4, 5, 200]"
```

Calling this method may invalidate any existing indices for use with this collection.

> **Note**: O(), where  is the length of the collection. If `i == endIndex`, this method is equivalent to `append(_:)`.

O(), where  is the length of the collection. If `i == endIndex`, this method is equivalent to `append(_:)`.

## Parameters

- `newElement`: The new element to insert into the collection.
- `i`: The position at which to insert the new element.    must be a valid index into the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/insert(_:at:)-88yqz)*