# last

**Framework**: Swift  
**Kind**: property

The last element of the collection.

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
var last: Self.Element? { get }
```

#### Discussion

If the collection is empty, the value of this property is `nil`.

```swift
let numbers = [10, 20, 30, 40, 50]
if let lastNumber = numbers.last {
    print(lastNumber)
}
// Prints "50"
```

> **Note**: O(1)

O(1)

## See Also

- [subscript(String.Index) -> Character](string/subscript(_:)-lc0v.md)
  Accesses the character at the given position.
- [var first: Self.Element?](string/first.md)
  The first element of the collection.
- [func randomElement() -> Self.Element?](string/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](string/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/last)*