# lazy

**Framework**: Foundation  
**Kind**: property

A sequence containing the same elements as this sequence, but on which some operations, such as `map` and `filter`, are implemented lazily.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var lazy: LazySequence<Self> { get }
```

## See Also

- [func reduce<Result>(Result, (Result, Self.Element) throws -> Result) rethrows -> Result](data/reduce(_:_:).md)
  Returns the result of combining the elements of the sequence using the given closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/lazy)*