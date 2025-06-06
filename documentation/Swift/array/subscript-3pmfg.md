# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

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
subscript(x: (UnboundedRange_) -> ()) -> Self.SubSequence { get set }
```

## See Also

- [subscript(Int) -> Element](array/subscript(_:)-25iat.md)
  Accesses the element at the specified position.
- [var first: Self.Element?](array/first.md)
  The first element of the collection.
- [var last: Self.Element?](array/last.md)
  The last element of the collection.
- [subscript(Range<Int>) -> ArraySlice<Element>](array/subscript(_:)-53fvb.md)
  Accesses a contiguous subrange of the array’s elements.
- [subscript<R>(R) -> Self.SubSequence](array/subscript(_:)-3kwny.md)
- [subscript<R>(R) -> Self.SubSequence](array/subscript(_:)-4h7rl.md)
  Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [func randomElement() -> Self.Element?](array/randomelement.md)
  Returns a random element of the collection.
- [func randomElement<T>(using: inout T) -> Self.Element?](array/randomelement(using:).md)
  Returns a random element of the collection, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/subscript(_:)-3pmfg)*