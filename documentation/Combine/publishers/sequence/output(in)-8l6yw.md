# output(in:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

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
func output(in range: Range<Elements.Index>) -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure>
```

Available when `Elements` conforms to `Collection` and `Failure` conforms to `Error`.

## See Also

### Selecting specific elements
- [func first() -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](./first%28%29.md)
- [func first(where: (Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](./first%28where%29.md)
- [func last() -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](./last%28%29.md)
- [func last(where: (Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](./last%28where%29.md)
- [func output(at: Elements.Index) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](./output%28at%29-3r7zo.md)
- [func output(at: Elements.Index) -> Optional<Publishers.Sequence<Elements, Failure>.Output>.Publisher](./output%28at%29-9kto7.md)
- [func output(in: Range<Elements.Index>) -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure>](./output%28in%29-6g2zc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/sequence/output(in:)-8l6yw)*