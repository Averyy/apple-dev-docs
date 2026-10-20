# last(where:)

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
func last(where predicate: (Output) -> Bool) -> Optional<Output>.Publisher
```

## See Also

### Selecting specific elements
- [func first() -> Just<Output>](./first%28%29.md)
- [func first(where: (Output) -> Bool) -> Optional<Output>.Publisher](./first%28where%29.md)
- [func last() -> Just<Output>](./last%28%29.md)
- [func output(at: Int) -> Optional<Output>.Publisher](./output%28at%29.md)
- [func output<R>(in: R) -> Optional<Output>.Publisher](./output%28in%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/last(where:))*