# ignoreOutput()

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
func ignoreOutput() -> Empty<Publishers.Sequence<Elements, Failure>.Output, Failure>
```

## See Also

- [func collect() -> Result<[Publishers.Sequence<Elements, Failure>.Output], Failure>.Publisher](publishers/sequence/collect.md)
- [func reduce<T>(T, (T, Publishers.Sequence<Elements, Failure>.Output) -> T) -> Result<T, Failure>.Publisher](publishers/sequence/reduce(_:_:).md)
- [func tryReduce<T>(T, (T, Publishers.Sequence<Elements, Failure>.Output) throws -> T) -> Result<T, any Error>.Publisher](publishers/sequence/tryreduce(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/sequence/ignoreoutput())*