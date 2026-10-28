# first

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

The first element of the collection.

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
var first: Self.Element? { get }
```

## Discussion

If the collection is empty, the value of this property is `nil`.

```swift
let numbers = [10, 20, 30, 40, 50]
if let firstNumber = numbers.first {
    print(firstNumber)
}
// Prints "10"
```

## See Also

### Getting Characters and Bytes
- [subscript(String.Index) -> Character](./subscript%28_%29-lc0v.md)
  Accesses the character at the given position.
- [var last: Self.Element?](./last.md)
  The last element of the collection.
- [func randomElement() -> Self.Element?](./randomelement%28%29.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](./randomelement%28using%29.md)
  Returns a random element of the collection, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/first)*