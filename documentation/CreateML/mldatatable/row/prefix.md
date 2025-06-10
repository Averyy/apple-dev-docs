# prefix(_:)

**Framework**: Create ML  
**Kind**: method

Returns a subsequence, up to the specified maximum length, containing the initial elements of the collection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func prefix(_ maxLength: Int) -> Self.SubSequence
```

#### Return Value

A subsequence starting at the beginning of this collection with at most `maxLength` elements.

#### Discussion

If the maximum length exceeds the number of elements in the collection, the result contains all the elements in the collection.

```None
let numbers = [1, 2, 3, 4, 5]
print(numbers.prefix(2))
// Prints "[1, 2]"
print(numbers.prefix(10))
// Prints "[1, 2, 3, 4, 5]"
```

> **Note**: O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(), where  is the number of elements to select from the beginning of the collection.

## Parameters

- `maxLength`: The maximum number of elements to return.    must be greater than or equal to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/row/prefix(_:))*