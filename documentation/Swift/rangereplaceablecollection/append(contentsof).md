# append(contentsOf:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Adds the elements of a sequence or collection to the end of this collection.

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
mutating func append<S>(contentsOf newElements: S) where S : Sequence, Self.Element == S.Element
```

#### Discussion

The collection being appended to allocates any additional necessary storage to hold the new elements.

The following example appends the elements of a `Range<Int>` instance to an array of integers:

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.append(contentsOf: 10...15)
print(numbers)
// Prints "[1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15]"
```

> **Complexity**: O(*m*), where *m* is the length of `newElements`.

## Parameters

- `newElements`: The elements to append to the collection.

## Default Implementations

### RangeReplaceableCollection Implementations
- [func append<S>(contentsOf: S)](./append%28contentsof%29-15j8g.md)
  Adds the elements of a sequence or collection to the end of this collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rangereplaceablecollection/append(contentsof:))*