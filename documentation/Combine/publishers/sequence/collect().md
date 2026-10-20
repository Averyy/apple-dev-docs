# collect()

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
func collect() -> Result<[Publishers.Sequence<Elements, Failure>.Output], Failure>.Publisher
```

Available when `Elements` conforms to `Sequence` and `Failure` conforms to `Error`.

## See Also

### Reducing elements
- [func ignoreOutput() -> Empty<Publishers.Sequence<Elements, Failure>.Output, Failure>](./ignoreoutput%28%29.md)
- [func reduce<T>(T, (T, Publishers.Sequence<Elements, Failure>.Output) -> T) -> Result<T, Failure>.Publisher](./reduce%28_,_%29.md)
- [func tryReduce<T>(T, (T, Publishers.Sequence<Elements, Failure>.Output) throws -> T) -> Result<T, any Error>.Publisher](./tryreduce%28_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/sequence/collect())*