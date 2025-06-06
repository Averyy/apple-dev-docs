# last

**Framework**: Tabulardata  
**Kind**: property

The last element of the collection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var last: Self.Element? { get }
```

#### Discussion

If the collection is empty, the value of this property is `nil`.

```None
let numbers = [10, 20, 30, 40, 50]
if let lastNumber = numbers.last {
    print(lastNumber)
}
// Prints "50"
```

> **Note**: O(1)

## See Also

- [func last(where: (Self.Element) throws -> Bool) rethrows -> Self.Element?](anycolumnslice/last(where:).md)
  Returns the last element of the sequence that satisfies the given predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/anycolumnslice/last)*