# output(at:)

**Framework**: Combine  
**Kind**: method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func output(at index: Int) -> Optional<Output>.Publisher
```

## See Also

- [func first() -> Just<Output>](just/first.md)
- [func first(where: (Output) -> Bool) -> Optional<Output>.Publisher](just/first(where:).md)
- [func tryFirst(where: (Self.Output) throws -> Bool) -> Publishers.TryFirstWhere<Self>](just/tryfirst(where:).md)
  Publishes the first element of a stream to satisfy a throwing predicate closure, then finishes normally.
- [func last() -> Just<Output>](just/last.md)
- [func last(where: (Output) -> Bool) -> Optional<Output>.Publisher](just/last(where:).md)
- [func tryLast(where: (Self.Output) throws -> Bool) -> Publishers.TryLastWhere<Self>](just/trylast(where:).md)
  Publishes the last element of a stream that satisfies an error-throwing predicate closure, after the stream finishes.
- [func output<R>(in: R) -> Optional<Output>.Publisher](just/output(in:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/output(at:))*