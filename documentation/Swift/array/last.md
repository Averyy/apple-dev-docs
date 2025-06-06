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

## See Also

- [subscript(Int) -> Element](array/subscript(_:)-25iat.md)
  Accesses the element at the specified position.
- [var first: Self.Element?](array/first.md)
  The first element of the collection.
- [subscript(Range<Int>) -> ArraySlice<Element>](array/subscript(_:)-53fvb.md)
  Accesses a contiguous subrange of the array’s elements.
- [subscript<R>(R) -> Self.SubSequence](array/subscript(_:)-3kwny.md)
- [subscript<R>(R) -> Self.SubSequence](array/subscript(_:)-4h7rl.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript((UnboundedRange_) -> ()) -> Self.SubSequence](array/subscript(_:)-3pmfg.md)
- [func randomElement() -> Self.Element?](array/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](array/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Swift/array/last)*