# reduce(_:_:)

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
func reduce<T>(_ initialResult: T, _ nextPartialResult: @escaping (T, Publishers.Sequence<Elements, Failure>.Output) -> T) -> Result<T, Failure>.Publisher
```

## See Also

- [func collect() -> Result<[Publishers.Sequence<Elements, Failure>.Output], Failure>.Publisher](publishers/sequence/collect.md)
- [func ignoreOutput() -> Empty<Publishers.Sequence<Elements, Failure>.Output, Failure>](publishers/sequence/ignoreoutput.md)
- [func tryReduce<T>(T, (T, Publishers.Sequence<Elements, Failure>.Output) throws -> T) -> Result<T, any Error>.Publisher](publishers/sequence/tryreduce(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/sequence/reduce(_:_:))*