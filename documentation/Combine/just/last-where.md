# last(where:)

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
func last(where predicate: (Output) -> Bool) -> Optional<Output>.Publisher
```

## See Also

- [func first() -> Just<Output>](just/first.md)
- [func first(where: (Output) -> Bool) -> Optional<Output>.Publisher](just/first(where:).md)
- [func last() -> Just<Output>](just/last.md)
- [func output(at: Int) -> Optional<Output>.Publisher](just/output(at:).md)
- [func output<R>(in: R) -> Optional<Output>.Publisher](just/output(in:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/last(where:))*